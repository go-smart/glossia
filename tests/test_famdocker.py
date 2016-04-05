import pytest
import asyncio.coroutines
import asyncio
from unittest.mock import MagicMock
import time
import uuid
import traceback
import pdb
import lxml.etree
import builtins
from unittest.mock import MagicMock, patch, mock_open

from gssa.family import Family
from gssa.families.docker import DockerFamily
from gssa.docker import Submitter
from gssa.families.elmer_libnuma import ElmerLibNumaFamily
import gssa.parameters

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
def famdocker():
    files_required = MagicMock()
    famdocker = DockerFamily(files_required)
    famdocker._model_builder = MagicMock()
    return famdocker

    ###############################
    ######### LEGACY.PY ###########
    ###############################


#   def init has nothing to test ...


def test_get_needle_parameter(monkeypatch, famdocker):
    random_needle_index = MagicMock()
    random_key = MagicMock()
    random_try_json = MagicMock()
    famdocker._needles = MagicMock()
    famdocker._needle_order = MagicMock()
    famdocker.get_parameter = MagicMock()
    random_needle_index = 'index1'
    famdocker._needle_order = {'index1': 'p1'}
    random_try_json = True
    random_key = 'key1'
    famdocker.get_parameter.return_value = 123456
    result = famdocker.get_needle_parameter(
        random_needle_index, random_key, random_try_json)
    assert (result == 123456)


def test_get_parameter(monkeypatch, famdocker):
    random_key = MagicMock()
    random_try_json = MagicMock()
    random_parameters = MagicMock()
    famdocker._parameters = MagicMock()
    random_parameters = None
    random_try_json = True
    random_key = 'key1'
    famdocker._parameters = {'key1': {'par1', 'par2'}}
    monkeypatch.setattr('gssa.parameters.convert_parameter',
                        lambda p1, p2, p3: 123456)
    result = famdocker.get_parameter(
        random_key, random_try_json, random_parameters)


@pytest.mark.asyncio
def test_prepare_simulation(monkeypatch, famdocker):
    random_working_directory = MagicMock()
    result = yield from famdocker.prepare_simulation(random_working_directory)
    assert (result is True)


def test_get_percentage_socket(monkeypatch, famdocker):
    random_working_directory = MagicMock()
    random_working_directory = 'dir1'
    result = famdocker.get_percentage_socket_location(random_working_directory)
    assert (result == 'dir1/update.sock')


@pytest.mark.asyncio
def test_clean(monkeypatch, famdocker):
    famdocker._submitter = MagicMock()
    famdocker._submitter.destroy.return_value = {}
    famdocker._submitter.finalize.return_value = 333
    yield from famdocker.clean()
    famdocker._submitter.destroy.assert_called_with()
    famdocker._submitter.finalize.assert_called_with()


def test_load_definition(monkeypatch, famdocker):
    random_xml = MagicMock()
    random_parameters = MagicMock()
    random_algorithms = MagicMock()
    famdocker.load_core_definition = MagicMock()
    famdocker.load_definition(random_xml, random_parameters, random_algorithms)
    famdocker.load_core_definition.assert_called_with(
        random_xml, random_parameters, random_algorithms)


def test_retrieve_files(monkeypatch, famdocker):
    random_destination = MagicMock()
    famdocker._retrievable_files = MagicMock()
    famdocker._retrievable_files = {'file1', 'file2', 'file3'}
    random_destination = 'destination1'
    famdocker.retrieve_files(random_destination)
    # hmmm .... nothing to assert here...
