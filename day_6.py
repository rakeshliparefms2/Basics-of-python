












































































































Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # String methods
>>> s = 'raKeSh'
>>> s
'raKeSh'
>>> # convert lower to upper and viceversa
>>> s.swapcase()
'RAkEsH'
>>> #####################
>>> # is type of method
>>> # is methods gives a boolean output
>>> s
'raKeSh'
>>> s.isalpha()
True
>>> s = 'abc123'
>>> s
'abc123'
>>> s.isalnum()
True
>>> s.isalpha()
False
>>> a = '1234'
>>> a.isdigit()
True
>>> s.isdigit()
False
>>> s1 = '   '
>>> s1.isspace()
True
>>> 'hello my number is:9866345123'
'hello my number is:9866345123'
>>> 'hello my number is:9866345123'.split(':')
['hello my number is', '9866345123']
>>> 'hello my number is:9866345123'.split(':')[1]
'9866345123'
>>> 'hello my number is:9866345123'.split(':')[1].isdigit()
True
>>> #################
>>> # Assignment: check other string methods
>>> ####################################
>>> # List:
>>> # How to declare a list?
>>> []
[]
>>> list()
[]
>>> type([])
<class 'list'>
>>> ###########
>>> # Feature of a list
>>> # Background data structure is array
>>> # hence it supports indexing
>>> # it supports slicing
>>> #-------------------
>>> k = [10,20,30,40,50]
>>> k
[10, 20, 30, 40, 50]
>>> type(k)
<class 'list'>
>>> e = [1 2 3 4]
SyntaxError: invalid syntax
>>> # , is used as a seperator
>>> k
[10, 20, 30, 40, 50]
>>> # index
>>> # +ve indexing
>>> k[0]
10
>>> k[2]
30
>>> # -ve indexing
>>> k[-1]
50
>>> k[-4]
20
>>> # Slicing
>>> k[:]
[10, 20, 30, 40, 50]
>>> k[3:]
[40, 50]
>>> k[::-1]
[50, 40, 30, 20, 10]
>>> k[-2:-4:-1]
[40, 30]
>>> ############
>>> # it accepts homo./hetro. values
>>> k
[10, 20, 30, 40, 50]
>>> # in k we have all elements of int type
>>> w = [12,34.5,'python',4+5j]
>>> w
[12, 34.5, 'python', (4+5j)]
>>> ###########
>>> # It preserves sequence order
>>> ###########
>>> # Duplicates are allowed
>>> l = [1,2,1,1,1,1]
>>> l
[1, 2, 1, 1, 1, 1]
>>> ############
>>> # List is Mutable data type
>>> k
[10, 20, 30, 40, 50]
>>> id(k)
1716868357000
>>> # lets change the list
>>> # using index we can change element
>>> k[-1]
50
>>> k[-1] = 500
>>> k
[10, 20, 30, 40, 500]
>>> id(k)
1716868357000
>>> k
[10, 20, 30, 40, 500]
>>> # lets replace 20,30 by 100,20
>>> # 100 and 200
>>> k[1:3]
[20, 30]
>>> k[1:3] = [100,200]
>>> k
[10, 100, 200, 40, 500]
>>> id(k)
1716868357000
>>> # when we are performing the changes is an object, and changes persist in the same
>>> # here new object is not required to save the changes
>>> # then that data type is MUTABLE
>>> # suppose we want to add a new element
>>> k
[10, 100, 200, 40, 500]
>>> k.append('java')
>>> k
[10, 100, 200, 40, 500, 'java']
>>> # append()will add a single element at the end
>>> ###########################
>>> # if we want to check doc. of any method from data structure then use help()
>>> help(k.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> # now if  i want to check all the methods of a list
>>> dir(k)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> k
[10, 100, 200, 40, 500, 'java']
>>> id(k)
1716868357000
>>> # clear
>>> help(k.clear)
Help on built-in function clear:

clear() method of builtins.list instance
    Remove all items from list.

>>> k.clear()
>>> k
[]
>>> id(k)
1716868357000
>>> #####
>>> a = ['A',12,30,50,100,'B']
>>> a
['A', 12, 30, 50, 100, 'B']
>>> id(a)
1716868918920
>>> # copy()
>>> help([].copy)
Help on built-in function copy:

copy() method of builtins.list instance
    Return a shallow copy of the list.

>>> # copy method is used to create a new copy of ur object
>>> # new object will have same elements as that of old one
>>> a
['A', 12, 30, 50, 100, 'B']
>>> b = a.copy()
>>> b
['A', 12, 30, 50, 100, 'B']
>>> id(a)
1716868918920
>>> id(b)
1716868936136
>>> # here id's are different
>>> # means a new object with same element gets created
>>> # lets try to change any of list
>>> b
['A', 12, 30, 50, 100, 'B']
>>> b[0]
'A'
>>> b[0] = 'Amit'
>>> b
['Amit', 12, 30, 50, 100, 'B']
>>> # now check a
>>> a
['A', 12, 30, 50, 100, 'B']
>>> # copy() creates an individual objects using same data
>>> ####################
>>> # i want to create an object with same value and same id
>>> # it is known as Deep copy
>>> c = a
>>> a
['A', 12, 30, 50, 100, 'B']
>>> c
['A', 12, 30, 50, 100, 'B']
>>> id(a)
1716868918920
>>> id(c)
1716868918920
>>> # here we have same id's
>>> # hence changes performed in any of the object persist in both
>>> a
['A', 12, 30, 50, 100, 'B']
>>> c
['A', 12, 30, 50, 100, 'B']
>>> c[-1]
'B'
>>> c[-1] = 'Baban'
>>> c
['A', 12, 30, 50, 100, 'Baban']
>>> a
['A', 12, 30, 50, 100, 'Baban']
>>> a[2]
30
>>> a[2] = 'C#'
>>> a
['A', 12, 'C#', 50, 100, 'Baban']
>>> #check c
>>> c
['A', 12, 'C#', 50, 100, 'Baban']
>>> # changes persist in both object bcz of same id
>>> ##################
>>> # qQ. What is shallow and deep copy?
>>> # what is difference betwn them?
>>> ###############
>>> #Recap
>>> # shallow copy
>>> s1 = ['amit','dinesh','suresh']
>>> s1
['amit', 'dinesh', 'suresh']
>>> id(s1)
1716868917448
>>> #shallow copy
>>> s2 = s1.copy()
>>> s2
['amit', 'dinesh', 'suresh']
>>> id(s2)
1716868939208
>>> # deep copy
>>> s3 = s1
>>> s3
['amit', 'dinesh', 'suresh']
>>> id(s3)
1716868917448
>>> s3[-1]
'suresh'
>>> s3[-1] = 'ramesh'
>>> s3
['amit', 'dinesh', 'ramesh']
>>> s1
['amit', 'dinesh', 'ramesh']
>>> s2 #shallow copy
['amit', 'dinesh', 'suresh']
>>> 
