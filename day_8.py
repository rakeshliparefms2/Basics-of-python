Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # List remaining methods
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> # sort(): default ascending order
>>> p = [23,100,9,3,45,67,88,100]
>>> p
[23, 100, 9, 3, 45, 67, 88, 100]
>>> help(p.sort)
Help on built-in function sort:

sort(*, key=None, reverse=False) method of builtins.list instance
    Stable sort *IN PLACE*.

>>> p.sort(key=min)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    p.sort(key=min)
TypeError: 'int' object is not iterable
>>> p
[23, 100, 9, 3, 45, 67, 88, 100]
>>> min(p)
3
>>> max(p)
100
>>> min(23)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    min(23)
TypeError: 'int' object is not iterable
>>> d = ['ram','Abhijeet','ashok','nilesh','Abhiram']
>>> d
['ram', 'Abhijeet', 'ashok', 'nilesh', 'Abhiram']
>>> len(d)
5
>>> d.sort(key=len)
>>> d
['ram', 'ashok', 'nilesh', 'Abhiram', 'Abhijeet']
>>> # sorted the list in ascending order
>>> ##########################
>>> # Tuple
>>> # syntax: ()
>>> ()
()
>>> type(())
<class 'tuple'>
>>> # create an empty  tuple
>>> ()
()
>>> tuple()
()
>>> a = ()
>>> a
()
>>> type(a)
<class 'tuple'>
>>> b = tuple()
>>> b
()
>>> type(b)
<class 'tuple'>
>>> #############
>>> # Features: It has almost all features same as that of List
>>> # except one
>>> # List is Mutable &
>>> # Tuple is Immutable
>>> #######################
>>> # why tuple is immutable???
>>> t = (10,20,30,40)
>>> # aasignment: check indexing and slicing over a tuple
>>> t
(10, 20, 30, 40)
>>> # lets try to change 40 to 400
>>> t[-1]
40
>>> t[-1] = 400
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    t[-1] = 400
TypeError: 'tuple' object does not support item assignment
>>> ##############
>>> # lets check method supported by tuple
>>> dir(t)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> # it contains only 2 methods:'count', 'index'
>>>  # which are nt used for perfroming manipulation
>>> # check method of a list
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> # list many methods are used for direct manipulation of data
>>> # hence list is mutable and tuple is immutable
>>> #################################
>>> # Q. Interview
>>> t1 = (1,2,3)
>>> t1
(1, 2, 3)
>>> t2 = (5,6,7)
>>> t2
(5, 6, 7)
>>> t1 + t2
(1, 2, 3, 5, 6, 7)
>>> t1
(1, 2, 3)
>>> t2
(5, 6, 7)
>>> # Q.  which one is better????
>>> # list or tuple???
>>> # it depends on the requirement of a business
>>> ####################
>>> # Q. why list take more memory than tuple
>>> # Example
>>> t1
(1, 2, 3)
>>> l1 = [1,2,3]
>>> l1
[1, 2, 3]
>>> # now check the memory for bot
>>> # both
>>> t1.__sizeof__()
48
>>> l1.__sizeof__()
64
>>> # what is the reason of above case?????
>>> # which one is faster tuple of list???
>>> ########################################
>>> # Set:
>>> # Packing and Unpacking of tuple: VVIMP
>>> 10
10
>>> type(10)
<class 'int'>
>>> 10,
(10,)
>>> type(10,)
<class 'int'>
>>> type((10,))
<class 'tuple'>
>>> # default comma separated values in python are Tuple
>>> 10,20,30
(10, 20, 30)
>>> 'A','F','G'
('A', 'F', 'G')
>>> # Paacking: grouping multiple objects in a single identifier
>>> 'k','g',f'
SyntaxError: EOL while scanning string literal
>>> 'k','g','f'
('k', 'g', 'f')
>>> film = 'k','g','f'
>>> film
('k', 'g', 'f')
>>> #rx:2
>>> f = 12.3,45.55,60.77
>>> f
(12.3, 45.55, 60.77)
>>> # Unpacking: opposite of packing
>>> # to unfold packed values, we need multiple identifiers
>>> film
('k', 'g', 'f')
>>> # how many elements present in film
>>> len(film)
3
>>> x,y,z = film # her k,g,f will be assigned to x,y,z resp.
>>> x
'k'
>>> y
'g'
>>> z
'f'
>>> ###########
>>> p,q,q = 100,200,300
>>> p
100
>>> q
300
>>> q = 200
>>> q = 300
>>> q
300
>>> p1,q1,r1 = 100,200,300
>>> p1
100
>>> q1
200
>>> r1
300
>>> ############
>>> ##############################
>>> # SET
>>> # Syntax:
>>> # Empty set
>>> s = set()
>>> s
set()
>>> type(s)
<class 'set'>
>>> ############
>>> # Syntax:
>>> s = {1,2,3,4,5}
>>> s
{1, 2, 3, 4, 5}
>>> type(s)
<class 'set'>
>>> a = {'A','B','C'}
>>> a
{'B', 'A', 'C'}
>>> # Set doesnt preserve sequence order
>>> #########
>>> d = {1,2,'A','B'}
>>> d
{1, 2, 'B', 'A'}
>>> # it suppports homo. and hetro type of data
>>> #########
>>> # duplicates are not allowed
>>> f = {1,2,3,4,1,1,1,1,1,1,1}
>>> f
{1, 2, 3, 4}
>>> r = {1,2,2,2,2,3,3,3,1,1,1,1,}
>>> r
{1, 2, 3}
>>> e = {12,0,1,'2','23'}
>>> e
{0, 1, '2', 12, '23'}
>>> ##############
>>> # Indexing is not supported
>>> s
{1, 2, 3, 4, 5}
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    s[0]
TypeError: 'set' object does not support indexing
>>> # no slicing
>>> s[::-1]
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    s[::-1]
TypeError: 'set' object is not subscriptable
>>> # No array data structure
>>> # Background data struucture is a HASH TABLE
>>> ###############
>>> # Set is Mutable in nature
>>> s
{1, 2, 3, 4, 5}
>>> id(s)
2141431803976
>>> s.update({10,20,30})
>>> s
{1, 2, 3, 4, 5, 10, 20, 30}
>>> s.update({'A'})
>>> s
{1, 2, 3, 4, 5, 10, 20, 'A', 30}
>>> ###########
>>> # can we use empty {} to create an empty set
>>> {}
{}
>>> type({})
<class 'dict'>
>>> {()}
{()}
>>> type({()})
<class 'set'>
>>> type({[]})
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    type({[]})
TypeError: unhashable type: 'list'
>>> t1
(1, 2, 3)
>>> s
{1, 2, 3, 4, 5, 10, 20, 'A', 30}
>>> d = set()
>>> d
set()
>>> d.update(t1)
>>> d
{1, 2, 3}
>>> # www.programiz.com
>>> 
