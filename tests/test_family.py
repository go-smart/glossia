import pytest
import asyncio.coroutines
import asyncio
from unittest.mock import MagicMock
import time
import uuid
import traceback
import pdb

from gssa.family import Family

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


@pytest.fixture(scope="function")
def family():
    FamilyType = MagicMock()
    family = Family()
    family._model_builder = MagicMock()
    return family

    ######### FAMILY.PY ###########


def test_get_needle_parameter(monkeypatch, family):
    random_needle_index = MagicMock()
    random_key = MagicMock()
    random_try_json = MagicMock()
    random_try_json = True
    family._needles = MagicMock()
    family._needle_order = MagicMock()
    family.get_parameter = MagicMock()
    random_needle_index = 'a'
    family._needles = {'b': {'parameters': 'd'}}
    family._needle_order = {'a': 'b'}
    family.get_parameter.return_value = 666
    result = family.get_needle_parameter(
        random_needle_index, random_key, random_try_json)
    assert (result == 666)


def test_get_parameter(monkeypatch, family):

    random_key = MagicMock()
    random_try_json = MagicMock()
    random_parameters = MagicMock()
    family._parameters = MagicMock()
    random_key = 'a'
    random_try_json = True
    random_parameters = None
    family._parameters = {'a': {'b', 'c'}}
    monkeypatch.setattr('gssa.parameters.convert_parameter',
                        lambda p1, p2, p3: True)
    result = family.get_parameter(
        random_key, random_try_json, random_parameters)
    assert (result is True)


@pytest.mark.asyncio
def test_validation(monkeypatch, family):
    random_working_directory = MagicMock()
    random_working_directory = None
    result = yield from family.validation(random_working_directory)
    yield from wait()
    assert (result is None)


def test_load_core_definition(monkeypatch, family):
    family._needles = MagicMock()
    family._regions = MagicMock()
    family._regions_by_meaning = MagicMock()
    family._files_required = MagicMock()
    monkeypatch.setattr('os.path.splitext', lambda tsttmp1, tsttmp2: True)
    random_xml = lxml.etree.fromstring ("""
    <gssa>
        <needles>
            <needle file='surface:tsttmp.txt' index = 'tsttmp333' > 
            </needle>
        </needles>
        <regions>
        </regions>
    </gssa>    
    """)

0
