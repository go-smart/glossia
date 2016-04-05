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
