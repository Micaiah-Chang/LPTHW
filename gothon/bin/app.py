# To Do List:
# Ask Lopen about the bugs
# Currently: improving the unit tests. 

import web
from gothonweb import map,end
from random import randint

urls = (
	'/game', 'GameEngine',
	'/', 'Index',
	'/login', "Login"
)

app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, 
								  initializer={'room':None})
	web.config._session = session
else:
	session = web.config._session


class Index(object):
	def GET(self):
		# this is used to "setup" the session with starting values
		session.room = map.START
		web.seeother("/game")
		
		
class GameEngine(object):

	def GET(self):
		if session.room:
			return render.show_room(room=session.room)
		else:
			# why is this here? do you need it?
			#quip = end.quips[randint(0,len(end.quips)-1)]
			# return render.you_died(quip=quip)
			pass
			#return render.show_room(room=session.room)
		
	def POST(self):
		form = web.input(action=None)
		
		# there is a bug here, can you fix it?
		# if session.room and form.action:
		if session.room != None and form.action != None:
			session.room = session.room.go(form.action)
		else:  
			pass

		
		
		web.seeother("/game")

class LogIn(object):
	def GET(self):
		pass
		
	def POST(self):
		pass
		
if __name__ == "__main__":
	app.run()