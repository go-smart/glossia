import pytest
import asyncio.coroutines
import asyncio
import time
import uuid
import traceback
import pdb
from unittest.mock import MagicMock, patch, mock_open
import builtins

from gssa.docker import Submitter

import gssa.comparator


known_guid = str(uuid.uuid4()).upper()
unknown_guid = str(uuid.uuid4()).upper()


def magic_coro():
    mock = MagicMock()
    return mock, asyncio.coroutine(mock)


@asyncio.coroutine
def wait():
    pending = asyncio.Task.all_tasks()

    relevant_tasks = [t for t in pending if ('test_' not in t._coro.__name__)]
    yield from asyncio.gather(*relevant_tasks)


@pytest.fixture(scope="function")
def docker():
    docker = Submitter()
    # ef __init__(self, x, server_id, database, ignore_development=False):
    docker._model_builder = MagicMock()
    return docker

    ####### DOCKER.PY #########


def test_del(monkeypatch, docker):
    docker.finalize = MagicMock()
    docker.__del__()
    docker.finalize.assert_called_with()


def test_set_update_socket(monkeypatch, docker):
    random_socket_location = MagicMock()
    random_socket_location = "tsttmp1"
    docker._socket_location = MagicMock()
    docker._socket_location = 'tsttmp1'
    assert (docker._socket_location == random_socket_location)


def test_copy_output(monkeypatch, docker):
    random_requested = MagicMock()
    random_target = MagicMock()
    docker._output_directory = MagicMock()
    monkeypatch.setattr('os.path.join', lambda tsttmp1, tsttmp2: True)
    monkeypatch.setattr('shutil.copyfile', lambda tsttmp1, tsttmp2: True)
    result = docker.copy_output(random_requested, random_target)
    assert (result == True)


def test_add_input(monkeypatch, docker):
    random_input_file = MagicMock()
    docker._input_files = MagicMock()
    docker.add_input(random_input_file)
    docker._input_files.append.assert_called_with(random_input_file)


def test_output(monkeypatch, docker):
    random_requested = MagicMock()
    docker._output_directory = MagicMock()
    docker._output_directory = 'home/output/'
    random_requested = 'requested/'
    tsttmp_path = 'tsttmp123'
    with patch.object(builtins, 'open', mock_open(read_data=tsttmp_path)):
        result = docker.output(random_requested)
    assert (result == 'tsttmp123')


def test_notify_output(monkeypatch, docker):
    random_filename = MagicMock()
    docker._output_files = MagicMock()
    docker._output_files. append.return_value = True
    result = docker.notify_output(random_filename)
    docker._output_files. append.assert_called_with(random_filename)


def test_send_command(monkeypatch, docker):
    tsttmp1 = MagicMock()
    random_writer = tsttmp1
    random_command = MagicMock()
    random_arguments = MagicMock()
    # json.dumps makes {'command': command, 'arguments': arguments} into
    # a string '{"command": VALUEOFCOMMAND, "arguments": VALUEOFARGUMENTS}'

    # "%s\n" % string gives "VALUEOFSTRING\n"

    # bytes("sddslkfjdl") is the same as b"sddlkfjdl"

    #tsttmp1.write.assert_called_withe (bytes("%s\n" % json.dumps({ 'command': command, 'arguments': arguments }), 'UTF-8'))
    # dafuq am i supposed to do here ???


@pytest.mark.asyncio
def test_destroy(monkeypatch, docker):
    docker.reader = True
    docker.writer = True
    docker.send_command = MagicMock()
    rr1, rr2 = magic_coro()
    docker.receive_response = rr2
    rr1.return_value = True, "Yeah"
    #docker.receive_response    = MagicMock()
    #docker.receive_response.return_value =  True , "Yeah"
    yield from docker.destroy()
    docker.send_command.assert_called_with(docker.writer, 'DESTROY', None)
    rr1.assert_called_with(docker.reader)
    docker.writer = MagicMock()


def test_finalize(monkeypatch, docker):
    docker.reader = True
    tsttmp1 = MagicMock()
    docker.writer = tsttmp1
    docker.finalize()
    #tsttmp1.close.return_value = True
    tsttmp1.close.assert_called_with()
    # I receive the following message:
    # RuntimeError: Task got bad yield: True


@pytest.mark.asyncio
def test_receive_response(monkeypatch, docker):
    random_reader = MagicMock
    rr1, rr2 = magic_coro()
    random_reader.readline = rr2
    rr1.return_value = b'{"success": "blibble", "message": "blobble"}'
    tsttmpmessage = {'success': 'blibble', 'message': 'blobble'}
    #monkeypatch.setattr('json.loads', lambda tsttmpline: tsttmpmessage)
    result = yield from docker.receive_response(random_reader)
    assert (result == ('blibble', 'blobble'))

    # monkeypatch.setattr( 'json.loads'    , lambda 'success' , 'message' : True )
    # This won't work... How am I to generate a message with two variables ?
