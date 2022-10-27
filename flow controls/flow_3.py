"""
# q. Reverse the words:Bachchan Amitabh
s = 'Amitabh Bachchan'
for i in s.split()[::-1]:
    print(i,end=' ')
=======================
# q. Reverse the character/blocks
s = 'Amitabh Bachchan'
# print(s[::-1])
print(reversed(s))
# whenever u get output in the form of object
# in order to get values from it
# u have 2 options:1. iterate over it 2. typecast
#print(tuple(reversed(s)))
final = ''
for i in reversed(s):
    final+=i #it will concatenate one block at a time
print(final)
===============================
# q. Reverse the character/blocks
s = 'Amitabh Bachchan'
print(s[-3])
#-1 to -n
for i in range(-1,-(len(s)+1),-1):
    #print(i,end=' ')
    print(s[i],end='')
==============================
# q. Reverse the character of individual word
s = 'Amitabh Bachchan'
for i in s.split():
    print(i[::-1],end=' ')
==============================
# q. i want to fetch vowels from the string: a,i,o,u,e
s = 'Amitabh Bachchan'
vowels = ['a','i','e','o','u','A','I','O','U','E']
for i in s:
    if i in vowels:
        print(i,end=' ')
===================================
# Interview q. i want a dict of each block and its count
#  {'A':1,'m':1,'i':1,'t':1,'a':3.....}
s = 'Amitabh Bachchan'
d = {}
for i in s:
    #print(i,s.count(i))
    # d[key] = value
    d[i] = s.count(i)
print(d)
"""
# Interview q. interchange 1st and last 2 chacters from string
# Expected: 'hantabh BachcAmi'
s = 'Amitabh Bachchan'
#################################
# Print the +ve and -ve index of each block
# example: A is present at 0,-16
#################################
# my key  =3
# means i want to shift characters by 3
# input  s = 'Amitabh Bachchan'
# Expected: 'Dplw....
###############################
