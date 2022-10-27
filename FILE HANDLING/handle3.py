"""
WRITE OPERATION:
- w mode
- a append mode
- x exclusive mode
------------------------------------------
append mode: create+add lines at the end
------------------------
f = open('c.txt','a')
print(f.writable())
# it is used to create file + add contents at the end of file
# add some contents
# f.write('This is append mode\n')
# f.write('We can add contents at the end')
f.write('\n1234234546')
---------------------------------
x: exclusive mode
Rule: if file is not present then create a new file
but if file already present then throw an exception FileExistsError:
- this is used to create a file only ones
-----------------------------------------------
# create a new file d.txt with x mode
f = open('d.txt','x')
print(f.writable())
f.write('123\n4567')
--------------------------------------------
Another file extension is binary file
img,audio,video
-------------------
Lets try to read an image file from desktop
-------------------------------------
f = open('C:\\Users\hakim\OneDrive\Desktop\\New\ML_flow.jpeg','rb')
# rb means read in binary mode
# print(f.read())
data = f.read()

f2 = open('C:\\Users\hakim\OneDrive\Desktop\sample.png','wb')
# wb write in binary
f2.write(data)

# Assignment: Read a text file and write contents to other files
----------------------------------------------------------

# lets create a new empty file
# open('e.txt','w')

# find out mobile number present in the e.txt
f = open('e.txt')
# print(f.read())

# for i in f.read():
#    if i.isdigit():
#        print(i,end='')
# --------------------
# print(f.read().find('9'))
#f.seek(39)
#print(f.read())
# ----------------------------
print(f.read().split(':')[-1])
====================================
# Read f.txt, it contains numbers
# read those numbers, display addition + average
---------------------------------------
f = open('f.txt')
tot = 0
#print(f.read().split(','))
data = f.read().split(',')
print(data)
for i in data:
    #print(type(i))
    # default dtype is str we need to typecast
    tot += int(i)
print(tot)
print(tot/len(data))
--------------------------------------
# Display Name and Age from g.txt
# now add Name and age data into h.txt
f = open('g.txt')
f2 = open('h.txt','w')
# print(f.read())
data = f.readlines()
for i in data:
    #print(i.split(',')[:2])
    f2.writelines(i.split(',')[:2])
    f2.write('\n')
------------------------------------------
"""
f = open('C:\\Users\hakim\OneDrive\Desktop\\trans.txt')
print(f)

f2 = open('C:\\Users\hakim\OneDrive\Desktop\\trans2.txt','w')








