import pytest
import asyncio.coroutines
import asyncio
from unittest.mock import MagicMock
import time
import uuid
import traceback
import pdb
import lxml.etree

from gssa.families.mesher_gssf import MesherGSSFMixin

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
def mesher():
    files_required = MagicMock()
    mesher = MesherGSSFMixin()
    mesher._model_builder = MagicMock()
    return mesher

    ######### CONFIG.PY ###########


@pytest.mark.asyncio
def test_mesh(monkeypatch, mesher):
    random_working_directory = MagicMock()
    mesher.to_mesh_xml = MagicMock()
    random_working_directory = 'tsttmp1'
    monkeypatch.setattr('os.path.exists', lambda p3: True)
    monkeypatch.setattr('shutil.copyfile', lambda p4, p5: 'ZZ')
    result = yield from mesher.mesh(random_working_directory)
    yield from wait()
    assert (result is True)


def test_to_mesh_xml(monkeypatch, mesher):
    mesher.get_parameter = MagicMock()
    mesher.get_needle_parameter = MagicMock()
    mesher._needles = MagicMock()
    mesher._regions = {'key1': {
        'format': 'A4', 'input': 'keyboard', 'groups': 'team1', 'meaning': 'organ'}}
    mesher._parameters = {'key2': ('entry1', 'entry2')}
    mesher._mesher_xml = MagicMock()
    mesher._needles = {'key3': {'class': 'class1',
                                'file': 'file1', 'parameters': 'par1'}}
    mesher_mesher_xml = True

    def tsttmp_get_parameter(name):
        if name == "CENTRE_OFFSET":
            return 1000
        elif name == "CENTRE_LOCATION":
            return [111, 222, 333]
        elif name == "SIMULATION_SCALING":
            return 1000
        elif name == "SETTING_SOLID_NEEDLES":
            return True
        elif name == "SETTING_AXISYMMETRIC_INNER":
            return 'tsttmp1'
        elif name == "SETTING_AXISYMMETRIC_INNER_COARSE":
            return 'tsttmp2'
        elif name == "SIMULATION_DOMAIN_RADIUS":
            return True
        elif name == "RESOLUTION_HIGH":
            return True

    def tsttmp_get_needle_parameter(number, name):
        if name == "NEEDLE_TIP_LOCATION":
            return (11, 22, 33)
        elif name == "NEEDLE_ENTRY_LOCATION":
            return (111, 422, 933)

    mesher.get_parameter.side_effect = tsttmp_get_parameter
    mesher.get_needle_parameter.side_effect = tsttmp_get_needle_parameter
    #mesher._regions.items.return_value         = { 'format' : 'A4' , 'input' : 'keyboard' , 'groups' : 'team1' }
    #mesher._parameters.items.return_value      = { 'key1' , 'item1 ', 'item2' }
    #monkeypatch.setattr ( 'lxml.etree.Element'    , lambda p1  : 'q1' )
    #monkeypatch.setattr ( 'lxml.etree.SubElement' , lambda p2  : 'q2' )
    result = mesher.to_mesh_xml()
    xml = b"""<gssf name="elmer_libnuma" version="1.0.2">
  <geometry>
    <needleaxis x="100" y="400" z="900"/>
    <centre x="212.01525445522105" y="626.0610178208842" z="1242.1372900969895"/>
    <simulationscaling ratio="1000"/>
  </geometry>
  <regions>
    <A4 name="key1" input="input/keyboard" groups="t; e; a; m; 1"/>
  </regions>
  <constants>
    <parameter name="key2" value="&quot;entry1&quot;" type="entry2"/>
  </constants>
  <needlelibrary zones="true"/>
  <mesher type="CGAL" zone_boundaries="true">
    <inner type="axisymmetric" template="tsttmp1"/>
    <inner type="axisymmetric" name="coarse" template="tsttmp2"/>
    <extent radius="True"/>
    <centre/>
    <lengthscales nearfield="1.0" farfield="2.0" zonefield="1.0" vessels="far"/>
    <organ region="key1"/>
  </mesher>
  <optimizer/>
  <needles>
    <needle name="1"/>
  </needles>
</gssf>
"""
    assert (lxml.etree.tostring(result, pretty_print=True) == xml)


0
