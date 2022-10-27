"""
Higher order function:
- map(func,iterable)
- filter(func,iterable)
used to filter out the values based
on condition given inside a function
it will return results for only True instances

filter will give a original sequence or may be sub-sequence
================================
- reduce(func,sequence)
-------------------------------
k = [12,45,3,67,89,90,1,23,44,68,22]
# filter out even number from above sequence
even = lambda no : no%2==0
# filter will check this condition and selects values
# from sequence where it returns True
#print(even(9))
print(filter(even,k))
# typecast the filter object
print(list(filter(even,k)))
------------------------------
k = [12,45,3,67,89,90,1,23,44,68,22]
# filter out numbers divisible by 5
print(tuple(filter(lambda num: num % 5 == 0,k)))
-------------------------------------------
names = ['Ajay','Vijay','Nitish','Ramesh','Suresh','Ratna']
# WA single line solution: for to fetch name end with 'h'
print(list(filter(lambda nm: nm.endswith('h'),names)))
------------------------------------------------------
# Q. what is difference/similarity between map and filter??
====================================================
# Reduce: used to reduce the sequence into single object
Example: sum,greater no,
------------------
Reduce is not directly present like map and filter
it is present in functools module
so we need to import reduce
Syntax:
reduce(function,sequence)
--------------------------
from functools import reduce
k = [12,45,3,67,89,90,1,23,44,68,22]
# addition of all numbers
print(reduce(lambda x,y:x+y,k)) # performs cumulative addition
# in case of reduce we need not to typecast
-------------------------------
from functools import reduce
k = [12,45,3,67,89,90,1,23,44,68,22]
# find out largest number
print(reduce(lambda x,y: x if x>y else y,k))
--------------------------------
Assignment:
Solve 10 examples on each higher order function
==============================================
# Nested functions:
function inside another function is nested function
----------------------------
def outer():
    print('This is outer function')
    def inner():
        print('Inner function')
    inner()
outer()
=========================
# function referencing
# using outer we are referring to inner
def outer():
    print('This is outer function')
    def inner():
        print('Inner function')
    return inner
o = outer()
print(o)
# o in an instance of inner
o()
o()
==========================
def central_gov():
    print('Central')
    def state_gov():
        print('State')
    return state_gov
ref = central_gov()
print(ref)
# this ref will use to access state_gov
ref()
ref()
ref()
=============================
def central_gov():
    print('Central')
    def state_gov():
        print('State')
    return central_gov,state_gov
ref1,ref2 = central_gov()
print(ref1,ref2)
# this ref will use to access state_gov
ref1()
ref1()
ref2()
===============================
def central_gov():
    print('Central')
    def state_gov():
        print('State')
    return central_gov,state_gov
ref1,ref2 = central_gov()
print(ref1,ref2)
# this ref will use to access state_gov
ref1()
ref1()
ref2()
===========================
def outer():
    x = 100
    def inner():
        print(x)
    inner()
outer()
===============================
# Function aliasing: giving a nick name or
short name to existing function
-----------------
def prerajulization():
    print('Operations')
p = prerajulization
p()
p()
-----------------
"""










