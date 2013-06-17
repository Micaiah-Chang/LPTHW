class ParserError(Exception):
	pass
	
class Sentence(object):

	def __init__(self, subject, verb, object):
		# remember we take ('noun', 'princess') tuples and convert them
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = object[1]
		
		
def peek(word_list): #expects a list of tuples
	if word_list: #if this argument exists
		word = word_list[0] #takes the first tuple
		return word[0]  #and returns the first element of that tuple
	else:
		return None
		
		
def match(word_list, expecting): #takes a list of tuples and a word_type
	if word_list:
		word = word_list.pop(0) #take the first element from the list and set it equal to word
		
		if word[0] == expecting: #if the first element aka the word type works
			return word #then return the entire tuple
		else:
			return None #otherwise, don't return anything
	else:
		return None
		
		
def skip(word_list, word_type):
	while peek(word_list) == word_type: #if the word type matches the type in the word list...
		match(word_list, word_type) # check it to see if they're the same
		
def parse_verb(word_list):
	skip(word_list, 'stop')
	
	if peek(word_list) == 'verb':
		return match(word_list, 'verb')
	else: 
		raise ParserError("Expected a verb next.")
		
		
def parse_object(word_list):
	skip(word_list, 'stop')
	next = peek(word_list)
	
	if next == 'noun':
		return match(word_list, 'noun')
	if next == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParserError("Expected a noun or direction next.")
		
def parse_subject(word_list, subj):
	verb = parse_verb(word_list)
	obj = parse_object(word_list)
	
	return Sentence(subj, verb, obj)
	

def parse_sentence(word_list):
	skip(word_list, 'stop')
	
	start = peek(word_list)
	
	if start == 'noun':
		subj = match(word_list, 'noun')
		return parse_subject(word_list, subj)
	elif start == 'verb':
		# assume the subject is the player then
		return parse_subject(word_list, ('noun', 'player'))
	else:
		raise ParserError("Must start with subject, object or verb not: %s" % start)
		