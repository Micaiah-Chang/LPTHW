from nose.tools import *
# import os, sys, inspect
 # # realpath() with make your script run, even if you symlink it :)
# cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
# if cmd_folder not in sys.path:
	# sys.path.insert(0, cmd_folder)

	import sys
sys.path.append('bin')
from app import app
# Above is hacky way to get python to recogize app as a module
from tools import assert_response

def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status = "404")
    
    # test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)
    
    # make sure default values work for the form
    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="Nobody")
    
    # test that we get expected Values
    data = {'name': 'Zed', 'greet': 'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Zed")
    