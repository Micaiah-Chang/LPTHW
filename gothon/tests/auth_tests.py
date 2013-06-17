from nose.tools import *
from bin.auth import app
from tools import assert_response 

def test_logins():
	resp = app.request('/login')
	assert_response(resp, status='401 Unauthorized')
	# Shouldn't authorize when there's no login!
	
	# Check should authorize when there is though you silly goose.
	data = {'username': 'jon','password': 'password1'}
	resp = app.request('/login', method="POST", data=data)
	
	#assert_response(resp,  status='200')
	
def test_signup():
	pass
