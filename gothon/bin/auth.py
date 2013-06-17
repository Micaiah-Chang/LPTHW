import web
import re
import base64
import passlib
import sqlite3
from bin.passwords import *

urls = (
	'/', 'Index',
	'/login', 'Login',
	'/signup', "SignUp"
)

app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")

allowed = (
	('jon', 'password1'),
	('tom', 'pass2'),
	('newbie', "password")
)

# Passwords already stored on the database. 
# Need to hash them into it. 


class Index(object):
    def GET(self):
        if web.ctx.env.get('HTTP_AUTHORIZATION') is not None:
            return 'This is the index page'
        else:
            raise web.seeother('/login')
			
class Login(object):
    def GET(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        authreq = False
        if auth is None:
            authreq = True
        else:
            auth = re.sub('^Basic ','',auth)
            username,password = base64.decodestring(auth).split(':')
            if (username,password) in allowed:
                raise web.seeother('/')
            else:
                authreq = True
        if authreq:
            web.header('WWW-Authenticate','Basic realm="Auth example"')
            web.ctx.status = '401 Unauthorized'
            return
			
class SignUp(object):
	def GET(self):
		return render.signup()
		
	def POST(self):
		"""Should take some user's signup information and pass it to allowed """
		form = web.input()
		
		authdb = web.database(dbn='')
		pwdhash = hashlib.sha512(form.password).hexdigest()
		cursor = authdb.cursor()
		cursor.execute("")
			
if __name__ == '__main__':
	app.run()