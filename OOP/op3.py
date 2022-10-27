"""
explore self:
it acts as pointer/a reference variable which is responcible for
accessing everything inside class into a method
----------------------------------
class Sample:
    def __init__(self,name,age,salary):
        # make instance variable
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        # fetch details from init and display here
        print(self.name,self.age,self.salary)

s = Sample('A',22,80000)
s.display()
# we can check instance var using __dict__
print(s.__dict__)
-----------------------------------------
If I want to change var. inside a method
- yes it is possible using self
self makes variables as a instance
and instance var. are those whose value changes from object to object
--------------------------------------------
class Sample:
    def __init__(self,name,age,salary):
        # make instance variable
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        # fetch details from init and display here
        self.name= 'Akshay'
        print(self.name,self.age,self.salary)

s = Sample('A',22,80000)
s.display()
# we can check instance var using __dict__
print(s.__dict__)

s2 = Sample('Swapnil',24,78000)
print(s2.__dict__)
# from outside change salary
s2.salary = 98000
print(s2.__dict__)
# swapnil want bonus
s2.bonus = 10000
print(s2.__dict__)
---------------------------------------------
# Types of variables in OOP
- Local: method level
- Global: outside class
- instance: inside instance method
- static/class level variable: inside a class and outside a method
============================================
Local var:
class Sample:
    def m1(self):
        x = 100 #local to m1
        print(x)
    def m2(self):
        #print(x) #wont be available in m2
        pass

s = Sample()
print(s.x) # local var. nt accessible outside a class
-----------------------------------------------
Global variable:
x = 'global'
class Sample:
    print(x)

    def m1(self):
        print(x)

print(x)
s = Sample()
s.m1()
------------------------------
- instance var: inside instance method
----------------------
class Sample:
    def m1(self):
        self.x = 12
    def m2(self):
        print(self.x)

s = Sample()
s.m1()
print(s.x)
s.m2()
---------------------------------
static/class level variable: inside a class and outside a method
------------------------------------
class Sample:
    st = 'static'
    def m1(self):
        #print(st)
        # static var will nt be available inside instance method
        pass
    def m2(self):
        # to access st inside m2 take the help of className ref
        print(Sample.st)
s = Sample()
s.m2()
# can we access static var outside a class
print(s.st)
# use className outside as well to access static var
print(Sample.st)
# className acts as a reference for a static var.
# which works inside a method and outside a class also
-----------------------------------
# lets try to change static variable using className as a ref.
class Bank:
    ifsc = 'SBI76523' # static var
    def m1(self):
        print(Bank.ifsc)
        # lets change ifsc
        Bank.ifsc = 'PNB45678'
print(Bank.ifsc)
b = Bank()
print(b.ifsc)
# now call m1
b.m1()
print(b.ifsc)
----------------------------------------
# lets try to change static variable using self as a ref.
class Bank:
    ifsc = 'SBI76523' # static var
    def m1(self):
        print(Bank.ifsc)
        # lets change ifsc using self
        self.ifsc = 'PNB45678'
print(Bank.ifsc)
b = Bank()
print(b.__dict__)
b.m1()
print(b.__dict__)
# lets check ifsc using object
print(b.ifsc)
print(Bank.ifsc)
-----------------------------------------
class Bank:
    ifsc = 'SBI76523' # static var
    def m1(self):
        print(Bank.ifsc)
        # lets change ifsc using self
        #Bank.ifsc = 'PNB45678'
        self.ifsc = 'PNB45678'
b1 = Bank()
b1.m1()
print(b1.ifsc)

b2 = Bank()
print(b2.ifsc)
-----------------------------
class Bank:
    print('hello')

    def m1(self):
        print('m1 called')
    def m2(self):
        print('m2 called')

b = Bank()
b.m1()
b.m2()
=============================
IQ:
- Differentiate local,global,instance, static variables
- Can we change value of static variable? How?
- self vs object
- method vs constructor
- __init__(self) means what? what is the purpose
- How class gets executed using an object
- How many objects we can create
- Explain call by value and call by reference
- Can we delete instance var?
- How we can use className as a ref. variable
- what is self
"""


