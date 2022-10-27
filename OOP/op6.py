"""
class A:
    def m1(self):
        print('m1 A')

class B(A):
    def m1(self):
        print('m1 B')

class C(B):
    def m2(self):
        super().m1()
        A.m1(self)

c = C()
c.m2()
===============================
class A:
    def m1(self):
        print('m1 A')

class B(A):
    def m1(self):
        print('m1 B')

class C(A):
    def m2(self):
        super().m1()
        A.m1(self)

c = C()
c.m2()

   A
B     C
=========================================
# Multiple inheritance:
We have more than one parent and from these parent we can create a child class
Example:

Mother   Father
     Child

In case of multiple inheritance we must need to folow hierarchy
means class are to be prioritised

This priority we can manage by supplyng parent class sequence
in child class from left to right
-----------------------------
class Mother:
    def m1(self):
        print('Access mother')
    def common(self):
        print('M- common')
class Father:
    def m2(self): print('Access Father')
    def common(self):
        print('F-common')
class Child(Mother,Father):
    def m3(self):
        super().common()
        Father.common(self)
c = Child()
c.m1()
c.m2()
c.common()
c.m3()
=====================================
class Mother:
    def m1(self):
        print('Access mother')
    def common(self):
        print('M- common')
class Father:
    def m2(self): print('Access Father')
    def common(self):
        print('F-common')
class Child(Mother,Father):
    pass
c = Child()
# i want to execute common method from both classes
Father.common(c)
Mother.common(c)
---------------------------------------------

class A:
    def m1(self):
        print('m1-A')
class B:
    def m1(self):
        print('m1-B')
    def m2(self):
        print('m2-B')
class C:
    def m2(self):
        print('m2-C')
class Child(B,A,C):
    pass

ob = Child()
ob.m1() # CLASS B
ob.m2() # class B
==========================
class Mother:
    def m1(self):
        print('Access mother')
    def common(self):
        print('M- common')
class Father:
    def m2(self): print('Access Father')
    def common(self):
        print('F-common')
class Child():
    pass
c = Child()
# i want to execute common method from both classes
# without inheritance also we can access member from other class
Father.common(c)
Mother.common(c)
====================================
class Bank:
    def debit(self):
        print('Debit operation')

#Bank().debit()

#b = Bank()
#b.debit()

sbi = Bank()
Bank.debit(sbi)

hdfc = Bank()
Bank.debit(hdfc)


"""




