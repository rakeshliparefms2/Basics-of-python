'''
f = open('a.txt')
# 3 options
# read(), readline(), readlines()
# read() will read all the contents start to end
print(f.read())
---------------------------
supppose if  u want to read some specific part
f = open('a.txt')
print(f.read(10))
--------------------------------------
# readline(): it reads one line at a time
f = open('a.txt')
print(f.readline())
print(f.readline())
-----------------------------
# readline(hint): it reads one line at a time
f = open('a.txt')
print(f.readline(5)) # wil read 5 block from line1
print(f.readline(5)) # wil read 5 block from line1
print(f.readline()) # wil read remaining block from line1
print(f.readline())# will read next line
---------------------------------
# readline(hint): it reads one line at a time
f = open('a.txt')
print(f.readline()) # read line1
print(f.readline())# read line2
-------------------------------------
# readline(limit): it reads one line at a time
f = open('a.txt')
print(f.readline()) # read line1
print(f.readline())# read line2
'''
