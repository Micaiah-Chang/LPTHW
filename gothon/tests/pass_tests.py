from nose.tools import *
from bin.passwords import *

def test_password():
	password = "password"
	hash = encrypt_this(password)
#	assert_equal(hash,encrypt_this(password)
	assert_equal(verify_this(password,hash), True)
	
def test_login():
	password = "password"
	hash = encrypt_this(password)
	login = ('username', hash)
	