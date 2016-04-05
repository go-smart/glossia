import pytest
import asyncio.coroutines
import asyncio
from unittest.mock import MagicMock , call
import time
import uuid
import traceback
import pdb

from gssa.client import GoSmartSimulationClientComponent

import gssa.comparator


known_guid   = str(uuid.uuid4()).upper()
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
def client(monkeypatch):
    panos_x                 = MagicMock()
    panos_gssa_file         = MagicMock()
    panos_subdirectory      = MagicMock()
    panos_output_files      = MagicMock()
    panos_tmp_transferrer   = MagicMock()
    panos_input_files       = MagicMock()
    panos_definition_files  = MagicMock()
    panos_skip_clean        = MagicMock()
    panos_server            = MagicMock()
    monkeypatch.setattr( 'lxml.etree.parse' , lambda panos1 : 'panos2' )
    client = GoSmartSimulationClientComponent ( panos_x , 'panos_gssa_file' , panos_subdirectory , panos_output_files )
    #    def __init__(self, x, gssa_file, subdirectory, output_files, tmp_transferrer='/tmp', input_files=None, definition_files=None, skip_clean=False, server=None):
    client._model_builder   = MagicMock()
    return client 



    ###########################
    ####### CLIENT.PY #########    
    ###########################    

def test_make_call  ( monkeypatch , client ) :  
    random_suffix = MagicMock()
    client.server = MagicMock()
    client.server = True
    random_suffix = 'panos_suffix'
    result = client.make_call ( random_suffix )
    assert ( result == "com.gosmartsimulation.panos_suffix"  )
    


@pytest.mark.asyncio  
def test_onJoin ( monkeypatch , client ) : 
    random_details          = MagicMock()
    random_call             = MagicMock()
    client.make_call        = MagicMock()
    client._subdirectory    = MagicMock()
    client.subscribe        = MagicMock()
    client.onComplete       = MagicMock()
    client.onFail           = MagicMock()
    client._guid            = known_guid   
    client._subdirectory    = 'ooo' 
    client.onComplete       = 'aaa'
    client.onFail           = 'www'
    client.make_call.return_value = 'hello'
    monkeypatch.setattr( 'lxml.etree.tostring' , lambda panos1 , encoding : "unicode" )
    call1 , call2           = magic_coro()
    client.call             = call2
    yield from client.onJoin ( random_details )
    yield from wait()
    panos_calls_a = [
        call('hello' , known_guid ) ,
        call('hello' , known_guid , "unicode" ) ,
        call('hello' , known_guid , 'ooo' ) ,
        call('hello' , known_guid ) ]
    call1.assert_has_calls ( panos_calls_a )
    panos_calls_b = [     
        call ( 'aaa' , 'hello' ) ,
        call ( 'www' , 'hello' ) ]
    client.subscribe.assert_has_calls (   panos_calls_b )
    


@pytest.mark.asyncio  
def test_onComplete ( monkeypatch , client ) : 
    random_guid             = known_guid
    random_success          = MagicMock()
    random_directory        = MagicMock()
    random_time             = MagicMock()
    random_validation       = MagicMock()
    call1 , call2           = magic_coro()
    client.call             = call2
    call1.return_value      = 'panosfiles'
    client.make_call        = MagicMock()
    client._output_files    = MagicMock()
    fin1 , fin2             = magic_coro()
    client.finalize         = fin2
    random_validation       = False
    client.make_call.return_value = 'aaa'
    fin1.return_value  = 'ooo'  
    monkeypatch.setattr( 'os.path.join' , lambda pan1 , pan2 : True )
    client.onComplete( random_guid, random_success, random_directory, random_time, random_validation )
    yield from wait() 
    call1.assert_called_with ( 'aaa' , random_guid , { } )
    fin1.assert_called_with ( random_guid )
        


#@pytest.mark.asyncio  
#def test_onStatus ( monkeypatch , client ) :     
    #random_guid             = known_guid
    #random_message          = MagicMock()
    #random_directory        = MagicMock()
    #random_time             = MagicMock()
    #random_validation       = MagicMock()
    #random_message          = { 0.3 , True } 
    ## hm.... nothing to test here...



@pytest.mark.asyncio  
def test_onFail ( monkeypatch , client ) :   
    random_guid             = known_guid
    random_message          = MagicMock()
    random_directory        = MagicMock()
    random_time             = MagicMock()
    random_validation       = MagicMock()
    fin1 , fin2             = magic_coro()
    client.finalize         = fin2
    result = client.onFail( random_guid, random_message, random_directory, random_time, random_validation )
    yield from wait() 
    fin1.assert_called_with ( random_guid ) 
    
    
@pytest.mark.asyncio  
def test_finalize ( monkeypatch , client ) :   
    random_guid             = known_guid
    client._skip_clean      = MagicMock()
    call1 , call2           = magic_coro()
    client.call             = call2
    client.shutdown         = MagicMock()
    client._skip_clean      = False
    client.make_call        = MagicMock()
    client.make_call.return_value = 'aaa'
    yield from client.finalize  ( random_guid    ) 
    yield from wait()
    call1.assert_called_with ( 'aaa' , random_guid ) 
    client.shutdown.assert_called_with ()

     
def test_shutdown ( monkeypatch , client ) :   
    client.leave = MagicMock()
    client.shutdown()
    client.leave.assert_called_with ()

@pytest.mark.asyncio  
def test_onLeave ( monkeypatch , client ) :
    random_details      = MagicMock()
    client.disconnect   = MagicMock()
    client.onLeave ( random_details )
    yield from wait()
    client.disconnect.assert_called_with (  )












    
