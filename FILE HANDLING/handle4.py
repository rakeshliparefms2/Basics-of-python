"""
Read Write operations over CSV file
CSV: Comma separated values
# Example:
Name,Age,Salary
---------------------------------
To perform operations related to csv file we need CSV module
----------------------------------
import csv
# Create a new csv file
f = open('sample.csv','w',newline='\n')
wr = csv.writer(f)
print(wr)
# use writerow function to add values as a list of string
wr.writerow(['Name','Age','Salary'])
wr.writerow(['Mahesh',23,45000])
wr.writerow(['Arti',23,55000])
wr.writerow(['Swapnil',25,95000])
-------------------------------------
import csv
f = open('test.csv','a',newline='\n')
wr = csv.writer(f)
n = int(input('How many records you want to add?'))
# wr.writerow(['Name','Age'])
for i in range(n):
    nm = input('Enter the name of Student:')
    ag = int(input('Enter the age:'))
    wr.writerow([nm,ag])
=================================================
import csv
f = open('test.csv','w',newline='\n')
wr = csv.writer(f)
n = int(input('How many records you want to add?'))
# wr.writerow(['Name','Age'])
for i in range(n):
    nm = input('Enter the name of Student:')
    ag = int(input('Enter the age:'))
    wr.writerow([nm,ag])
wr.writerow('\n')
wr.writerow('\n')
wr.writerow('\n')
f.seek(22)
wr.writerow(['Amit',34])
==================================================
Read Operation over CSV
-------------------------------
import csv
f = open('sample.csv')
#print(f.read())
rd = csv.reader(f)
print(rd)
print(list(rd))
# Can we add above list as a multiple record at a time
-=============================================================

f = open('a.txt')
print(f.closed)
f.close()
print('After close():',f.closed)
# in above example, we need to take care of close operation
# In python we have solution on this
# which does auto closing of a file
------------------------------------------
Syntax:
with open(filename.ext) as f:
    Operations related to file inside a block
Outside the scope ur file will get closed automatically
-------------------
Example:
with open('a.txt') as f:
    print(f.readline())
    print('Is file closed(inside):',f.closed)
print('Is file closed (outside):',f.closed)
--------------------------------------
with open('b.txt','w') as f:
    f.write('1234\n')
    f.write('00000')
=================================================
"""











