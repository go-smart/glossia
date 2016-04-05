import pytest
import asyncio.coroutines
import asyncio
import uuid
from unittest.mock import MagicMock, patch, mock_open
import builtins

from gssa.docker import Submitter


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
    docker._model_builder = MagicMock()
    return docker


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
    assert (result is True)


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
    docker.notify_output(random_filename)
    docker._output_files. append.assert_called_with(random_filename)


@pytest.mark.asyncio
def test_destroy(monkeypatch, docker):
    docker.reader = True
    docker.writer = True
    docker.send_command = MagicMock()
    rr1, rr2 = magic_coro()
    docker.receive_response = rr2
    rr1.return_value = True, "Yeah"
    yield from docker.destroy()
    docker.send_command.assert_called_with(docker.writer, 'DESTROY', None)
    rr1.assert_called_with(docker.reader)
    docker.writer = MagicMock()


def test_finalize(monkeypatch, docker):
    docker.reader = True
    tsttmp1 = MagicMock()
    docker.writer = tsttmp1
    docker.finalize()
    tsttmp1.close.assert_called_with()


@pytest.mark.asyncio
def test_receive_response(monkeypatch, docker):
    random_reader = MagicMock()
    rr1, rr2 = magic_coro()
    random_reader.readline = rr2
    rr1.return_value = b'{"success": "blibble", "message": "blobble"}'
    result = yield from docker.receive_response(random_reader)
    assert (result == ('blibble', 'blobble'))
