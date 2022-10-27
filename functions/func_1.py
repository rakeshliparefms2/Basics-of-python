"""
Function:
uses a strategy: Write ones and use multiple times
Advantage: Code Re-usability
----------------------------------
In programming, when we want a group of statements
to be executed as per requiremnt and multiple times
or it may be for ones then will write a block of code
and this is nothing but a Function
-------------------
Syntax:
def function_name():
    statement
    .
    .
===========================================
In function we have to follow 2 process:
1. Declaring the function
def simple():
    print('Hello')

2. Calling the function
simple()
=================================
in python we have 2 types of function:
1. Built-in function:
present in python default,
print()
id()
type()
bin()
list()
tuple()
range()

2. User defined function
will be created by user as per requirement
"""
# Declaration
def simple():
    print('Hello')

# calling
# to get output
# calling is important
simple()
for i in range(5):
    simple()

import test
test.suhas()
