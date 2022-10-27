"""
def function(parameters):
    ...
    ..
    ..
    return
# Parameters and return are optional
----------------------------------------------
4. Variable length argument:
-----------------
# WAP to do the addition of variable numbers
def add(a,b):
    print(a+b)
add(10,20)
add()
add(1,2,3)
add(10,20,30,40)
=========================
We cant pass multiple values in above case as declaation only
contains 2 parameters(a,b)
So above issue we can solve using variable length arguments.
---------------------------------------------------------
# WAP to do the addition of variable numbers
def add(*args): # instead of args we can use any other valid identifier
    print(args)
add(10,20)
add()
add(1,2,3)
add(10,20,30,40)
# when we supply variable length Positional arguments
# then it returns Tuple always
====================================
# supply following inputs to a function func
and get the addition of elements
func(10,20)
func(1,2,3,-5)
func()
func(1,2,3,4,5,6)
===================================
def func(*n):
    print(sum(n))
func(10,20)
func(1,2,3,-5)
func()
func(1,2,3,4,5,6)
=============================
# WAP to fetch only characters from function calling
def func(*n):
    for i in n:
        if str(i).isalpha():
            print(i,end=' ')
    print()
func('X',10,'A')
func(1,'V',3,'N')
===============================
Variable length keyword arguments
-----------------------
def func(**kwargs):
    print(kwargs)
func()
func(name='Python',age=23)
func(roll_no= 12,name='Abhi',marks= 80)
# kwargs gives a dict always
func(a =10,b=20,c=30)
=================================
def func(**kwargs):
    print(kwargs.values())
func()
func(name='Python',age=23)
func(roll_no= 12,name='Abhi',marks= 80)
# kwargs gives a dict always
func(a =10,b=20,c=30)
===============================================
VVIMP Q:
What is *args and **kwargs?
Differentiate both???
##############################################
Return statement:
return is a keyword
---------------------------
# a function without return
def add():
    print(100+200)

result = add()
print(result)
# When ur function does nt return anything
# then it returns ==> None means nothing
-------------------------------------
def add():
    #print(100+200)
    return 100 + 200

result = add()
print(result)
# When ur function does nt return anything
# then it returns ==> None means nothing
===========================
def kharacha(paise):
    paise -= 500 # purchased 500 rs Tshrt
    return paise
rem = kharacha(1000)
print(rem)
==========================
# How many values we can return
-> n number
===================================
def sample(a,b):
    return a,b,a+b
    # return brings the value outside
    # only single return is allowed
print(sample(20,40)) #packing is performed here
#x,y,z = sample(1,2) #unpacking
p = sample(1,2)
print(p)
#print(x,y,z,sep='--')
============================
def sample(a,b):
    return a,b,a+b
    # return brings the value outside
    # only single return is allowed
print(sample(20,40)) #packing is performed here
#x,y,z = sample(1,2) #unpacking
p = sample(1,2)
print(p)
#print(x,y,z,sep='--')
====================================
def test(fever):
    if fever >96:
        return 'positive'
    else:
        return 'negative'
result =test(70)
if result == 'positive':
    print('14 days isolation')
else:
    print('Take medicine and rest+ Home isolation')
==================================================
"""



