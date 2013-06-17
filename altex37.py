#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ex37.py -- Symbol Review (exercise from the book "Hard Way Pithon v 2")

def print_title( title, decorators ):
    """ Prints title with decoration '*' symbols around it """
    decorators = "*" * decorators
    print "\n%s %s: %s\n" % ( decorators, title, decorators )

def go_forward():
    """ Waits for press an Enter key """
    raw_input( "Press ENTER to continue: ")
    print "\n"
    
print_title( "#1 KEYWORDS", 40 ) # Begin of the section with keywords

print_title( "#1.1 Keywords: 'and'", 20 ) # 1st keyword: and
print """\tThe expression 'x and y' first evaluates ('evaluate' -
'оценивать') 'x'. If 'x' is FSalse, its value is returned. Otherwise,
'y' is evaluated and the resulting value is returned.
"""

# 1.1 EXAMPLE with 'and'
var_a = 123
var_b = 'BIG'
print var_a and var_b

go_forward()

print_title( "#1.2 Keywords: 'del'", 20) # 2nd keyword: del
print """\tDeletion is reqursively defined very similar to the way
assignment ('assignment' - 'присвоение') is defined.
\tDeletion of a target list reqursively deletes each target, from left
to right.
\tDeletion of a name removes a binding of that name from the local or
global namespace, depending on whether the name occurs ('occurе' -
'происходить', 'встречаться').
\tIt's illigal to delete a name from the local namespace if it occurs
as a free variable in a nested ('nested' - 'вложенный') block.
\tDeletion of attribute references ('reference' - 'ссылка',
subscriptions ('subscription' - 'подписка', 'подпись') and slicings
('slicing' - 'нарезка') is passed ('передается') to the primary
('primary' - 'основной') object involved ('involve' - 'включать в
себя').
"""

# 1.2 EXAMPLE with 'del'
del var_a, var_b

go_forward()

print_title( "#1.3 Keywords: 'import' and 'from'", 20 ) # 3rd keywords: import, from
print """\tImport statements ('statement' - 'оператор') are executed in
two steps: (1) find a module and initialize it if necessary; (2) define
('define' - 'определять') a name or namespaces in the local namespace
(of the scope ('scope' - 'предел', 'охват') where the 'import' statement
occurs.
"""

# 1.3 EXAMPLE with 'from'
from sys import argv

go_forward()

print_title( "#1.4 Keywords: 'not'", 20) # 4th keyword: not
print """\tThe operator 'not' yields ('yield' - 'давать', 'приносить')
True if its argument is False, False otherwise.
"""

# 1.4 EXAMPLE with 'not'
print not False

go_forward()

print_title( "#1.5 Keywords: 'while'", 20 ) # 5th keyword: while
print """\tThe 'while' statement is used for repeated execution as long
as an expression is True.
"""

# 1.5 EXAMPLE with 'while'
one = 1
while one == 1:
    print one
    one = one + 1

go_forward()

print_title( "#1.6 Keywords: 'with' and 'as'", 20 ) # 6th keywords: with, as
print """\tThe 'with' statement is used to wrap ('wrap' - 'оборачивать',
'упаковывать') the execution of a block with methods defined by a
context manager.
""" 

# 1.6 EXAMPLE with 'with' and 'as'
print "..."

go_forward()

print_title( "#1.7 Keywords: 'if', 'elif' and 'else'", 20 ) # 7th keywords: if, elif, else
print """\tThe if statement is used for conditional ('conditional' - 
'условный') execution. It selects exactly ('exactly' - 'точно') one of
the suites ('suite' - 'набор') by evaluating the expressions one by one
until one is found in 'if' or 'elif' to be True. If all expressions are
false, the suite of the 'else' clause ('clause' - 'пункт') if presented
is executed.
"""

# 1.7 EXAMPLE with 'if', 'elif' and 'else'
if( False ): print "if"
elif( True): print "elif"
else: print "else"

go_forward()

print_title( "#1.8 Keywords: 'global'", 20 ) # 8th keyword: global
print """\tThe 'global' statement is a declaration which holds
('действует') for the entrie ('entire' - 'весь') current code block. It
means that the listed identifiers ('identifier' - 'идентификатор') are
to be interpreted as globals.
"""

# 1.8 EXAMPLE with 'global'
def my_function():
    global one
    print one
    
