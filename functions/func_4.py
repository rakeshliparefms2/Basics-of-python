"""
VVVVVVIMP:
Anonymous function/Nameless function/lambda function
Syntax:
lambda parameter/s:expression
---------------------------------
It is a function without name
used for performing one time operation
One time operation/use means we can supply only one Expression
Multiple expressions are not allowed
==================================
s = lambda x: x + 100
print(s(50))
# Lambda function has implicit return statement
#-------Normal function--------
def add(x):
    return x + 100
print('add',add(50))
==============================
Example 2:
------------------
# Normal function
def square(n):
    return n*n
print(square(4))
#########################
sq = lambda n: n*n
print(sq(10))
-----------------------------
def convert(s):
    return s.split(),s.upper()
    # return list of string
out = convert('Hello all batch 19')
print(out)
#------------------------
con = lambda s:s.split(),s.upper()
print(con('This is mentos life'))
# only single expression or operation we can perform
# but more than 1 is not allowed in lambda

# How lambda is different from normal function
# What is the difference between lambda and normal function
=====================================
def sample(name,branch='SBI'):
    return name,branch
print(sample('Umesh'))
#-------------------
sample = lambda name,branch='BOI':name+' '+branch
#lambda with default arguemnt
print(sample('Priya'))
print(sample('Abhilash','IDBI'))
---------------------
info = lambda nm,age:nm+age
#print(info('34', 'Pranav')) #positional
print(info(age='34', nm='Pranav')) #keyword args
---------------------------------------
add = lambda a,b,c:a+b+c
print(add(10,1,30,40))
#in normal function return is optional
# in lambda function return is implicit/by default
#-------------------------------
# in  normal function we can return multiple values
# whereas in lambda only single expression we can return
-------------------------------
def add():
    pass
sub = lambda x:x+10

print(add)
print(sub)
#check the output
# lambda is used form short term purpose
basically used for writing a concise,simple, one liner, compact expression
-------------------------------------------
# WA function to find out even odd number
def check(num):
    if num%2 == 0:
        return 'Even'
    else:
        return 'Odd'
print(check(1))
#----------------------------
# to implement this logic we need ternary operator
check = lambda num: 'Even' if num %2 == 0 else 'Odd'
print('Lambda:',check(8))
-----------------------------------
# WA function to find out largest amongst 2 numbers
# return_of_if if_condition else else_return
grt = lambda x,y:'X is greater' if x>y else 'Y is greater'
print(grt(10,30))
print(grt(1,0))
--------------------------------
# Actually this lambda function is used in higher order function
as an input
 ---------------------
 Which are higher order function???
 3 types of higher order functions:
 1. map
 2. filter
 3. reduce
==========================================
1. map(func,iterable):
the function inside a map will be applied on each element from iterable
-------------------------------
ls = list(range(10,21))
print(ls)
# make a square of each element
print(map(lambda num:num*num, ls))
# when we got the output in the form of object
# then to see actual values typecast the object
print(list(map(lambda num:num*num, ls)))
# this lambda function will be applied on each element of ls
--------------------------------------------
Example2:

"""
nms = ['renuka','abhijit','akshay','Vaibhav','yogesh','arti']
# name should be in reverse order
#for i in nms:
#    print(i[::-1],end=' ')
#------------------------
#reverse = lambda name:name[::-1]
#print(list(map(reverse,nms)))
#---single line solution required
#print(list(map(lambda name:name[::-1],nms)))
#--------------Normal-------------------
def rev(nm):
    #print(type(nm))
    for i in nm:
        print(i[::-1],end=' ')

rev(nms)
#print(list(map(rev,nms)))