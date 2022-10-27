"""
Flow control blocks:
1. Selective/conditional statements: purpose is to run the code
on the basis of a condition

if <condition> # used to test only one condition
here if is a keyword

if else # used to test 2 conditions
if elif else # used to test 3 condition
if elif elif elif....else [elif ladder]
# can test multiple conditions

if hp
    if 8gb
    else 6gb
else
# Nested if: can test dependent conditions
-----------------------------
if is condition based
elif is condition based
else is optional and condition less
we use else to test default/last condition
-----------------------------------
Examples:
=============================
# if <condition>:
# when condition is True, then only ur control will
# enter inside the block
# else it wont[if condition is False]
num = 2
# checking number is +ve or nt
if num > 0:
    print('Good evening')
==================================
# check number is even or odd
num = 27
if num %2 == 0:
    print(num, 'is even')
else:
    print(num,'is odd')
================================
# Test student percentage and assign a class to the student
per = float(input('Enter your percentage:'))
if per >= 75:
    print('You got Distinction')
elif per >= 65:
    print('You got First class')
elif per >= 55:
    print('You got Second class')
elif per >= 45:
    print('You got Pass class')
else:
    print('Sorry you are Fail..')
=================================================
# Q. find out largest number among 3
num1 = 125
num2 = 450
num3 = 10

if (num1 > num2) and (num1 > num3):
    print(num1,'is greater than',num2,'and',num3)
elif num2 > num3:
    print(num2, 'is greater than', num1, 'and', num3)
else:
    print(num3, 'is greater than', num1, 'and', num2)
================================================
# Nested if
# if outer condition is True then inner
# if condition will get checked
mobile = 'samsung'
ram = '1 gb'
if mobile == 'realme':
    if ram == '8 gb':
        print('Price is:Rs.',12000)
    elif ram == '6 gb':
        print('Price is:Rs.', 10500)
    else:
        print('Price is:Rs.', 9000)
else:
    print('Sorry we only sell Realme mobiles ')
===================================================

2. Iterative statements
3. Transfer statements
"""
if 2 == 2:
    pass



