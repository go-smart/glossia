import pytest
import asyncio.coroutines
import asyncio
from unittest.mock import MagicMock
import time
import uuid
import traceback
import pdb

from gssa.translator import GoSmartSimulationTranslator

import gssa.comparator
import lxml.etree

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
def translator():
    translator = GoSmartSimulationTranslator ( )
    translator._model_builder   = MagicMock()
    return translator 



    ###############################
    ####### TRANSLATOR.PY #########    
    ###############################   
     
#   def __init__(self):
#       self._files_required = {}     
#       nothing to test here I guess...
     
def test_get_files_required ( monkeypatch , translator ) :  
    translator._files_required = MagicMock()
    translator._files_required = 'panos555'
    result = translator.get_files_required ()
    assert ( result == 'panos555' )


#no orange
def test_translate ( monkeypatch , translator ) :  



    random_xml = lxml.etree.fromstring ("""
<gssa>
    <algorithms>
        <algorithm result='RESULT'>
            <arguments>
                <argument name='fiz' />
                <argument name='bob' />
            </arguments>
            <content>slkjdflkajs</content>
        </algorithm>
    </algorithms>
    <parameters>
    </parameters>
    <numericalModel>
        <definition family='lighthouse'>
        </definition>
    </numericalModel>
</gssa>    
""")

    result = translator.translate ( random_xml )
    numerical_model = random_xml.find('numericalModel')

    assert ( result == ( 'lighthouse', numerical_model, {}, {'RESULT':{'arguments': ['fiz', 'bob'], 'content': 'slkjdflkajs'}} ) )
    
