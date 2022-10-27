"""
3. Transfer statement: loop control statements
- break
used to break a loop
breaks current execution flow
and exit from the loop
####
break only works inside the block
===================
for i in range(7):
    #print(i)
    if i == 4:
        break
    else:
        print(i)
=============================
temp = [12,30,23,10,15,22,35,11,7,24,26,30]
for i in temp:
    if i == 35:
        break
    else:
        print('current temp. is:',i)
====================================
temp = [12,30,23,10,15,22,35,11,7,24,26,30]
for i in temp:
    if i == 35 :
        continue
    else:
        print('current temp. is:',i)
=====================================
#test more than 1 condition
temp = [12,30,23,10,15,22,35,11,7,24,26,30]
for i in temp:
    if (i == 35) or (i<=10) :
        continue
    else:
        print('current temp. is:',i)
===================================
# flipkart cart scenario using continue
cart = [1999,399,499,650,800,2500,2999,450,299,199,99]
for i in cart:
    if i < 500: #product less than 500
        print('Product price is Rs:', i, 'Delivery charges applied')
        continue #it skip the value at given condition
    else: #product greater than 500
        print('Product price is Rs:',i,'Free delivery applicable')
=======================================
Difference between break and continue????
for i in range(5):
    if i == 3:
        break
    else:
        print(i)
print('-------------------')
for i in range(5):
    if i == 3:
        continue
    else:
        print(i)
=========================================
- continue:
it skips the value at given condition but continues loop
=================================================
- pass: null statement, used to create an empty block
if True:
    pass
for i in range(6):
    pass
========================================
"""


