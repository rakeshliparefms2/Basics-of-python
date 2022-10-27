AZSW	a"""
try:

except:

else:

finally:
========================
How to deal with  exception
--------------------------
a = 5
try:
    print(a)
except:
    print('please assign value to a')
    a = 100
    print(a)
else: # this is optional
    print('No exception')

    for i in range(a):
        print(i)
finally:
    print('Zukga nahi sala')
-------------------------------
How to handle typical exception?
-means we know which exception is gonna happen/occure
-----------------------------
try:
    #print(10/0)
    #print(a)
    #print('1'/3)
    print([].index(10))

except ZeroDivisionError as msg:
    print('Error:',msg)

except NameError as msg:
    print('Error:', msg)
    print('Write further logic here')


except TypeError as msg:
    print('Error:',msg)

# default exception
except:
    print('Default exception')
    try:
        print(e)
    except:
        print('Handled')
-----------------------------
# From where u will get names of all exceptions
----------------
#print(help('builtins'))
print(help(Exception))
----------------
# Lets combine multiple exceptions together
--------------
try:
    #print(10/0)
    #print(a)
    #print('1'/3)
    #print([].index(10))

except (ZeroDivisionError,NameError) as msg:
    print('Error:',msg)
-----------------------
To handle all exceptions under one roof use
Exception as a main class
----------------------------
try:
    #print(10/0)
    #print(a)
    #print('1'/3)
    print([].index(10))

except Exception as msg:
    print('Error:',msg)
------------------------------
- try and except must be there
- use of any one of them is nt allowed
=====================
try:#mandatory
    pass

except:#mandatory

    pass
    try:
        pass
    except:
        pass

else: # optional
    pass

finally: #optional
    pass

=======================
How to generate an exception
use raise keyword
---------------------
# we need to specify condition for which this exceptioon will get raised
#if we want to allow only adults
age = 13
if age <= 18:
    try:
        raise Exception('Error ala re....')
    except:
        print('Error handled')
else:
    print('Welcome to this...')
------------------------------
raise is used to customize exceptions
----------------------
raise NameError('Name error generated')
----------------------------------------
"""































