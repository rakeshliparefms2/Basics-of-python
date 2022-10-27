"""
2. Iterative statements: used for performing iterations
Iteration means we use iterable(str,list,tuple,set,dict,range)
and from that iterable we fetch each element one by one

It contains 2 types
- for loop
syntax:
for(keyword) var(identifier) in(operator) sequence/iterable:
    print(var)
------------------------------------
Example
----------------------------
# input as list
nm = ['Ramesh','Mahesh','Suresh','Dinesh']
# default for loop read from left to right
for n in nm:
    print(n)
--------------------------------
# string
s = 'good evening Nilesh'
for char in s:
    print(char, end='')
-------------------------------------
# string: need to print only words
s = 'good evening Nilesh'
print(s.split())
for word in s.split():
    print(word)
==================================
# string: need to print words ending with 'h'
s = 'good evening Nilesh Umesh'
print(s.split())
for word in s.split():
    #print(word)
    if word.endswith('h'):
        print(word)
-----------------------------------
# string: need to print only numbers into another list
s = 'good evening Nilesh 9834373453 Umesh 34534523 '
print(s.split())
n = []
for word in s.split():
    #print(word)
    if word.isdigit():
        #print(word)
        n.append(word)
print(n)
-----------------------------------
s = {10,20,10,40,10,50}
for i in s:
    print(i)
    # set does not preserve sequence order
---------------------------
#dict
d = {'name': 'python', 'age': 32, 'place': 'US'}
for i in d:
    print(i)
    # default it fetches only keys
----------------------------------
d = {'name': 'python', 'age': 32, 'place': 'US'}
for i in d:
    # i is key
    #b = i, d.get(i)
    #print(b)
    print(i, d.get(i))
===================================
d = {'name': 'python', 'age': 32, 'place': 'US'}
for i in d.items():
    print(i)
===============================
d = {'name': 'python', 'age': 32, 'place': 'US'}
for i in d.values():
    print(i)
===============================
# range function
for i in range(5):
    #print(i)
    print('Kuldip')
===============================
# range function
for i in range(5,16):
    print(i)
-------------------------
# range function
for i in range(16,4,-1):
    print(i)
---------------------------
- while loop
"""

















