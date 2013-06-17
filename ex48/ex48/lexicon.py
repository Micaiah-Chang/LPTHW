# Lexicon for ex 48
# lexicon = [("direction", "north"),
                        # ("direction", "south"),
                        # ("direction", "east"),
                        # ("direction", "west"),
                        # ("direction", "north"),
                        # ("direction", "down"),
                        # ("direction", "left"),
                        # ("direction", "right"),
                        # ("direction", "back"),
                        # ("verb", "go"),
                        # ("verb", "stop"),
                        # ("verb", "kill"),
                        # ("verb", "eat"),
                        # ("stop", "the"),
                        # ("stop", "in"),
                        # ("stop", "of"),
                        # ("stop", "from"),
                        # ("stop", "at"),
                        # ("stop", "it"),
                        # ("noun", "door"),
                        # ("noun", "bear"),
                        # ("noun", "princess"),
                        # ("noun", "cabinet")
                        # ]     


                        
lexicon = { "north": "direction",
            "south": "direction",
                        "east": "direction",
                        "west": "direction",
                        "north": "direction",
                        "up": "direction",
                        "down": "direction",
                        "left": "direction",
                        "right": "direction",
                        "back": "direction",
                        "go": "verb",
                        "stop": "verb",
                        "kill": "verb",
                        "eat": "verb",
                        "the": "stop",
                        "in": "stop",
                        "of": "stop",
                        "from": "stop",
                        "at": "stop",
                        "it": "stop",
                        "door": "noun",
                        "bear": "noun",
                        "princess": "noun",
                        "cabinet": "noun"
                        }
 
def scan(stuff):
        words = stuff.split()
        sentence = []
        for item in words:
                if item.isdigit() == True:
                        temp = ('number', int(item))
                else:
                        temp = (lexicon.get(item.lower(),'error'),item.lower())
                #       temp = (lexicon[lexicon.index(item.lower()), item.lower())
                sentence.append(temp)   
                # try:
                        # int(item)
                        # temp = ('number', int(item))
                # except ValueError:
                        # item = item.lower()
                        # temp = (lexicon.get(item,'error'), item)
                # finally:
                        # sentence.append(temp)
        return sentence                 
