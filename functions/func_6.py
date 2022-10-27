"""
z = lambda a,b:(a+b,a-b,a+100)
print(z(10,20))
==============================
Types of Variable:
Global var.
Local Var.
Non local
===========================
Global variable:
The variable which is available anywhere throughout the program
and we declare this variable outside the function
at the same indent level
Example:
# global variable
x = 200
def test():
    # access x inside a function
    print('Inside:',x)

# access x outside a function
print('Outside:',x)
test()
-----------------------------------
Local Variable:
the variable which is declared inside a function called as Local var
This var. wil nt be accessible outside the function
Local var is having a restricted scope
means it will be accessible only to that function or within the function
outside we  cant access.
Example:
def test():
    # local var. to test
    x = 'python inside'
    print(x)
test()
print(x)# wont be accessible
----------------------------------
# local x directly nt available
# but we want to access it outside
# solution 1  is to use: return
def test():
    # local var. to test
    x = 'python inside'
    print(x)
    return x
x = test()
print(x)
------------------------------
# Solution 2 is: use global keyword
y = 70
def test():
    # local var. now set as a global
    global x
    x = 'python inside'
    print(x,y)
test()
print(x,y)
-------------------------------
x = 100 #global
def test():
    #print(x)
    # lets try to modify x
    #x = x + 100
    #x = 80
    global x
    x += 2
    print(x)
test()
--------------------------------------
cm = 'Udhhav Thackrey'
def politics():
    #print(cm)
    #print(cm.replace('Udhhav Thackrey','Devendra Fadanvis'))
    # in local scope changing the cm is nt possible
    cm = cm.replace('Udhhav Thackrey','Devendra Fadanvis')
politics()
=======================================
cm = 'Udhhav Thackrey'
def politics():
    #print(cm)
    #print(cm.replace('Udhhav Thackrey','Devendra Fadanvis'))
    # in local scope changing the cm is nt possible
    global cm
    cm = cm.replace('Udhhav Thackrey','Devendra Fadanvis')
    print(cm)
politics()
print(cm)
=====================================
Nonlocal variable:
it is related to nested function
====================================
def outer():

    x = 200 #local to outer
    def inner():
        nonlocal x
        x = 400
        print('Inner:',x)
    inner()
    print('Outer:',x)
outer()
#print(x)
=========================
def sample_1():
    val1 = 'local_1'
    def sample_2():
        val1 = 'local_2'
        print('Sample2:',val1)
    sample_2()
    print('Sample1:',val1)
sample_1()
===========================================
def sample_1():
    val1 = 'local_1'
    def sample_2():
        nonlocal val1
        val1 = 'local_2'
        print('Sample2:',val1)
        def test():
            print(val1)
        test()
    def sample_3():
        print('Sample3:',val1)

    sample_2()
    sample_3()
    print('Sample1:',val1)

sample_1()
=====================================================
Function:
Decorator
Iterator
Generator
Closure
==========================
#eval()
#print(12+45/5*4)
# tk input from user
op = eval(input('Enter expression:'))
print(op)
print(type(op))
"""
# take a list as an input from user
ls = eval(input('Enter a list'))
print(ls)
print(type(ls))
