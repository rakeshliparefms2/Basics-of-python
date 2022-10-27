"""
Iterative statements/Conditional:
1. for loop
# Patterns: *,number, Alphabate
-----------------------------------------
*
**
***
****
*****
---------------------
for i in range(1,6):
    print(i*'*')
---------------------------
for i in range(1,6): #row
    for j in range(i): # column
        print(j*'*',end='')
    print()
--------------------------
for i in range(1,6): #row
    for j in range(1,i+1): # column
        print(j, end='')
    print()
===========================
for i in range(1,6): #row
    for j in range(1,i+1): # column
        print(i, end='')
    print()
====================\
55555
4444
333
22
1
==============================
for i in range(5,0,-1): #row
    for j in range(1,i+1): # column
        print(i, end='')
    print()
======================
for i in range(5,0,-1): #row
    for j in range(1,i+1): # column
        print(j, end='')
    print()
=====================
12345
1234
123
12
1
====================
for i in range(5,0,-1): #row
    for j in range(i,0,-1): # column
        print(j, end='')
    print()

for i in range(5,0,-1):
    print(i,end=' ')
================================

# Amulyas academy
==============================
# alphabates
========================
for i in range(1,6):
    print(chr(i+64)*i)
------------------
A
BB
CCC
DDDD
EEEEE
=====================
for i in range(1,6):
    print(chr(70-i)*i)
-----------------------
E
DD
CCC
BBBB
AAAAA
==========================
AAAAA
BBBB
CCC
DD
E
=====================\
for i in range(5,0,-1):
    print(i*chr(70-i))
===================
for i in range(1,6):
    print(chr(i+64)*(6-i))
-------------------------------------
2. While loop:
conditionally infinite loop
Hence we need some external factors to stop the contineous
iteration
Syntax:
while <condition>:
    statements
    .
    .
-----------------------
num = 1
while num == 1:
    print('hello')
    num = 2
--------------------------
# Write a program to print 1,10 natural numbers using while loop

num = 1
while num < 11:
    print(num)
    num += 1
=========================
# WAP to print 1,10 even numbers
num = 1
while num < 11:
    print(num+1)
    num += 2
=========================
# WAP to Print python 5 times
st = 'python'
count = 1
while count <=5 :
    print(st)
    count += 1
==============================
Q. What is difference between for and while???
while is condition based, for is not
in while we control of iteration,in for it read all objects in container
"""



























