print "\\ \\\\" # prints out a backslash
print "\'Look at the pretty single quotes\' \\'" # prints out a single quote
print '\"How about them double quotes?\" \\"' # prints out a double quote
print "A sound comes out when I do \\a!\a" # Produces a sound
print "Moo.\b, \\r" # moves back one space, so that , is replaced by ,
print "Hey\\n \nYo" #linebreak
print "Yes\rNo. \\r" #Returns to the start of the line and overwrites whatever
print "Yes\rNo\n \\r"
print "There be Tabs\t here. \\t" # Puts a tab there
print "Vertical \v tabs \vahoy. \\v" #Puts a verticle tab

print "%d"
print "There are integers here: %d or five." %5 #%d gives you integers
print "%i"
print "This is another way to write integers such as %i." % -3 # Same here. 
#Both of the above are the same
print "%o"
print "Prints numbers in base 8, for example 50 is %o. (50/8 = 6 remainder 2)" %50
#Above is Octal
print "%u"
print "Prints out decimals, but can't do negatives: %u and %u" %(-10.1, 10.1)
#Supposed to be unsigned decimal
print "%x"
print "Unsigned hexidecimal, testing with 255 and 128: %x and %x." %(255,128)
print "%X"
print "Also unsigned hexidecimal, only with uppercase %X and %X."  %(255,128)
print "%e"
print "Gives it in exponential notation, always with 6 zeros after: %e"% 1
#Floating point exponential format
print "%E"
print "Same as above only the E is uppercase: %E" % 500
print "Prints out floating point decimals: %f." % 123.56
print "%F"
print "Prints out floating point decimals: %F." % 51.1
print "%g"
print "Floating point, but uses expoential if exponent is greater than -4 or less than precision."
print "Compare: 10 and 0.0000001: %g ,  %g " %(10, 0.0000001)
print "%G"
print "Same as above: %G, %G, note the uppercase exponential." %(10, 0.0000001)
print "%c"
print "Just prints out single characters like %c." % 'i'
print "%r"
print "Always prints out a string, like %r or %r." % (100, 'foo')
print "%s" 
print "Prints out a string like %s." % 'Moo'
print "%%"
print "Just printing % signs"