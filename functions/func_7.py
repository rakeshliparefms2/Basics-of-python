"""
Types of Variables
- Local var
---------------------
# local var is available anywhere INSIDE a function
# nt outside
def sample():
    x = 'local'
    print(x)
    def test():
        print(x)
    test()
    print(x)
sample()
print(x)
-----------------------------------
# if local var. we want outside then use return
# with calling function u wil get it
def sample():
    x = 'local'
    print(x)
    def test():
        print(x)
    test()
    return x
x = sample()
print(x)
---------------------------------------
# if local var. we want outside then use return
# with calling function u wil get it
def sample():
    global x
    x = 'local'
    print(x)
    def test():
        print(x)
    test()
sample()
print(x)
------------------------------------------
- Global var
------------------------------
# global variable is available everywhere throughout the program
x = 'global'
def sample():
    print(x)
    def test():
        print(x)
    test()
print(x)
sample()
print(x)

def secret():
    print(x)
    def test_2():
        print(x)
------------------------------------------
- Nonlocal var: is associated with nested function
-----------------------------
def politics():
    cm = 'UT'
    def S_sena():
        nonlocal cm
        cm = 'DF'
        print(cm)
    S_sena()
    #print(cm)
    return cm
cm = politics()
print(cm)
=====================================
VVVVVVIMP
Lets considdr following example:
ls = ['abhijeet','Ashwin','Divya','Harshala','Komal','NITIN']
# i want new list in which all names in CAPITAL
new = []
for nm in ls:
    #print(nm.upper())
    new.append(nm.upper())
print(new)
--------------------
List Comprehension: the above example we can solve using this
to give a small, and concise solution
Syntax:
[expression for val in sequence]
[expression for val in sequence if condition]
Example:
ls = ['abhijeet','Ashwin','Divya','Harshala','Komal','NITIN']
print([nm.upper() for nm in ls])
# its a short way to reduce no. of lines
# best for one liner solution
----------------------------------------------
ls = ['abhijeet','Ashwin','Divya','Harshala','Komal','NITIN']
# i want list of tuple
# [(name,len(name)]
print([(nm.upper(),len(nm)) for nm in ls])
====================================================
ls = ['abhijeet','Ashwin','Divya','Harshala','Komal','NITIN']
# i want list of names whose length is > 5
print([nm for nm in ls if len(nm) > 5])
-------------------------------------------------
ls = ['abhijeet','Ashwin','Divya','Harshala','Komal','NITIN']
# i want list of names whose name contains 'i'
print([nm for nm in ls if 'i' in nm.lower()])
---------------------------------
#fetch even numbers
print([x for x in range(10) if x%2 ==  0])
---------------------------
k = [10,20,30,40,50]
# set a constant value at each place
# take constant as 0
print([0 for i in k])
print(['Constant' for i in k])
============================
k = [10,20,30,40,50]
# add 100 in each element
add = lambda i: i+ 100
print([add(i) for i in k])
print([i+100 for i in k])
==============================
# Use of ternary operator in List comprehension
--------------------------
ls = ['abhijeet','Ashwin','Divya','Harshala','Komal','NITIN']
# Assign Group 1 to the student whose name ends with a
# else will go to Group 2
print(['Group_1' if x.endswith('a') else 'Group_2' for x in ls])
--------------------------------
# flipkart: apply charges for purchase of below 499
# otherwise free delivery
cart = [499,1000,2999,199,154]
print(['Free delivery' if p>499 else '+Rs.40 charges applied'for p in cart])
---------------------------------------------
Dict comprehension:
syntax:
{expression(key:value) for i in sequence}
=================================

ls = ['abhijeet','Ashwin','Divya','Harshala','Komal','NITIN']
# Expected output:{'abhijeet':7.....}
print({len(i): i for i in ls}) # keys cant be duplicate
print({i: len(i) for i in ls})
========================================
"""












