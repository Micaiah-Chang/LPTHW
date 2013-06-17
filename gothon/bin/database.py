import web

db = web.database(dbn='mysql', user='Newbie', pw='password', db='physics')


urls = (
	'/(.*)', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
	def GET(self, name):
		return render.index(name)
		
if __name__ == "__main__":

	app.run()