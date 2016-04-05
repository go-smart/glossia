import pytest
import asyncio.coroutines
import asyncio
from unittest.mock import MagicMock
import time
import uuid
import traceback
import pdb

from gssa.session import GoSmartSimulationServerSession

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
def session(monkeypatch):
    tsttmp_database = MagicMock()
    monkeypatch.setattr( 'gssa.server.GoSmartSimulationServerComponent' , MagicMock )
    session = GoSmartSimulationServerSession ( known_guid , "tsttmp_server_id" , tsttmp_database , False )
    #ef __init__(self, x, server_id, database, ignore_development=False):
    session._model_builder = MagicMock()
    return session 



    ############################
    ####### SESSION.PY #########    
    ############################    




@pytest.mark.asyncio        
def test_doSearch    ( monkeypatch , session ) :  
    random_guid = known_guid
    session._component = MagicMock()
    session._component.doSearch.return_value = 1555
    result = yield from session.doSearch ( known_guid , limit = None )
    assert ( result == 1555 )
    
    
    


@pytest.mark.asyncio    
def test_doInit    ( monkeypatch , session ) :  
    random_guid = known_guid
    session._component = MagicMock()
    session._component.doInit.return_value = 1555    
    result = yield from session.doInit ( known_guid  )
    assert ( result == 1555 )




#@pytest.mark.asyncio    
#def test_doApi    ( monkeypatch , session ) :  
    #session._component = MagicMock()
    #session._component.doApi.return_value = 1555    
    #result = yield from session.doApi (  )
    #assert ( result == 1555 )




@pytest.mark.asyncio    
def test_doClean    ( monkeypatch , session ) :  
    random_guid = known_guid
    session._component = MagicMock()
    session._component.doClean.return_value = 1555    
    result = yield from session.doClean ( random_guid )
    assert ( result == 1555 )



@pytest.mark.asyncio    
def test_doStart    ( monkeypatch , session ) :  
    random_guid = known_guid
    session._component = MagicMock()
    session._component.doStart.return_value = 1555    
    result = yield from session.doStart ( random_guid )
    assert ( result == 1555 )




@pytest.mark.asyncio    
def test_doTmpValidation    ( monkeypatch , session ) :  
    random_guid = known_guid
    random_directory = MagicMock()
    session._component = MagicMock()
    session._component.doTmpValidation.return_value = 1555    
    result = yield from session.doTmpValidation ( random_guid , random_directory )
    assert ( result == 1555 )

  

@pytest.mark.asyncio    
def test_doUpdateFiles    ( monkeypatch , session ) :  
    random_guid = known_guid
    random_files = MagicMock()
    session._component = MagicMock()
    session._component.doUpdateFiles.return_value = 1555    
    result = yield from session.doUpdateFiles ( random_guid , random_files )
    assert ( result == 1555 )




@pytest.mark.asyncio    
def test_doRequestFiles    ( monkeypatch , session ) :  
    random_guid = known_guid
    random_files = MagicMock()
    session._component = MagicMock()
    session._component.doRequestFiles.return_value = 1555    
    result = yield from session.doRequestFiles ( random_guid , random_files )
    assert ( result == 1555 )







0    
