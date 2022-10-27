"""
Numeric: int, float, complex
Boolean: True, False
String
List
Tuple
Set
Dict
=============================================
Frozen set: Immutable set
==================================
s = frozenset([10,20,30,40])
print(s)
print(dir(s))
# after looking at the output
# it tells us, frozenset does not contain mutable methods.
# example: pop, update,add,discard, remove etc
# Q. Differentiate Set and frozenset?
# Q. when to use set and frozenset??
===============================================
Range: is used to generate sequential numbers
Default range starts from 0
range is a data type
range is a function
Different patterns of range():
range(n/stop)=> stop is exclusive:stop will nt be added in the output
----------------------
print(list(range(16)))
# it will generate 0 - 15 , 16 will nt be in the output
-------------------------------------------
# range(start,stop)
print(list(range(16,21)))
# start is 16 and stop at 21
--------------------------------------------
# range(start,stop,step)
print(list(range(16,21,2)))
---------------------------
# Can we do -ve stepping
# yes
print(list(range(21,16,-1)))
----------------------------
# Q. Generate 1-100 numbers
print(list(range(1,101)))

generate 1-100 een numbers
print(list(range(2,101,2)))

generate 1-100 odd numbers
print(list(range(1,101,2)))
==========================================
bytes(): it is used to generate byte sequence for given list of int
it has a range: 0-256
===========================
k = [12,4,60]
print(bytes(k))
========================================
k = [12,4,60]
bt = bytes(k)
print(bt[-1])
#is it mutable?
# bt[-1] = 30
# in case of bytes direct assignment of value is nt possible
print(dir(bt))
# as it does nt contain any mutable method hence bytes is immutable
=======================================
bytearray(): it is same as that of bytes
but bytearray is Mutable in nature
----------------------------------------
k = [12,4,60]
bt = bytearray(k)
print(bt)
print(bt[-1])
bt[-1] = 30
print(bt)
print(bt[-1])
#-----------------
print(dir(bt))
# as it contains methods those support mutable operations, and changes
# persist in the same object
# hence its mutable
=========================================
None: its a keyword
Nothing, null, empty stub
--------------------------------
k = [1,None, None, 10]
print(k)
print(k[1])
========================================
NUMBER SYSTEM
TYPE CONVERSION/TYPECASTING
========================
NUMBER SYSTEM:
Binary [0,1]
Octal [0-7]
Decimal [0-9] #default
Hexadecimal [0-9A-F]
================================
num = 100
# binary
print('Decimal to binary:',bin(num)) # 0b1100100
print('Binary to Decimal:',0b1100100)
# Octal
print(oct(num)) # 0o144
print(0O144)
# Hex
print(hex(num)) # 0x64
print(0x64)
print('--------------------')
# hex to binary
print(bin(0x64))
===========================================
TYPECASTING:
1. Implicit: typecasting performed by python itself
Example:
print(10/5)
print('10'+'20')
print(0b1111)
print(4.5 + 1+5j)
--------------------------------
2. Explicit: typecasting performed by user
print(int(10/5))
print(int('10')+int('20'))
print(hex(0b1111))
print(str(4.5 + 1))
------------------
Assignment:
s = '190'
int
float
complex
bool
list
tuple
set
bytes
bytearray
bin
oct
hex
"""