my_function()

go_forward()

print_title( "#1.9 Keywords: 'or'", 20 ) # 1.9 keyword: or
print """\tThe expression 'x or y' first evaluates 'x'. If 'x' is TRUE,
its value is returned; otherwise 'y' is evaluated and the resulting
value is returned.
"""

# 1.9 EXAMPLE with 'or'
print False or True

go_forward()

print_title( "#1.10 Keywords: 'assert'", 20 ) # 1.10 keyword: assert
print """\tAssert ('assert' - 'утверждать') statements are a convenient
way to insert debugging assertions into a program. If assert is False, 
'AssertionError' is being called.
"""

# 1.10 EXAMPLE with 'assert'
assert( True )

go_forward()

print_title( "#1.11 Keywords: 'pass'", 20 ) # 1.11 keyword: pass
print """\tPass is a null operation - when it is executed, nothing
happens. It is usefull as a placeholder, when a statement is required
syntactically.
"""

# 1.11 EXAMPLE with 'pass'
pass

go_forward()

print_title( "#1.12 Keywords: 'yield'", 20 ) # 1.12 keyword: yield
print """\tThe 'yield' statement is only used when defining a generator
function, and is only used in the body of the generator function. Using
a 'yield' statement in a function definition is sufficient
('sufficient' - 'достаточно') to cause that definition to create a
generator function instead of a normal function.
"""

# 1.12 EXAMPLE with 'yield'
print "..."

go_forward()

print_title( "#1.13 Keywords: 'break'", 20 ) # 1.13 keyword: break
print """\t'break may only occur syntactically nested in a 'for' or
'while' loop, but not nested in a function or class definition whithin
that loop.
"""

# 1.13 EXAMPLE with 'break'
while True:
    print "break"
    break

go_forward()

print_title( "#1.14 Keywords: 'try', 'except' and 'finally'", 20 ) # 1.14 keyword: try, except, finally
print """\tThe 'try' statement specifies ('specify' - 'указывать',
'уточнять') exception ('exception' - 'исключение') handlers ('handler'-
'обработчик') and/or cleanup code for a group of statements.
\tThe 'except' clause(s) specify one or more exception handlers.
If 'finally' is presented, it specifies a 'cleanup' handler.
"""

# 1.14 EXAMPLE with 'try', 'except' and 'finally'
f = None
filename = "test_file.txt"
try:
    try:
        f = open( filename )
        text = f.read()
    except IOError:
        print 'An error occured'
finally:
    if f:
        f.close()

go_forward()

print_title( "#1.15 Keywords: 'print'", 20 ) # 1.15 keyword: print
print """\t'print' evaluates each expression in turn and writes the
resulting object to standert output.
"""

# 1.15 EXAMPLE with print
print "example"

go_forward()

print_title( "#1.16 Keywords: 'class'", 20 ) # 1.16 keyword: class
print """\tA class definition defines a class object.
"""

# 1.16 EXAMPLE with class
class new_class():
    pass

go_forward()

print_title( "#1.17 Keywords: 'exec'", 20 ) # 1.17 keyword: exec
print """\tThis statement supports dynamic execution of Python code.
"""

# 1.17 EXAMPLE with exec
var_print = "print 'example'"
exec( var_print )

go_forward()

print_title( "#1.18 Keywords: 'in'", 20 ) # 1.18 keyword: in
print """\tFor the list and tuple ('tuple' - 'из того же набора') types,
'x in y' is True if and only if there exists an index 'i' such that
'x == y[ i ]' is True.
\tFor the Unicode and strings types, 'x in y' is True if and only if
'x' is a substring of 'y'.
""" 

# 1.18 EXAMPLE with in
print "a" in "abc"

go_forward()

print_title( "#1.19 Keywords: 'raise'", 20 ) # 1.19 keyword: raise
print """\tIf no expressions are presented, 'raise' ( 'raise' -
'повышать', 'поднимать' ) re-raises the latest exception that was active
in the current scope. If no exception is active in the current scope, a
'TypeError' exception is raised indicating that this is an error.
"""

# 1.19 EXAMPLE with raise
print "..."

go_forward()

