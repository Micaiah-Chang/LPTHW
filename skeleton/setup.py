try: 
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'My Project',
	'author': 'Alan Huan Chang',
	'url': 'PLACEHOLDER.',
	'download_url': 'ALSO PLACEHOLDER PROBABLY GITHUB',
	'author_email': 'ahchang012@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)