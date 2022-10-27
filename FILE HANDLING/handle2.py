"""
Read operation:
- read()
- readline()
- readlines()
-----------------------------------------
f = open('a.txt')
# print(f.read()) # used to read all the contents
# print(f.readline()) # used to read one line at a time
print(f.readlines()) # used to read all the contents but
# format is: list of string
# means each line of a text file will be a one element of a list
-------------------------------------------
# Iterations using the read operation
---------------------
read()
----------------

f = open('a.txt')
data = f.read()
for i in data:
    print(i)

# read a single block/char line by line
========================================
f = open('a.txt')
data = f.readline()
for i in data:
    print(i)

# read a first line character by character
========================================
f = open('a.txt')
data = f.readlines()
for i in data:
    print(i)
# read a line by line
# bcz its a list of string
# so one line at a time it will read
# All the lines will be visited
========================================
f = open('a.txt')
print(f.read(14))
print(f.read())
for i in range(3):
    print(f.read())
=========================
f = open('a.txt')
for i in range(3):
    print(f.readline())
    # will read 1st 3 lines
============================================

f = open('a.txt')
for i in range(3):
    print(f.readlines())

# Q. difference between read(), readline(), readlines()
-----------------------------------------------------------
# WRITE OPERATION
################################################
Modes used :
'w' Write
'a' append
'x' exclusive

All above modes are used to create a file+ performs Write operation
====================================
# w mode:
------------------------------------------
f = open('A.txt') Default its read mode
# case sensetivity abt file name is nt an issue here
# but extension(.txt) + proper name u should give  while reading
print(f.read())
---------------------------------
# lets create a new file using write mode
f = open('b.txt', mode='w')
# w mode performs Truncate operation
# remove old contents

# lets add new contents
print(f.writable())
#f.write('This is b.txt file\n')
#f.write('I am adding new content in this file\n')
#f.write('Lets enjoy new operation')
# write all in one write
f.write('This is new file\nI am adding new content\nEnjoy')
# above new content is overwritten in b.txt
# in write operation ur content must be in string format
f.write(1234) #accepts only str data type
---------------------------------------------------------
f = open('b.txt','w')
f.writelines(['Name is Ramesh\n','Age is 30\n','Place is Pune'])
f.writelines([12,'A','345','ASE'])# int values not allowed
==================================================
f = open('b.txt','w')
f.writelines('This is str we are\n supplying')
# in writelines list of string + string is allowed as an input
f.write(['A','F']) # list is nt allowed in write()
=================================
Q. Difference between write() and writelines()
==============================================
# Seek() and Tell() functions in file handling
-----------------------------
tell(): it will tell current position of ur cursor in the file
# used for checking operation
=============================
f = open('b.txt')
print(f.tell())
# lets read some blocks
print(f.read(4))
print(f.tell())
# seek(): bring the cursor to given position
f.seek(16)
print(f.read())
============================================
# read only transaction id
f = open('trans.txt','r')
f.seek(5)
print(f.read(12))
"""







