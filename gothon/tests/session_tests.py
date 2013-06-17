from nose.tools import * 
from bin.auth import *
from tools import assert_response

def test_index():
	resp = app.request('/')
	assert_response(resp, status='303')
	
	resp = app.request('/login')
	assert_response(resp, status = '401')
	
	