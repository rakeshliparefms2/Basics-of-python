Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # check keywords present in the python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> help('del')
The "del" statement
*******************

   del_stmt ::= "del" target_list

Deletion is recursively defined very similar to the way assignment is
defined. Rather than spelling it out in full details, here are some
hints.

Deletion of a target list recursively deletes each target, from left
to right.

Deletion of a name removes the binding of that name from the local or
global namespace, depending on whether the name occurs in a "global"
statement in the same code block.  If the name is unbound, a
"NameError" exception will be raised.

Deletion of attribute references, subscriptions and slicings is passed
to the primary object involved; deletion of a slicing is in general
equivalent to assignment of an empty slice of the right type (but even
this is determined by the sliced object).

Changed in version 3.2: Previously it was illegal to delete a name
from the local namespace if it occurs as a free variable in a nested
block.

Related help topics: BASICMETHODS

>>> # we cant use these keywords as an identifier
>>> a = 70
>>> a
70
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> try = 50
SyntaxError: invalid syntax
>>> # bcz these keywords are reserved keywords
>>> with = 'java'
SyntaxError: invalid syntax
>>> w = 'java'
>>> w
'java'
>>> with = 'java'
SyntaxError: invalid syntax
>>> # if we want to use with then change case sensitivity
>>> With = 'java'
>>> With
'java'
>>> # Python is case sensitive language
>>> a = 1
>>> a=1
>>> # PEP8 proposal
>>> ##############################
>>> 'Saurabh'
'Saurabh'
>>> "Saurabh"
'Saurabh'
>>> Saurabh # it will be treated as an identifier
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    Saurabh # it will be treated as an identifier
NameError: name 'Saurabh' is not defined
>>> print('Hello good evening to all participants')
Hello good evening to all participants
>>> print('Hello \ngood evening \nto all participants')
Hello 
good evening 
to all participants
>>> # \n for a new line
>>> print('Hello \ngood evening \n to all participants')
Hello 
good evening 
 to all participants
>>> print('Hello \tgood evening \tto all participants') # \t for tab
Hello 	good evening 	to all participants
>>> ########################
>>> print(123456789)
123456789
>>> print('My mobile number is:',9822131415)
My mobile number is: 9822131415
>>> #####################
>>> name = 'Umesh'
>>> name
'Umesh'
>>> age = 25
>>> age
25
>>> print('My name is:',name)
My name is: Umesh
>>> print('My name is:',name,'and age is:',age)
My name is: Umesh and age is: 25
>>> ####################
>>> print('My name is:','name','and age is:',age)
My name is: name and age is: 25
>>> #############
>>> 'avinash' # object
'avinash'
>>> avinash # identifier
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    avinash # identifier
NameError: name 'avinash' is not defined
>>> ####################
>>> # Space is also considered as a block
>>> print('            ')
            
>>> print('     hello       ')
     hello       
>>> ####################################
>>> print('My name is {} and age is {}'.format(name,age))
My name is Umesh and age is 25
>>> # lets change the sequence
>>> print('My name is {} and age is {}'.format(age,name))
My name is 25 and age is Umesh
>>> # here seuquence order matters, but we have a solution
>>> # give the positions
>>> print('My name is {1} and age is {0}'.format(age,name))
My name is Umesh and age is 25
>>> #################################
>>> # format specifiers: int 23 %d, float 12.5 %f, string 'python' %s
>>> name
'Umesh'
>>> age
25
>>> print('My name is %s and age is %d'%(name,age))
My name is Umesh and age is 25
>>> n1 = 'suresh'
>>> n2 = 'ramesh'
>>> n3 = 'mahesh'
>>> n1
'suresh'
>>> n2
'ramesh'
>>> n3
'mahesh'
>>> print('We are 3 friends:%s,%s,%s'%(n1,n2,n3))
We are 3 friends:suresh,ramesh,mahesh
>>> print('We are 3 friends:%s,%s,%s'%(n3,n2,n1))
We are 3 friends:mahesh,ramesh,suresh
>>> print('We are 3 friends:%s,%s'%(n3,n2,n1))
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    print('We are 3 friends:%s,%s'%(n3,n2,n1))
TypeError: not all arguments converted during string formatting
>>> print('We are 3 friends:%s,%s,%s'%(n3,n2))
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print('We are 3 friends:%s,%s,%s'%(n3,n2))
TypeError: not enough arguments for format string
>>> print('My name is %s and age is %d'%(name,age))
My name is Umesh and age is 25
>>> print('My name is %s and age is %d'%(age,name))
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print('My name is %s and age is %d'%(age,name))
TypeError: %d format: a number is required, not str
>>> print('My name is %s and age is %f'%(name,age))
My name is Umesh and age is 25.000000
>>> age
25
>>> 
