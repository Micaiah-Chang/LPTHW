try: 
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'Exercise 47',
	'author': 'Alan Huan Chang',
	'url': 'PLACEHOLDER.',
	'download_url': 'ALSO PLACEHOLDER PROBABLY GITHUB',
	'author_email': 'ahchang012@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': ['tests/ex47_tests.py'],
	'name': 'ex47'
}

setup(**config)