#test parser.py
from nose.tools import *
from ex48 import parser
from ex48 import lexicon

# direction_list = [('direction', 'north'),
			   # ('direction','south' ),
			   # ('direction', 'east'),
			   # ('direction', 'west'),
			   # ('direction','down'),
			   # ('direction', 'up'),
			   # ('direction', 'left'),
			   # ('direction', 'right'),
			   # ('direction', 'back')]
			   
# verb_list = [('verb', 'go'),
			# ('verb', 'kill'),
			# ('verb', 'stop'),
			# ('verb', 'eat'),]
			


object_list = [()]

def test_peek():
	assert_equal(parser.peek(lexicon.scan("north south east west")), "direction")
	assert_equal(parser.peek(lexicon.scan("moo ias blargh")), 'error')
	#assert_equal(parser.peek(""),None)
	
def test_match():
	assert_equal(parser.match(lexicon.scan("kill stop bear"), "verb"), ('verb', 'kill'))
	assert_equal(parser.match(lexicon.scan("kill stop bear"), "stop"), None)
	
def test_pverb(): #parse verb test
	assert_equal(parser.parse_verb(lexicon.scan("Eat it")), ("verb", "eat"))
	assert_equal(parser.parse_verb(lexicon.scan("In the eat")), ("verb", "eat"))
	assert_raises(Exception,parser.parse_verb, lexicon.scan("Princess ate the bear"))
	
def test_pobject():
	assert_equal(parser.parse_object(lexicon.scan("north princess")),('direction','north'))
	assert_equal(parser.parse_object(lexicon.scan("princess bear")),('noun','princess'))
	assert_raises(Exception, parser.parse_object, lexicon.scan("Eat the bear"))
	
def test_psub():
	sent = parser.parse_subject(lexicon.scan("eat the bear"), ('noun','princess'))
	subject = sent.subject
	verb = sent.verb
	object = sent.object
	assert_equal(subject, "princess")
	assert_equal(verb,"eat")
	assert_equal(object,"bear")
	
def test_psentence():
	def check(sent, subject, verb, object): 
		assert_equal(sent.subject, subject)
		assert_equal(sent.verb, verb)
		assert_equal(sent.object, object)
	sent = parser.parse_sentence(lexicon.scan("kill the bear"))
	
	check(sent, "player", "kill", "bear")
	
	sent = parser.parse_sentence(lexicon.scan("Princess kill the bear"))
	
	check(sent, "princess", "kill", "bear")
	
	
	assert_raises(Exception, parser.parse_sentence, (lexicon.scan('moo')))