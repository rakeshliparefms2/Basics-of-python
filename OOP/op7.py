"""
Encapsulation
Means its Data hiding
Members of a program are bind inside a container
-------------------------------------------
class Sample:
    x = 10
    y = 'simba'

    def m1(self):
        pass
# m1() and x,y presents inside a class
# those r nt accessible outside directly
# bcz they are encapsulated inside a container and that container is
# a class
m1()
print(x,y)
s = Sample()
-------------------------------------
Q. What is encapsulation?
---------------------------------------------
Access modifiers: public, private, protected
Public: these variables or methods available anywhere within the program and
to its subclass as well

Private: these variables or methods are available only within the class
outside the class it wont be available

Protected: these variables or methods are available within the same class and to its
subclass


Do we have access modifiers? ==> NO
But we can implement it using _ underscore convention
======================================
class Sample:
    x = 'public'
    _y = 'protected'
    __z = 'private'
    def m1(self):
        print(Sample.__z)
Sample().m1()
class Test:
    print(Sample.x,Sample._y)
    print(Sample._y)
    #print(Sample.__z)
=====================================

class Sample:
    x = 'public' #directly anywhere
    _y = 'protected' # indirectly anywhere
    __z = 'private'
s  = Sample()
print(s.x) #accessible
print(s._y) # accessible indirectly
print(s.__z) # not accessible
======================================
Methods?

class Sample:
    def m1(self):
        print('public method')
    def _m2(self):
        print('Protected method')
    def __m3(self):
        print('Private method')

# try to access using object
s =  Sample()
# public and protected methods will be available
s.m1()
s._m2()
# but private nt
#s.__m3()
=======================================
# Still if i want to access private method outside
then use 'Name Mangling technique'
It is used to store a private variable in dir strcuture
and same is used to access private members outside a class

ex. _className__variableName
    _className__methodName()
============================================
class Sample:
    a = 40
    b = 60
    __x = 'private variable'

    def __m1(self):
        print('Private method')
s = Sample()
#s.__m1()
print(dir(Sample))
print(s._Sample__x)
s._Sample__m1()
==========================================
_m1() __m1()
Q. Differentiate public private protected
Q. Name mangling technique? how to access private member outside a class
########################################################################
Abstraction: Its information hiding
--------------------------------------
Abstraction is associated with class and its methods
Rule:
- In order to make a normal class as an abstract class we need to do 2 things
    1. import ABC(Abstract Base class) class from abc module, then inherit this
    ABC into a normal class
    2. Create an abstract method using asbtractmethod() decorator
"""
from abc import ABC,abstractmethod
class Sample(ABC):

    @abstractmethod
    def m1(self): # an abstract method
        pass
#Rule: we cant create an object of abstract class Sample
class Info(Sample):
    def m1(self):
        print('Implemented Abstract method in Child')
i = Info()
i.m1()
# Rule 2: When we have any abstract method present in abstarct class
# then its implementation must be provided in Child class








