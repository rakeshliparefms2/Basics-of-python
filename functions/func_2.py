"""
# syntax:
def function_name(parameters):
    .....
    .....
    .....

function_name(parameters)
If in declaration we have parameters then
we must need to supply values to it
==============================
# a, b are positional arguments
def sum(a,b):
    print(a+b)
sum(20,40)
sum(100,200)
sum(-10,-40)
sum(1)# this will raise exception bcz b value is nt given
sum()# this will give error bcz a,b values bt given
=========================================
# a, b are positional arguments
def sum(a,b):
    print(a+b)
sum(20,40,50,60)
# raise TypeError: sum() takes 2 positional arguments but 4 were given
=====================================
# a, b are positional arguments
def sum(a,b,c,d):
    print(a+b+c+d)
sum(10,20)
# raise TypeError: sum() takes 2 positional arguments but 4 were given
# Rule: if u have 4 parameters in declaration
# u must have to pass 4 values/arguments at the time of calling
======================================
# Types of arguments:
- Positional: sequence/order of values matters
--------------------------------------
Example:
---------------------------------------
def info(name,age):
    print('your name is:',name)
    print('Your age is:',age)
info('Suhas',24)
info(31,'python')
# bcz its positional hence
# 31 will be given to name and python will be age
=====================================
- Keyword: sequence/order of values doesn't matters
-----------------------------------
Example:
-------------------------------
def info(name,age):
    print('your name is:',name)
    print('Your age is:',age)
info('Suhas',24)
info(age=31,name='python')
# keyword map values to its exact parameter
# so, order doesnt matters in this case
==========================================
def display(roll_no,name,per,):
    print('Roll number:',roll_no,'name:',name,'percentage:',per)

display(name='Dinesh',roll_no=34,per=88)

display(name='Shital',roll_no=11,76)
# Rule: positional argument should nt follow keyword argument
=============================================
# we can specify/give a positional argument
# ONLY before Keyword argument
def display(roll_no,name,per,):
    print('Roll number:',roll_no,'name:',name,'percentage:',per)

#display(22,per = 88,name='Pranay')
# this is allowed because positional argument
# follow keyword argument
display(name='A',roll_no=12,name=99)
========================================
def sample(a,b,c):
    pass
sample(a =10,b= 10,c=10)
=============================
def sample(a,b,c):
    print(a,b,c)
sample('10','20','30')
# if i expect first 2int, last float
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = float(input('Enter c:'))
sample(a,b,c)
==========================================================
- Default
-----------------------------
# Default arg we can supply in declaration only
def bank(name,branch,IFSC='SBI7700'): #here IFSC is a default arg.
    print(name,branch,IFSC)
bank('Supriya','Katraj')
bank('Swapnil','Swaragate','BOI87234')
bank('Sujit','Katraj','BOM783645')
===============================
def operating_sys(name,account='Guest'):
    print('Hello',name,'welcome to',account,'account')

operating_sys('Renuka')
operating_sys('Karishma','Star')
=========================================
- Variable length
"""
