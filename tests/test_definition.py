import pytest
import asyncio.coroutines
import asyncio
from unittest.mock import MagicMock
import time
import uuid
import traceback
import pdb

from gssa.definition import GoSmartSimulationDefinition

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
def definition():
    definition = GoSmartSimulationDefinition(
        known_guid, "tsttmp_xml_string", "tsttmp_home_dir", "tsttmp_translator", True)
    # def __init__(self, guid, xml_string, tmpdir, translator,
    # finalized=False, ignore_development=False, update_status_callback=None):
    definition._model_builder = MagicMock()
    return definition


####### DEFINITION STARTS HERE #######


#@pytest.mark.asyncio


def test_definition_3tests(monkeypatch, definition):
    random_dir = MagicMock()
    definition._remote_dir = MagicMock()
    definition._remote_dir = 123
    definition._guid = MagicMock()
    definition._guid = 234

    result1 = definition.get_remote_dir()
    assert (result1 == 123)

    definition.set_remote_dir(random_dir)
    assert (definition._remote_dir == random_dir)

    result3 = definition.get_guid()
    assert (result3 == 234)


def test_create_xml_from_string(monkeypatch, definition):
    random_xml = "STRING"
    monkeypatch.setattr('lxml.etree.fromstring', lambda tsttmp83: 'tsttmp1111')
    definition._finalized = False
    result = definition.create_xml_from_string(random_xml)
    assert (result is True)


def test_definition_2tests(monkeypatch, definition):
    random_files = MagicMock()
    definition._files = MagicMock()
    # files is a dictrionary, so the .update part is skipped
    definition.update_files(random_files)
    definition._files.update.assert_called_wth(random_files)

    result = definition.get_files()
    assert(result == definition._files)


def test_finalize(monkeypatch, definition):
    definition._xml = MagicMock()
    definition._transferrer = MagicMock()
    definition._translator = MagicMock()
    definition._ignore_development = MagicMock()
    definition._shadowing = MagicMock()
    definition._model_builder = MagicMock()
    definition._transferrer = MagicMock()
    definition._files = MagicMock()
    tsttmp_cls = MagicMock()
    tsttmp_fam333 = MagicMock()
    tsttmp_model = MagicMock()
    tsttmp_find = MagicMock()
    tsttmp_param = MagicMock()
    tsttmp_register = MagicMock()
    tsttmp_verifyer = MagicMock()
    tsttmp_families = MagicMock()
    tsttmp_register = {'eee': tsttmp_cls}
    tsttmp_families = {'aaa': tsttmp_fam333}
    tsttmp_param = {'DEVELOPMENT': True}
    #definition._xml                = True
    definition._ignore_development = True
    definition._xml.find.return_value = tsttmp_find
    definition._translator.translate.return_value = (
        'aaa', 'bbb', tsttmp_param, 'ddd')
    tsttmp_find.get.return_value = 'eee'
    tsttmp_fam333.return_value = tsttmp_model
    tsttmp_model.load_definition.return_value = 'vvvvvvvvv'
    monkeypatch.setattr(
        'gssa.transferrer.transferrer_register', tsttmp_register)
    monkeypatch.setattr('zope.interface.verify',
                        lambda p1, p2: tsttmp_verifyer)
    monkeypatch.setattr('gssa.family.register', tsttmp_families)
    result = definition.finalize()
    assert (result is True)


@pytest.mark.asyncio
def test_definition_3more(monkeypatch, definition):
    definition._finalized = MagicMock()
    definition._finalized = 'tsttmp1'
    result1 = definition.finalized()
    assert (result1 == 'tsttmp1')

    definition._dir = MagicMock()
    definition._dir = 'tsttmp2'
    result2 = definition.get_dir()
    assert (result2 == 'tsttmp2')

    definition._dir = MagicMock()
    random_definition, random_coroutine = magic_coro()
    definition._model_builder.clean = random_coroutine
    monkeypatch.setattr('shutil.rmtree', lambda tsttmp44: 'tsttmp4')
    result3 = yield from definition.clean()
    assert (result3 is True)


def test_gather_results(monkeypatch, definition):
    definition.get_dir = MagicMock()
    definition.get_dir.return_value = 'tsttmp000'
    definition._gather_files = MagicMock()
    definition._gather_files.return_value = 156
    result = definition.gather_results()
    definition._gather_files.assert_called_wth('results_archive.tgz',
                                               {'output': 'tsttmp000/output',
                                                'output.final': 'tsttmp000/output.final',
                                                'original.xml': 'tsttmp000/original.xml',
                                                'guid': 'tsttmp000/guid'})
    assert (result == 156)


def test_gather_diagnostics(monkeypatch, definition):
    definition.get_dir = MagicMock()
    definition.get_dir.return_value = 'tsttmp000'
    definition._gather_files = MagicMock()
    definition._gather_files.return_value = 156
    result = definition.gather_diagnostic()
    definition._gather_files.assert_called_wth('results_archive.tgz',
                                               {'input': 'tsttmp000/output',
                                                'input.final': 'tsttmp000/output.final',
                                                'logs': 'tsttmp000/logs',
                                                'original.xml': 'tsttmp000/original.xml',
                                                'guid': 'tsttmp000/guid'})
    assert (result == 156)


def test_gather_files(monkeypatch, definition):
    random_archive_name = MagicMock()
    definition.get_dir = MagicMock()
    random_files = MagicMock()
    definition.guid = MagicMock()
    monkeypatch.setattr('os.path.join', lambda tsttmp1, tsttmp2: True)
    monkeypatch.setattr('tarfile.open', lambda archive, mode: 'w:gz')
    #result = definition._gather_files ( random_archive_name , random_files )
    #assert ( result == 4233 )


def test_push_files(monkeypatch, definition):
    definition._shadowing = False
    definition._transferrer = MagicMock()
    definition.get_dir = MagicMock()
    uploaded_files = MagicMock()
    files = MagicMock(spec=dict)
    definition._transferrer.push_files.return_value = uploaded_files
    files.items.return_value = (('local', 'remote'),)
    monkeypatch.setattr('os.path.join', lambda tsttmp1, tsttmp2: True)
    monkeypatch.setattr('os.path.exists', lambda tsttmp3: True)
    result = definition.push_files(files, transferrer=None)
    assert (result == {'local': 'remote'})


@pytest.mark.asyncio
def test_simulate(monkeypatch, definition):
    definition._shadowing = False
    definition.get_dir = MagicMock()
    monkeypatch.setattr('os.path.exists', lambda tsttmp888: True)
    definition.get_dir.return_value = 'tsttmp000'
    random_definition, random_coroutine = magic_coro()
    definition._model_builder.simulate = random_coroutine
    random_definition.return_value = 'tsttmp13'
    result = yield from definition.simulate()
    assert (result == 'tsttmp13')
    # when I make a magic coroutine like :
    # a , b =     magic_coro()
    # then I have the annoying function = b
    # and set a.return_value =


@pytest.mark.asyncio
def test_validation(monkeypatch, definition):
    definition._shadowing = False
    random_definition, random_coroutine = magic_coro()
    definition._model_builder.validation = random_coroutine
    random_definition.return_value = 'tsttmp13'
    result = yield from definition.validation()
    assert (result == 'tsttmp13')
