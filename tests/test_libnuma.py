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
from gssa.families.elmer_libnuma import ElmerLibNumaFamily

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
def libnuma():
    files_required = MagicMock()
    libnuma = ElmerLibNumaFamily(files_required)
    libnuma._model_builder = MagicMock()
    return libnuma

    ######### LEGACY.PY ###########


#   def init has nothing to test ...


def test_get_percentage_socket_location(monkeypatch, libnuma):
    random_working_directory = MagicMock()
    random_working_directory = 'homedir'
    result = libnuma.get_percentage_socket_location(random_working_directory)
    assert (result == 'homedir/update.sock')


def test_get_needle_parameter(monkeypatch, libnuma):
    random_needle_index = MagicMock()
    random_key = MagicMock()
    random_try_json = MagicMock()
    libnuma._needles = MagicMock()
    libnuma._needle_order = MagicMock()
    libnuma.get_parameter = MagicMock()
    libnuma._needle_order = {'random_needle_index': {'parameters': 'index1'}}
    random_try_json = True
    libnuma.get_parameter.return_value = 123456
    result = libnuma.get_needle_parameter(
        random_needle_index, random_key, random_try_json)
    assert (result == 123456)


def test_get_parameter(monkeypatch, libnuma):
    random_key = MagicMock()
    random_try_json = MagicMock()
    random_parameters = MagicMock()
    libnuma._parameters = MagicMock()
    random_try_json = True
    random_parameters = None
    random_key = 'key0'
    libnuma._parameters = {'key0': ('key1', 'key2')}
    monkeypatch.setattr('gssa.parameters.convert_parameter',
                        lambda p1, p2, p3: 123456)
    result = libnuma.get_parameter(
        random_key, random_try_json, random_parameters)
    assert (result == 'key1')


@pytest.mark.asyncio
def test_prepare_simulation(monkeypatch, libnuma):
    random_working_directory = MagicMock()
    libnuma.to_xml = MagicMock()
    libnuma.to_xml.return_value = MagicMock()
    tsttmp_xml = """
    <validation_struct>   
    </validation_struct>
    """
    with patch.object(builtins, 'open', mock_open(read_data=tsttmp_xml)):
        result = yield from libnuma.validation(random_working_directory)
    assert (result == '{}')


@pytest.mark.asyncio
def test_validation(monkeypatch, libnuma):
    random_working_directory = MagicMock()
    random_working_directory = False
    libnuma._simulation_directory = MagicMock()
    libnuma._simulation_directory = 'homedir'
    monkeypatch.setattr('os.path.exists', lambda p1: True)
    tsttmp_xml = """
    <validation_struct>   
    </validation_struct>
    """
    with patch.object(builtins, 'open', mock_open(read_data=tsttmp_xml)):
        result = yield from libnuma.validation(random_working_directory)
    assert (result == '{}')