print_title( "#1.20 Keywords: 'continue'", 20 ) # 1.20 keyword: continue
print """\t'conrinue' may only occur syntactically nested in a 'for' or
'while' loop, but not nested in a function or class definition or
'finally' clause within that loop. It continues with the next cycle of
the nearest enclosing loop.
"""

# 1.20 EXAMPLE with continue
one = []
for letter in "python":
    if letter == 'h':
        one.append( 'H' )
        continue
    one.append( letter )
print one

go_forward()

print_title( "#1.21 Keywords: 'is'", 20 ) # 1.21 keyword: is
print """\tThe operators 'is' and 'is not' test for object identity:
'x is y' is true if and only if 'x' and 'y' are the same object.
'x is not y' yields the invers truth value.
"""

# 1.21 EXAMPLE with is
print "python" is "python"

go_forward()

print_title( "#1.22 Keywords: 'return'", 20 ) # 1.22 keyword: return
print """\t'return' leaves the current function call with the expression
list (or 'None') as return value.
"""

# 1.22 EXAMPLE with return
def hello_world():
    return "hello_world"
    
print hello_world()

go_forward()

print_title( "#1.23 Keywords: 'def'", 20 ) # 1.23 keyword: def
print """\tA function definition defines a user-defined function object.
"""

# 1.23 EXAMPLE with def
def any_function():
    pass
    
go_forward()


print_title( "#1.24 Keywords: 'lambda'", 20 ) # 1.24 keyword lambda
print """\tLambde forms (lambda expressions) have the same syntactic
position as expressions. They are shorthand ('to be shorthand' -
'быть сокращенным' to create anonymus functions. The expression 'lambda
arguments: expression' yields a function object.
"""

# 1.24 EXAMPLE with lambde
g = lambda x: x**2
print g( 3 )

go_forward()

print_title( "#2 DATA TYPES", 40 ) # 2nd part

print_title( "#2.1 Data Types: 'True' and 'False'", 20 ) # 1st data types set: True and False
print """\tReturnes True when the argument x is True, False otherwise.
The built ins ( 'built ins' - встроенные модули) True and False are only
 two instances of the class bool.
"""
go_forward()

print_title( "#2.2 Data Types: 'None'", 20 ) # 2nd data type: None
print """\tThe solve ('solve' - 'решать') value of 'types.NoneType' is
frequently ('frequently' - 'часто') used to represent the absence
('absence' - 'отсутствие') of value, as when default arguments are not
passed to a function.
"""

go_forward()

print_title( "#2.3 Data Types: 'strings', 'numbers', 'floats', 'lists'", 20 ) # 3rd data types set: strings, numbers, floats, lists
print """\t1. 'types.StringType' - the type of character strings (e.g.
('e.g' = 'exampli gratia' -  'например') "Spam"); alias ('alias' -
'псевдоним') of the built-in 'str'.
\t2. Class 'numbers'. Subclasses of this type describe complex numbers and include the
operations that work on the build-in 'complex' type.
\t3. 'types.FloatType' - the type of floating point numbers (e.g. 1.0);
alias of the built in 'float'.
\t4. 'types.ListType' - the types of lists (e.g. [ 0, 1, 3 ]); alias of
the build-in 'list'.
"""

go_forward()

print_title( "#3 STRING ESCAPE SEQUENCES ('sequence' - 'последовательность')", 40 ) # string escape sequences

print_title( "#3.1 String escape sequences: '\\\\'", 20 ) # 1st sequence: \\
print "\tBackslash."

go_forward()

print_title( "#3.2 String escape sequences: \'\\'\'", 20 ) # 2nd sequence: \'
print "\tSingle quote."

go_forward()

print_title( "#3.3 String escape sequences: '\\\"'", 20 ) # 3rd sequence: \"
print "\tDouble quote."

go_forward()

print_title( "#3.4 String escape sequences: '\\a'", 20 ) # 4th sequence: \a
print "\tASCII Bell."

go_forward()

print_title( "#3.5 String escape sequences: '\\b'", 20 ) # 5th sequence: \b
print "\tASCII Backspace."

go_forward()

print_title( "#3.6 String escape sequences: '\\f'", 20 ) # 6th sequence: \f
print "\tASCII Formfeed ('form feed' - 'перевод страницы')."

go_forward()

print_title( "#3.7 String escape sequences: '\\n'", 20 ) # 7th sequence: \n
print "\tASCII Linefeed. ('line feed' - 'перевод строки')"

