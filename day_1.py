Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('Hello')
Hello
>>> print('Hello Good morning')
Hello Good morning
>>> print('Hello Good morning 1234')
Hello Good morning 1234
>>> 23 * 4
92
>>> #####################
>>> # Identifier rules
>>> # hash is used for commenting purpose
>>> jkhjhkjssfdsf
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    jkhjhkjssfdsf
NameError: name 'jkhjhkjssfdsf' is not defined
>>> # Identifier: it an identity of an object
>>> # object is an entity which exist in the memory
>>> # in python everything is an object
>>> 100
100
>>> 'python'
'python'
>>> 23.5
23.5
>>> # how to check object exist into the memory???
>>> # use id function of a python
>>> id(100)
140707068108928
>>> id('python')
2659653565384
>>> a = 100
>>> # a: is an identifier
>>> a
100
>>> id(a)
140707068108928
>>> b = 'python'
>>> b
'python'
>>> id(b)
2659653565384
>>> #######################
>>> # Rules of an identifier
>>> # Use a-zcharacters
>>> # while giving name to an object use all letters n lower case
>>> q = 'Java'
>>> q
'Java'
>>> A = 67
>>> A
67
>>> a
100
>>> # A and a makes a difference here
>>> # Python is case sensitive language
>>> py = 'python'
>>> py
'python'
>>> Py #here P is in caps
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    Py #here P is in caps
NameError: name 'Py' is not defined
>>> pY
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    pY
NameError: name 'pY' is not defined
>>> PY
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    PY
NameError: name 'PY' is not defined
>>> # Only numbers are not allowed
>>> 12 = 120
SyntaxError: can't assign to literal
>>> # we can use  alphabates + numbers
>>> # number as a prefix is not allowed
>>> 5a = 'good morning'
SyntaxError: invalid syntax
>>> 3b = 450
SyntaxError: invalid syntax
>>> # number as a suffix , its allowed
>>> a5 = 'good morning'
>>> a5
'good morning'
>>> b3 = 450
>>> b3
450
>>> # PEP8 standards
>>> # use of _ underscore is allowed in identifier
>>> _  = 'MI'
>>> _
'MI'
>>> a_5 = 'GM'
>>> a_5
'GM'
>>> bank_name ='SBI'
>>> bank_name
'SBI'
>>> bankname = 'BOI'
>>> bankname
'BOI'
>>> ############################
>>> # Special symbols and characters are not allowed
>>> # !@~$%^&*():"<>?{}_+
>>> c@ = 'sham'
SyntaxError: invalid syntax
>>> $bank_pin = 1234
SyntaxError: invalid syntax
>>> #########################
>>> # between 2 chars or words, space is not allowed
>>> a b = 300
SyntaxError: invalid syntax
>>> bank ifsc = 'SBI12344'
SyntaxError: invalid syntax
>>> a_b = 300
>>> a_b
300
>>> bank_ifsc = 'SBI12344'
>>> bank_ifsc
'SBI12344'
>>> ########################################
>>> bank_ifsc = 'SBI#@Q$#%##$'
>>> bank_ifsc
'SBI#@Q$#%##$'
>>> a = $ab
SyntaxError: invalid syntax
>>> ########################################
>>> # Keywords in python
>>> # These are reserved words from Python
>>> # to check keywords present in python
>>> # we have to import keyword library
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> # to count total number of keywords present in python
>>> # use len() function
>>> len(keyword.kwlist)
35
>>> # these keywords can not be used as an identifier
>>> del = 'C++'
SyntaxError: invalid syntax
>>> with = 600
SyntaxError: invalid syntax
>>> #################################
>>> # if u want to undestand meaning of each keyword
>>> # then use help() function
>>> help('not')
Boolean operations
******************

   or_test  ::= and_test | or_test "or" and_test
   and_test ::= not_test | and_test "and" not_test
   not_test ::= comparison | "not" not_test

In the context of Boolean operations, and also when expressions are
used by control flow statements, the following values are interpreted
as false: "False", "None", numeric zero of all types, and empty
strings and containers (including strings, tuples, lists,
dictionaries, sets and frozensets).  All other values are interpreted
as true.  User-defined objects can customize their truth value by
providing a "__bool__()" method.

The operator "not" yields "True" if its argument is false, "False"
otherwise.

The expression "x and y" first evaluates *x*; if *x* is false, its
value is returned; otherwise, *y* is evaluated and the resulting value
is returned.

The expression "x or y" first evaluates *x*; if *x* is true, its value
is returned; otherwise, *y* is evaluated and the resulting value is
returned.

(Note that neither "and" nor "or" restrict the value and type they
return to "False" and "True", but rather return the last evaluated
argument.  This is sometimes useful, e.g., if "s" is a string that
should be replaced by a default value if it is empty, the expression
"s or 'foo'" yields the desired value.  Because "not" has to create a
new value, it returns a boolean value regardless of the type of its
argument (for example, "not 'foo'" produces "False" rather than "''".)

Related help topics: EXPRESSIONS, TRUTHVALUE

>>> #how to check details of print function
 
>>> help(print)
 
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> help(id)
 
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

>>> ############################
     
>>> import keyword
     
>>> keyword.kwlist
     
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
