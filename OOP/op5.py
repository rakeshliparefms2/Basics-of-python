"""
OOP Properties:
Pillars of OOP
- Inheritance
- Encapsulation
- Abstraction
- Polymorphism
-------------------------------
Inheritance:
Building a parent and child relationship
in which we have basically 2 classes
1. Parent class ( Base/root class)
2. Child class ( Derived class)
---------------------------
There are 4 different types of Inheritance:
- Simple/single inheritance
- Multilevel inheritance
- Multiple inheritance
- Hybrid
=====================================
1. Simple inheritance:
-in which we wil have only one parent and one child
- to build a relation we need to inherit Father class in child class
=============================
class Father:
    x = 100
    def money(self):
        print('Money of Father')
class Child(Father):
    pass

c = Child()
c.money()
print(c.x)
==================================
# suppose child class only has money method
# and Father class has x, car method
class Father:
    x = 100
    def car(self):
        print('Fathers car')

class Child(Father):
    def money(self):
        print('Money of Child')

c = Child()
c.money()
c.car()
=========================================
# Multilevel inheritance

class Central_gov: # suepr_parent
    def funds(self):
        print("central gov funds")
class State_gov(Central_gov): # Parent
    def s_funds(self):
        print('State gov fund')
    def funds(self):
        print('Central fund in State')
        super().funds()

class Local_gov(State_gov): # child
    pass
l = Local_gov()
l.funds()
l.s_funds()
--------------------------------------
Examples:
Multilevel inheritance:
Super Parent

Parent

child

Multiple inheritance

Father Mother
    child
==============================
# we can use a super() to access members of a super parent or parent
# if tht method or member is already present
# super we can use inside a method
class PM:
    def help(self):
        print('Help from PM')

class CM(PM):
    def help(self):
        print('Help from CM')
        #super().help()
        super(CM, self).help()
class MLA(CM):
    def fund(self):
        print('MLA fund')


m = MLA()
m.fund()
m.help()
=======================================
VVIMP:
Meth-od overriding:
If child and parent contains a method with same name,
so method in child overrides method in parent
and method in parent overriden in child

Overriding is completely a part of inheritance
without inheritance its nt possible
"""
class Father:
    def info(self):
        print('Father info')

class Child(Father):
    def info(self):
        print('Self.info')
        super().
c = Child()
c.info()










