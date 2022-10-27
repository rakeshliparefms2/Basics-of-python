Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Operators in Python
>>> # used to perform some operations
>>> # Arithmatic operator:
>>> # + - * / % // **
>>> 12 + 20
32
>>> 20 - 10
10
>>> 3 * 4
12
>>> 3/4
0.75
>>> # % mod operator: it gives remainder
>>> 23 % 10
3
>>> 4 % 2
0
>>> # // floor division
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> 4/5
0.8
>>> 4//5
0
>>> 5/3
1.6666666666666667
>>> 5//3
1
>>> # ** exponential/ power of operator
>>> 2 ** 4
16
>>> 3 ** 2
9
>>> 25 ** 2
625
>>> ##########################
>>> # Assignment operator
>>> a = 100
>>> a
100
>>> a + 100
200
>>> a
100
>>> a += 100 # a = a + 100
>>> a
200
>>> a-= 50
>>> a
150
>>> a *= 2
>>> a
300
>>> a /= 10
>>> a
30.0
>>> a **= 2
>>> a
900.0
>>> a //= 10
>>> a
90.0
>>> 900//10
90
>>> ######################
>>> # Relational operator/ COnditional operators
>>> # These operators alwways results boolean output[True, False]
>>> # < > <= >= == !=
>>> 1 < 0
False
>>> 1 ==  10
False
>>> 'python' == 'Python'
False
>>> 'Python' == 'Python'
True
>>> 34 != 23
True
>>> ##############################
>>> # Logical Operators
>>> # associated with conditional checking
>>> # here we need the help of comparison operators
>>> # 3 options: and or not
>>> # It is based on Truth Table
>>> # and Truth table
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> name = 'Snehal'
>>> name
'Snehal'
>>> age = 23
>>> age
23
>>> # nw check the conditions
>>> name == 'Snehal'
True
>>> name == 'Sneha'
False
>>> age == 40
False
>>> # True and True
>>> name == 'Snehal' and age == 23
True
>>> name == 'Shital' and age == 23
False
>>> name == 'Snehal' and age == 34
False
>>> name == 'Shital' and age == 3
False
>>> # value of True is 1
>>> int(True)
1
>>> # value of False is 0
>>> int(False)
0
>>> 10 and 20
20
>>> # x and y
>>> # if ur X is True then return Y
>>> # False means 0,None, ''
>>> # if ur X is False then return X
>>> 0 and 33
0
>>> False and 'python'
False
>>> ########################
>>> # or operator
>>> 10 and 0
0
>>> False and 10
False
>>> 'sagar' and 'pramod'
'pramod'
>>> '' and 'pramod'
''
>>> None and 'pramod'
>>> None
>>> 'sagar' and 10
10
>>> 'sagar' and 93457345
93457345
>>> #####################################
>>> # or operator
>>> name
'Snehal'
>>> age
23
>>> name == 'Snehal' or age == 90
True
>>> name == 'ehal' or age == 90
False
>>> ###########################
>>> # Not: negation
>>> not True
False
>>> not False
True
>>> not name == 'Vikas'
True
>>> not age == 23
False
>>> age == 23
True
>>> ##############################
>>> # Membership
>>> # it  checks either an element is a member of a sequence or not
>>> 'hema' in 'hema malini'
True
>>> # it has 2 types: in , not it
>>> 'jaya' in 'hema malini'
False
>>> # it results boolean output
>>> 12 in [10,11,12,13]
True
>>> 120 in [10,11,12,13]
False
>>> 120 not in [10,11,12,13]
True
>>> 'abc' not in 'prq'
True
>>> #######################
>>> # Identity operator
>>> # its check id / address of an objects
>>> # if address matches then it results True
>>> # otherwise False
>>> # 2 types:
>>> # is , is not
>>> #-----------
>>> 10 is 10
True
>>> 'py' is 'Py'
False
>>> id('py')
2945141591880
>>> id('Py')
2945181503928
>>> 'py' is not 'Py'
True
>>> #############################
>>> # interview question
>>> 10 ==  10
True
>>> 10 == 10.0
True
>>> 10 is 10
True
>>> 10 is 10.0
False
>>> id(10)
140723146511680
>>> id(10.0)
2945141292080
>>> # id's are different hence False
>>> # Content equality and address equality
>>> 10 == 10.0
True
>>> # it does contents equality
>>> 10 is 10.0
False
>>> # it does address equality
>>> # == is content equality
>>> # is : address equality
>>> 
