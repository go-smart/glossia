import builtins
import pytest
import asyncio.coroutines
import asyncio
from unittest.mock import MagicMock, patch, mock_open
import time
import uuid
import traceback
import pdb

import gssa.config

import gssa.comparator
import lxml.etree

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

    ###############################
    ######### CONFIG.PY ###########
    ###############################


def test_init_config(monkeypatch):
    random_config_file = MagicMock()
    random_config_file = None
    yaml_example = """
    thing:
        - thing1
        - thing2
        - thing3
    """
    expected_config = {'thing': ['thing1', 'thing2', 'thing3']}
    # real config is gssa.config.__config

    # (and add import builtins at top)
    # with patch.object(builtins, 'open', mock_open(read_data=CONTENTOFFILE)):

    with patch.object(builtins, 'open', mock_open(read_data=yaml_example)):
        result = gssa.config.init_config(random_config_file)

    assert (expected_config == gssa.config.__config)


def test_get(monkeypatch):
    random_key = MagicMock()
    random_default = MagicMock()
