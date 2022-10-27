"""
OOP:
class class_name:
    properties
    behaviour
--------------------------------
Convention
Use class name in Title case if its a single word
class Bank:
    pass

if its a combi. of 2 words then use CamelCase
class BankDetails:
    pass
========================================================
Recall:
class
class calling
object
--------------------------
class calling--> Constructor calling
-----------------------------------
class Bank:
    ifcs = 'BKID2324'
    def deposit(self):
        pass
    def withdraw(self):
        pass
b = Bank()
b.deposit()
# constructor: is used to allocate a memory
# Feature:
# Constructor has same name as that of class Name
# it allocates a memory
# Constructor can be empty or parameterized
print(dir())
------------------------------------------
# Create an empty constructor
class Sample:
    def __init__(self): #initializes memory
        print('Constructor method')
    def display(self):
        pass
Sample()
Sample()
# Q. what is constructor
# Q. what is __init__
# Q. differentiate method vs constructor
Sample().__init__()
------------------------------------
Parameterized constructor
----------------------
class Sample:
    def __init__(self,name,age):
        print('Name is:',name,'& age is:',age)

Sample('Priya',25)
Sample(24,'Renuka')
# above are positional args.
----------------------------
Use keyword argument
------------------------
class Sample:
    def __init__(self,name,age):
        print('Name is:',name,'& age is:',age)

#Sample('Priya',25)
Sample(age=24,name='Renuka')
# above arg type is keyword agrs..
=========================================
Use default args
-------------------------
class Sample:
    def __init__(self,name,age=18):
        print('Name is:',name,'& age is:',age)

# default age values is set to 18
Sample(name='Renuka')
Sample('Suhas',26)
--------------------------------
*args , **kwargs: Variable length argument
class Sample:
    def __init__(self,*args):
        print(args)

# default age values is set to 18
Sample('Dipti',22)
Sample('Suhas',26,'Pune')
-----------------------------------
class Sample:
    def __init__(self,**kwargs):
        print(kwargs)

# default age values is set to 18
Sample(name='Dipti',age=22)
Sample(name='Suhas',age=26,place='Pune')
Sample()
-----------------------------------
Is the init only option to supply arguments???
Answer is NO
We can suppply arguments to any normal method
---------------------------------------------
class Sample:
    def info(self,roll_no,name,std):
        print(roll_no,name,std,sep='\n')

Sample().info(12,'Ashwin',10)
--------------------------------------------
class Sample:
    def info(self,roll_no,name):
        # roll_no and name are local to info
        # we need to make them instance variables
        # using self we can make it
        self.roll_no = roll_no
        #(instance)    (local)
        self.name = name

    def display(self):
        print('Details provide by user:')
        print(self.roll_no)
        print(self.name)

s = Sample()
s.info(10,'A')
s.display()
# s--> Sample()--> info--> display()

#Sample().info(100,'abc')
#Sample().display()

# right way
#Aap-->Father--->Yameen-->Money
#object-->Constructor--> info-->display

# wrong way
#Constructor--> info
#Constructor---->display
------------------------------------------
self:
it works like a reference variable inside a class
it is active only inside a method
it wont work outside the method and class

Inside a method we can access and call any of the member of a class
------------------------
Task we can perform using self
1. add new instance variable using self
-------------------------------------------
class Test:
    pin = 1234
    def register(self,name):
        print(name) #name is local to register method
        self.name = name


    def task(self):
        print('welcome',self.name,'to a task')
        print(Test.pin)
        # className acts a a ref for variables declared inside a class
        # and outside a method
    def task2(self):
        print(self.name)
        # lets add new variables
        # we add using self
        self.age = 45
        self.pincode = 411008

t = Test()
t.register('XYZ')
t.task()
t.task2()
print(t.__dict__)
#print(t.age)

# We have 3 reference variables
# - self: inside a class+method
# - object: outside a class
# - className: inside a class method
------------------------------------------------
"""






