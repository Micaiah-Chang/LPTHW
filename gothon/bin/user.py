import hashlib
import web

# TODO: Figure out what a cryptographically secure way of generating
# salts would be. 


def POST(self):
	i = web.input()
	
	authdb = sqlite3.connect('users.db')
	pwdhash = hashlib.sha512(i.password).hexdigest()
	check = authdb.execute('select * from users where username=? and password=?')
	if check:
		session.loggedin = True
		session.username = i.username
		raise web.seeother('/results')
		
	else: return render.base("Those login details don't work.")