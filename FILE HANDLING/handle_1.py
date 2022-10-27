"""
File:
Is a medium to store the data/information in a suitable format
Each file will be stored on hard drive.
With specific extension.
Example
sample.py
test.txt
flower.jpg
1.wav
3.mp3
-------------------------------------------------
Python supports default text files
Python has 2 file formats:
- .txt
- .binary file ( img, audio,video )
=========================================================
File operations are as follows:
- Create
- Open
- read
- write
- close
-----------------------------------
# All above operations we can do using a single function of a python
# i.e open()
------------------------------------
open()
- default text file we can read
- default mode is 'r' read mode
------------------------------------------
f = open('a.txt')
# f is a handle
print(f)
# Lets read the properties of a file
print('Name of a file:',f.name) # name
print('Mode of a file:',f.mode) # mode
print('Is read mode on?-',f.readable()) # bool
print('Is write mode on?-',f.writable()) # bool
print('is my file is closed?-',f.closed) #bool
# u need to close the file explicitly
f.close()
print('After close() is my file is closed?-',f.closed) #bool
--------------------------------------------------
# if file is present in another directory
# in same project so we need to give a complete path
----------------------------------------
# how to read a file from another directory in the project
f = open('C:\\Users\hakim\PycharmProjects\Batch_19\out.txt')
print(f)
--------------------------------------------------
# If i want to read a file from desktop
f = open(r"C:\Users\hakim\OneDrive\Desktop\b.txt")
# this is not working, how to read then???
------------------------------------------------------
# Modes present in Python:
-----------------------------
Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
===========================================
# READ OPERATION
"""
f = open('a.txt')
# now read the contents from a file
# i have 3 options present in r mode
# read(), readline(), readlines()
# -----------------------
print(f.read())