def test_to_xml(monkeypatch, libnuma):

    etree1 = MagicMock()
    regions1 = MagicMock()
    argument1 = MagicMock()
    content1 = MagicMock()
    algorithms1 = MagicMock()
    file1 = MagicMock()
    extrapolated1 = MagicMock()
    root1 = MagicMock()
    modules1 = MagicMock()
    definition1 = MagicMock()
    libnuma._algorithms = MagicMock()
    libnuma.to_mesh_xml = MagicMock()
    libnuma._definition = MagicMock()
    libnuma._needles = MagicMock(spect=dict)
    libnuma.get_parameter = MagicMock()
    libnuma.get_needle_parameter = MagicMock()
    libnuma._disallowed_functions = MagicMock()
    libnuma._regions = MagicMock()
    q1, q2, q3 = MagicMock(),   MagicMock(),  MagicMock()

    definition1 = 'definition00000'
    content1 = 'content00000000'
    file1 = 'library:straight tines'
    modules1 = ['p1', 'p2', 'p3']
    libnuma._definition = definition1
    extrapolated1 = True
    q1, q2, q3 = ['x1', 'y1', 'z1'], ['x2', 'y2', 'z2'], ['x3', 'y3', 'z3']
    libnuma._algorithms = {'first_definition': {
        'arguments': argument1, 'content': content1}}
    regions1 = {"groups": "segmented-lesions"}
    root1 = lxml.etree.Element('test')
    libnuma._needles = {'first_needle': {
        'class': 'point-sources', 'file': file1}}
    libnuma._regions = {'first_regiom': {'groups': 'group1'}}

    libnuma.to_mesh_xml.return_value = root1
    #libnuma._needles.items.return_value          = { 'class' : 'point-sources' , 'file' : file1 }

    def tsttmp_get_parameter(name, irrelevant=False):
        if name == 'ELMER_NUMA_MODULES':
            return modules1
        elif name == 'SETTING_LESION_FIELD':
            return 'DEAD'
        elif name == 'CONSTANT_NEEDLE_EXTENSIONS':
            return [1, 2, 3, 4, 5]
    libnuma.get_needle_parameter.return_value = [q1, q2, q3]
    libnuma.get_parameter.side_effect = tsttmp_get_parameter

    #libnuma._algorithms.items.return_value       = algorithms1
    #libnuma._regions.items.return_value          = regions1

    #monkeypatch.setattr( 'lxml.etree.SubElement' , lambda p1 , p2 : etree1 )

    expected_xml = """
<test>
  <elmer>
    <variant modules="p1; p2; p3">definition00000
{{ p.SOURCES }}
</variant>
    <pointsources system="extrapolated">
      <extensions>
        <extension phase="0" length="1"/>
        <extension phase="1" length="2"/>
        <extension phase="2" length="3"/>
        <extension phase="3" length="4"/>
        <extension phase="4" length="5"/>
      </extensions>
      <points>
        <point i="0" x="x1" y="y1" z="z1"/>
        <point i="1" x="x2" y="y2" z="z2"/>
        <point i="2" x="x3" y="y3" z="z3"/>
      </points>
    </pointsources>
    <algorithms>
      <algorithm result="first_definition" arguments="">
        <arguments/>
        <content>content00000000</content>
      </algorithm>
    </algorithms>
  </elmer>
  <lesion field="DEAD"/>
</test>
    """.strip()
    result = libnuma.to_xml()
    assert (lxml.etree.tostring(
        result, pretty_print=True).decode().strip() == expected_xml)

    # so far :
    # root      = root1 =  MagicMock()
    # sidf.text = definition1 = MagicMock()
    # modules   = modules1 = [ 'p1' , 'p2' , 'p3' ]
    # ix , needle =  { 'class' : 'point-sources' , 'file' = file1 } ,
    # file1 = ('library' , 'straight tines' , )
    # location = needle['file'] = ('library' , 'straight tines' , )
    # prong_locations = [ q1 , q2 , q3 ] = [ 'x1' , 'y1' , 'z1' ] , [ 'x2' , 'y2' , 'z2' ] , [ 'x3' , 'y3' , 'z3' ]
    # extension_lengths = modules1 = [ 'p1' , 'p2' , 'p3' ]
    # phase, extension = 1 , 2 , 3 *AND*  [ 'p1' , 'p2' , 'p3' ]
    # i, location = 1 , 2 , 3 *AND* [ 'x1' , 'y1' , 'z1' ] , [ 'x2' , 'y2' , 'z2' ] , [ 'x3' , 'y3' , 'z3' ]
    # c, x = ('x', 'y', 'z')  *ZIP* location ^
    # result, definition =  { 'arguments' : argument1 , 'content' : content1 }
    # threshold_upper = modules1 =  [ 'p1' , 'p2' , 'p3' ]

    # point_sources = lxml.etree.SubElement(elmer, "pointsources")
    # extensions = lxml.etree.SubElement(point_sources, "extensions")
    # extension_node = lxml.etree.SubElement(extensions, "extension")
    # point = lxml.etree.SubElement(points, "point")
    # algorithms = lxml.etree.SubElement(elmer, 'algorithms')
    # algorithm = lxml.etree.SubElement(algorithms, "algorithm")
    # arguments = lxml.etree.SubElement(algorithm, "arguments")
    # lesion = lxml.etree.SubElement(root, 'lesion')
    # validation = lxml.etree.SubElement(root, 'validation')

# def retrieve_files has nothing to test


0
