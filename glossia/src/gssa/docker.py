#!/usr/bin/python3

import asyncio
import shutil
import json
import logging
import os

logger = logging.getLogger(__name__)

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from hachiko.hachiko import AIOEventHandler

from . import config
import gssa.error

default_dockerlaunch_socket_location = '/var/run/dockerlaunch/dockerlaunch.sock'


# Check for output in the Docker volume
class OutputHandler(AIOEventHandler, FileSystemEventHandler):
    def __init__(self, lock, loop=None, **kwargs):
        self._lock = lock

        AIOEventHandler.__init__(self, loop)
        FileSystemEventHandler.__init__(self, **kwargs)

    @asyncio.coroutine
    def on_moved(self, event):
        if event.dest_path.endswith('/output'):
            self._lock.release()


class Submitter:
    """Utility to manage communication with dockerlaunch.

    Submit the request to run an instance to the dockerlaunch daemon, also
    handling some of the standard bits and pieces of interface.

    """
    reader = None
    writer = None
    _cancelled = False
    _destroyed = False
    _socket_location = None
    _communication_lock = None

    def __init__(self):
        self._input_files = []
        self._output_files = []
        self._output_directory = None
        self._output_lock = asyncio.Lock()
        self._communication_lock = asyncio.Lock()

    def __del__(self):
        # Tidy up before quitting
        self.finalize()

    def set_update_socket(self, socket_location):
        """Set the socket that the bridge container should use to communicate."""
        self._socket_location = socket_location

    def copy_output(self, requested, target):
        """Retrieve output.

        Copy output files from the Docker volume to the simulation 'working
        directory'

        """
        if not self._output_directory:
            return None

        requested_location = os.path.join(self._output_directory, requested)
        target_location = os.path.join(target, requested)

        try:
            shutil.copyfile(requested_location, target_location)
        except shutil.SameFileError:
            # This is likely to be the case if we mount the output directory
            # to the bridge
            pass
        except:
            logger.exception('Could not copy output')
            return None

        return True

    def add_input(self, input_file):
        """Set additional input.

        Make a note that this file should be transferred to the Docker volume for
        the simulation

        """
        self._input_files.append(input_file)

    def output(self, requested, exists_only=False):
        """Return the content of the file ``requested``

        Args:
            requested (str): file name to request
            exists_only (Optional[bool]): only check existence, don't load

        Returns:
            str|bool: file content unless exists_only set, then existence True/False.

        """

        if not self._output_directory:
            return None

        requested_location = os.path.join(self._output_directory, requested)

        if exists_only:
            return os.path.exists(requested_location)
        else:
            try:
                with open(requested_location, 'r') as f:
                    return f.read()
            except:
                return None

    def notify_output(self, filename):
        """Print a message to highlight a new output file from Docker."""

        logger.debug('Output: %s' % filename)
        if filename not in self._output_files:
            self._output_files.append(filename)

    def send_command(self, writer, command, arguments=None):
        """Send a command to the dockerlaunch daemon."""

        logger.debug('--> %s %s' % (command, str(arguments)))
        writer.write(bytes("%s\n" % json.dumps({
            'command': command,
            'arguments': arguments
        }), 'UTF-8'))

    @asyncio.coroutine
    def run_script(self, loop, working_directory, image, files_required=[], magic_script=None):
        """Run the simulation.

        Args:
            loop (asyncio.BaseEventLoop): look to use for asynchronous calls.
            working_directory (str): location of simulation configuration/definition.
            image (str): a container image name.
                This must be known to dockerlaunch or it will refuse to run.
            files_required (Optional[array(str)]): files to return as output.
            magic_script (Optional[str]): DEPRECATED: script to upload to simulation
                container after all else in place as a trigger (default off).
        """
        success = True

        dockerlaunch_socket_location = config.get(
            "dockerlaunch.socket_location",
            default_dockerlaunch_socket_location
        )

        dump_logs = config.get(
            "dockerlaunch.dump_logs",
            False
        )

        # Connect to the dockerlaunch daemon (we should be in the `dockerlaunch`
        # group for this to work)
        try:
            reader, writer = yield from asyncio.open_unix_connection(
                dockerlaunch_socket_location
            )
        except Exception as e:
            logger.error("Could not open connection to dockerlaunch at {loc}: {exc}".format(
                loc=dockerlaunch_socket_location,
                exc=str(e)
            ))
            raise e

        # Read and write objects for reaching the daemon
        self.reader, self.writer = reader, writer

        # Lock the lock so that when we grab it again, it will hold until the output dir has
        # appeared (FIXME: needs timeout)
        yield from self._output_lock

        #try:
        #    temporary_directory = tempfile.TemporaryDirectory(prefix='/simdata/')
        #except Exception:
        #    logger.error("Could not create a temporary directory for docker")
        #    raise
        #os.chmod(temporary_directory.name, 0o755)

        #tmpdir = temporary_directory.name
        tmpdir = working_directory
        #self._temporary_directory = temporary_directory

        input_suffix = 'input.final'
        input_directory = os.path.join(tmpdir, input_suffix)
        input_tmp_suffix = 'input'
        input_tmp_directory = os.path.join(tmpdir, input_tmp_suffix)
        #os.makedirs(input_tmp_directory)

        #logger.info("Created temporary directory: %s" % tmpdir)

        logger.debug("Simulating")
        try:
            # Tell the daemon to fire up an instance
            self.send_command(writer, 'START', {
                'image': image,
                'update socket': self._socket_location,
                'volume location': os.path.basename(tmpdir)
            })
            success, message = yield from self.receive_response(reader)
            logger.debug('<-- %s %s' % (str(success), str(message)))

            if not success:
                raise RuntimeError('Could not start: %s', message)

            self.send_command(writer, 'CONTAINER')
            success, message = yield from self.receive_response(reader)
            logger.debug('<-- %s %s' % (str(success), str(message)))
            try:
                image_id = message['image_id']
            except KeyError:
                image_id = None

            with open(os.path.join(input_tmp_directory, 'glossia-simimage.txt'), 'w') as image_file:
                image_file.write(image_id if image_id else '[unknown]')

            # Set up our basic locations, for accessing the Docker volume
            if magic_script is not None:
                magic_script = os.path.join(
                    input_tmp_directory,
                    magic_script
                )
            #self._output_directory = os.path.join(
            #    tmpdir,
            #    message['output subdirectory']
            #)

            self._output_directory = os.path.join(tmpdir, 'output')
            logger.debug("Set magic script")

            # Start watching for output files of interest in the Docker volume
            event_handler = OutputHandler(self._output_lock, loop=loop)
            observer = Observer()
            observer.schedule(
                event_handler,
                tmpdir
            )
            # FIXME: this causes occasional spontaneous segfaults during file updating... diagnosis pending
            observer.start()
            logger.debug("Started observer")

            # Go through each file required by the simulation and put it into
            # the Docker volume
            #for f in files_required:
            #    to_location = os.path.join(input_tmp_directory, os.path.basename(f))
            #    from_location = os.path.join(working_directory, 'input', os.path.basename(f))
            #    if not f.startswith('.') and not os.path.isdir(to_location):
            #        logger.debug("Transferring %s to %s for docker" % (from_location, to_location))

            #        shutil.copyfile(
            #            from_location,
            #            to_location,
            #        )

            #for input_file in self._input_files:
            #    shutil.copyfile(input_file, os.path.join(input_tmp_directory, os.path.basename(input_file)))

            # Once those are copied, we can send the magic script, which tells
            # the instance to start processing. Note that, if the definition was
            # passed to the server in a TAR.GZ, this may already have been sent
            # above - however, this is None in that case.
            if magic_script is not None:
                with open(magic_script, 'w') as f, open(os.path.join(working_directory, 'start.py'), 'r') as g:
                    f.write(g.read())

                logger.debug("Wrote magic script to %s" % magic_script)

            os.rename(input_tmp_directory, input_directory)

            # observer.stop()

            # Wait for the simulation to finish
            # Wait until the output directory has arrived in this container's volumes
            # This avoids any critical communication between container and Glossia
            # (but it is important to allow cancellation)
            self._wait_fut = asyncio.ensure_future(self._output_lock.acquire())
            try:
                yield from self._wait_fut
            except asyncio.CancelledError:
                logger.warning("Cancelled simulation")
            finally:
                yield from self._communication_lock
                self._communication_lock.release()
                self._output_lock.release()

            self.send_command(writer, 'LOGS', None)
            success, message = yield from self.receive_response(reader)
            for handle in message:
                logger.debug('<-- %s %s %s' % (str(success), handle, str(message[handle].replace('\\n', '\n'))))

            if not success and not self._cancelled:
                raise RuntimeError('Could not retrieve logs: %s', message)

            # Get the simulation exit status
            exit_status = self.output(os.path.join('logs', 'exit_status'))

            outcome = False
            if exit_status:
                code_string, message = exit_status.split('\n', 1)
                if self._cancelled:
                    message = "[Cancelled] " + message
                try:
                    code = gssa.error.Error[code_string]
                except KeyError as e:
                    try:
                        code = gssa.error.Error(int(code_string))
                    except ValueError as e:
                        message += " [Code " + code_string + "]"
                        code = gssa.error.Error.E_UNKNOWN

                if code is gssa.error.Error.SUCCESS:
                    outcome = True
                else:
                    outcome = gssa.error.makeError(code, message)
            elif self._cancelled:
                code = gssa.error.Error.E_CANCELLED
                outcome = gssa.error.makeError(code, "Cancelled at user request")
            else:
                code = gssa.error.Error.E_UNKNOWN
                message = "Unknown error occurred (missing exit status)"
                outcome = gssa.error.makeError(code, message)

            # If we did not exit cleanly, inform the server
            (logger.debug if success is True else logger.warning)('<==> %s %s' % (str(code), str(message)))

            # Copy the logs back to the simulation 'working directory'
            for output_file in ('docker_inner.log', 'job.out', 'job.err'):
                logger.debug('-' * 20)
                logger.debug(output_file.upper())

                if dump_logs:
                    output_log = self.output(os.path.join('logs', output_file))

                    # Print out the logs
                    if output_log:
                        logger.debug(output_log)
                    else:
                        logger.warning("[no output from %s]" % output_file)
                elif not self.output(os.path.join('logs', output_file), exists_only=True):
                    logger.warning("[no output from %s]" % output_file)
        finally:
            self.finalize()

        return outcome

    @asyncio.coroutine
    def logs(self, only=None):
        """Retrieve logs from the simulation."""

        with (yield from self._communication_lock):
            self.send_command(self.writer, 'LOGS', {'only': only} if only else None)
            success, message = yield from self.receive_response(self.reader)
            logger.debug('<-- %s %s logs' % (str(success), str(only)))

        return message

    @asyncio.coroutine
    def cancel(self):
        """Break the output wait and instruct dockerlaunch to destroy simulation."""

        if not self._wait_fut:
            return False

        self._cancelled = True
        with (yield from self._communication_lock):
            self._wait_fut.cancel()
            yield from self.destroy(wait_for_response=True)
        return True

    @asyncio.coroutine
    def destroy(self, wait_for_response=True):
        """Destroy the simulation/bridge containers."""
        # destroy should be idempotent - that's fine.
        if self._destroyed:
            return

        if not self.reader or not self.writer:
            raise RuntimeError('No reader/writer members to access launcher daemon')

        # Tell the Docker side to tidy up
        self.send_command(self.writer, 'DESTROY', None)

        if wait_for_response:
            success, message = yield from self.receive_response(self.reader)
            logger.debug('<-- %s %s' % (str(success), str(message)))

            if success:
                self._destroyed = True
            else:
                raise RuntimeError('Could not destroy: %s', message)
        else:
            self._destroyed = True

    def finalize(self):
        """Close dockerlaunch connection."""
        if not self.reader or not self.writer:
            return

        writer = self.writer

        self.reader, self.writer = None, None

        writer.close()

    @asyncio.coroutine
    def receive_response(self, reader):
        """Handle JSON reply from dockerlaunch and format neatly."""
        while True:
            line = yield from reader.readline()

            if line:
                break

        # Turn the flat lines into a JSON pair: 'success' and 'message'
        line = line.decode('UTF-8').strip()

        try:
            message = json.loads(line)
        except ValueError as e:
            logger.error("Could not decode docker response")
            raise e

        try:
            success = message['success']
            message = message['message']
        except KeyError as e:
            raise e

        return success, message
