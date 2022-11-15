from zope.interface import implementer
import shutil

import os
import logging
import tempfile
import tarfile

from .transferrer import ITransferrer

logger = logging.getLogger(__name__)


# A transferrer that works only on the local machine, using /tmp to move files
# from client to server
@implementer(ITransferrer)
class TmpTransferrer:
    _input_archive = None

    def __init__(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

    # We expect the input archive to by a .tar.gz
    def pull_files(self, files, root, remote_root):
        temp_directory = None
        # If we have a specific archive, copy it across
        if self._input_archive:
            temp_directory = tempfile.mkdtemp()
            temp_archive = os.path.join(temp_directory, 'input.tar.gz')

            short_files = {}
            for k, v in files.items():
                short_files[k] = os.path.basename(v)

            try:
                shutil.copy(self._input_archive, temp_archive)
            except FileNotFoundError as e:
                logger.error("Could not transfer %s on /tmp to %s - not found" % (self._input_archive, temp_archive))
                raise e

            # Go through the files in the archive and extract any that have
            # names in our pull list. We do this to a temporary directory
            try:
                with tarfile.open(temp_archive, 'r:gz') as tar_file:
                    members = [m for m in tar_file.getmembers() if m.name in short_files.values()]
                    def is_within_directory(directory, target):
                        
                        abs_directory = os.path.abspath(directory)
                        abs_target = os.path.abspath(target)
                    
                        prefix = os.path.commonprefix([abs_directory, abs_target])
                        
                        return prefix == abs_directory
                    
                    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
                    
                        for member in tar.getmembers():
                            member_path = os.path.join(path, member.name)
                            if not is_within_directory(path, member_path):
                                raise Exception("Attempted Path Traversal in Tar File")
                    
                        tar.extractall(path, members, numeric_owner=numeric_owner) 
                        
                    
                    safe_extract(tar_file, temp_directory, members)
            except FileNotFoundError as e:
                logger.error("Could not extract %s" % temp_archive)
                raise e

            member_names = [m.name for m in members]
            for local, remote in files.items():
                if remote in member_names:
                    files[local] = os.path.join(temp_directory, remote)
        # If no archive, then we expect /tmp/{remote_root} to give us the
        # location
        else:
            for local, remote in files.items():
                files[local] = os.path.join('/tmp', 'gssa-transferrer', remote_root, remote)

        # Copy them to where we were asked
        for local, remote in files.items():
            absolute_path = os.path.join(root, local)
            try:
                shutil.move(remote, absolute_path)
            except FileNotFoundError as e:
                logger.error("Could not transfer %s on /tmp to %s - not found" % (remote, absolute_path))
                # raise e

        shutil.rmtree(temp_directory)

    # Send the files back the other way - to /tmp
    def push_files(self, files, root, remote_root):
        for local, remote in files.items():
            absolute_path = os.path.join(root, local)
            remote_absolute_path = os.path.join(remote_root, remote)
            logger.debug("Putting %s %s" % (absolute_path, remote_absolute_path))
            shutil.copy(absolute_path, os.path.join('/tmp', 'gssa-transferrer', remote_absolute_path))

    def configure_from_xml(self, xml):
        for node in xml:
            if node.tag == 'input':
                self._input_archive = node.get('location')
