from nose.tools import *
from bin.app import app
# Remember to do $env:PYTHONPATH "$env:PYTHONPATH;." 
# in nosetest path or else this will not be read as a module. 
from tools import assert_response

def test_index():
    # check that we get a response on the / URL
    resp = app.request("/")
    assert_response(resp, status="303")
    
    # test our first GET request to /game
    resp = app.request("/game")
    assert_response(resp)
    
    data = {"action": "shoot!"}
    resp = app.request("/game", method="POST", data=data)
    assert_response(resp,status="303")
	# assert_response(resp, status="303", contains="death")
	
	
    # test that we get expected Values
    # data = {'name': 'Zed', 'greet': 'Hola'}
    # resp = app.request("/hello", method="POST", data=data)
    # assert_response(resp, contains="Zed")
    
	