go_forward()

print_title( "#3.8 String escape sequences: '\\r'", 20 ) # 8th sequence: \r
print "\tASCII Carriage Return."

go_forward()

print_title( "#3.9 String escape sequences: '\\t'", 20 ) # 9th sequence: \t
print "\tASCII Horizontal Tab."

go_forward()

print_title( "#3.10 String escape sequences: '\\v'", 20 ) # 10th sequence: \v
print "\tASCII Vertical Tab."

go_forward()

print_title( "#4 STRING FORMATS", 40 ) # Begin of a clause about "String formats"

print_title( "#4.1 String formats: '%d'", 20) # 1st string format: %d
print "\tSigned integer decimal ('десятичное целое число')."

go_forward()

print_title( "4.2 String formats: '%i'", 20 ) # 2nd string format: %i
print "\tSigned integer decimal."

go_forward()

print_title( "4.3 String formats: '%o'", 20 ) # 3rd string format: %o
print "\tSigned octal value ('целое восмеричное значение')."

go_forward()

print_title( "4.4 String formats: '%u'", 20 ) # 4th string format: %u
print "\tObsolete ('obsolete' - 'устаревший') type. Identical to '%d'."

go_forward()

print_title( "4.5 String formats: '%x' and '%X'", 20 ) # 5th string formats: %x, %X
print "\tSigned hexadecimal ('целое шеснадцетиричное') (lowercase and uppercase)."

go_forward()

print_title( "4.6 String formats: '%e' and '%E'", 20 ) # 6th string formats: %e and %E
print "\tFloating point expanential format (lowercase and uppercase)."

go_forward()

print_title( "4.7 String formats: '%f' and '%F'", 20 ) # 7th string formats: %f and %F
print "\tFloating points decimal formats."

go_forward()

print_title( "4.8 String formats: '%g' and '%G'", 20 ) # 8th string formats: %g and %G
print """\tFloating point format. Uses lowercase (uppercase) exponential
format if exponent is less than -4 or not less than precision
('precision' - 'точность'), decimal format otherwise.
"""

go_forward()

print_title( "4.9 String formats: '%c'", 20 ) # 9th string format: %c
print "\tSingle character (accepts integer or single character string)."

go_forward()

print_title( "4.10 String formats: '%r'", 20 ) # 10th string format: %r
print "\tString (converts any Python object using 'repr()')."

go_forward()

print_title( "4.11 String formats: '%s'", 20 ) # 11th string format: %s
print "\tString (converts any Python object using 'str()')."

go_forward()

print_title( "4.12 String formats: '%%'", 20 ) #12th string format: %%
print """\tNo argument is converted, results in a '%' character in the
result.
"""

go_forward()

print_title( "#5 OPERATORS", 40 ) # last 5th capitel: OPERATORS of Python

print_title( "#5.1 Operators: '+', '-', '*', '/', '//', '%', '**'", 20 ) # 1st operators case: +, -, *, /, //, %
print"""\t'+' - addition.
\t'-' - substraction.
\t'*' - multiplication
\t'/' - division
\t'//' - division, that results a float value
\t'%' - remainder ('remainder' - 'остаток')
\t'**' - power ('power' - 'сила', 'степень')
"""

go_forward()

print_title( "#5.2 Operators: '<', '<=', '>', '>=', '==', '!=',", 20 ) # 2nd operators block: <, <=, >, >=, ==, !=
print """\t'<', '<=', '>', '>=' - ordering.
\t'==' - equality
\t'!=' - difference
"""

go_forward()

print_title( "#5.3 Operators: '@'", 20 ) # 3rd operator: @
print """\tA function definition may be wrapped ('обернута') by one or
more 'decorator' expressions. Decorator expressions are evaluated, when
the function is defined, in the scope that contains the function
definition. The result must be a callable, which is invoked ('invoke' - 
'вызывать') with the function object as the only argument.
"""

go_forward()

print_title( "#5.4 Operators: '+=', '-=', '*=', '/=', '//=', '%=', '**='", 20 ) #3rd group: +=, -=, *=, /=, //=, %=, **=
print """\tAugmented ('augmented' - 'расширенный') assigment is a
combination, in a single statement, of a binary operation and an
assignment statement.
"""

go_forward()

print_title( "THE END", 40 )
