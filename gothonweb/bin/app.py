import web
import os

urls = (
    '/hello', 'Index',
	'/backend', 'Backend',
	'/upload', 'Upload',
	'/uploaded', 'Uploaded',
	'/start', 'Start',
	'/error', 'PlaceHolder',
	'/count', 'Count',
	'/reset', 'Reset'
)

app = web.application(urls, globals())
# Sends the urls as globals to web app.

render = web.template.render('templates/', base="layout")
# Applies a default layout so that I don't have to do the boilerplate stuffs

web.config.debug = False

if web.config.get('_session') is None:
	session = web.session.Session(app, web.session.DiskStore('sessions'), {'count': 0})
	web.config._session = session
else: 
	session = web.config._session

class Count(object):
	def GET(self):
		print 'session', session
		session.count += 1
		return "It's your" + str(session.count) + "time here!"

class Reset(object):
	def GET(self):
		session.kill()
		return ""
		
		
class Index(object):
	'''Form page, sends person to a greeting '''
	def GET(self):
		return render.hello_form()
    
	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)

		
class Upload(object):
	def GET(self):
		return render.upload()
		
	def POST(self):
		x = web.input(myfile={})
		name = web.debug(x['myfile'].filename) # This is the filename
		web.debug(x['myfile'].value) # This is the file contents
		web.debug(x['myfile'].file.read()) # Or use a filline object
		form = web.input(contents=None)
		return render.uploaded(name = str(name), contents = form.contents) 		
		# raise web.seeother('/upload')
	
	
class images(object):
	'''Essentially copied from the web.py page on how to upload images'''
	def GET(self,name):
		ext = name.split(".")[-1] # Gather Extension
		
		
		cTYPE = {
			"png": "images/png",
			"jpg": "images/jpeg",
			"gif": "images/gif",
			"ico": "images/x-con"
		}
		
		if name in os.listdir('images'): #Security
			web.header("Content-Type", cType(ext)) #set the Header
			return open('images/%s' %name, "rb"),read() #rb is for reading images.
			
		else:
			raise web.notfound()

class Start(object):
	'''Where we start the game'''
	def GET(self):
		return render.start()
	
class PlaceHolder(object):
	'''Sort of custom made 404 page.'''
	def GET(self):
		return render.placeholder()

class Backend(object):
	'''Barebones placeholder for a backend system.'''
	def GET(self):
		return render.backend()
		
	def POST(self):
		pass
		
if __name__ == "__main__":
	app.run()