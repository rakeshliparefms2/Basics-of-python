Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # List methods:
>>> # how to check the methods of list==> using dir()
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> k = [10,20,10,30,40,10]
>>> k
[10, 20, 10, 30, 40, 10]
>>> # count
>>> help(k.count)
Help on built-in function count:

count(value, /) method of builtins.list instance
    Return number of occurrences of value.

>>> k.count(10)
3
>>> k.count(100)
0
>>> ########
>>> # extend()
>>> help(k.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> # iterable???
>>> # it means a collection of multiple elements,objects
>>> # on which we can perform iterations
>>> k
[10, 20, 10, 30, 40, 10]
>>> # examples of iterable: string,list,tuple,set,range,dict
>>> k
[10, 20, 10, 30, 40, 10]
>>> k.extend([1,2,3])
>>> k
[10, 20, 10, 30, 40, 10, 1, 2, 3]
>>> k.extend(['A','B'])
>>> k
[10, 20, 10, 30, 40, 10, 1, 2, 3, 'A', 'B']
>>> ##########
>>> # what is difference between append and extend????
>>> help([].append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> help([].extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> r = []
>>> r
[]
>>> r.append(1)
>>> r
[1]
>>> r.extend(2)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    r.extend(2)
TypeError: 'int' object is not iterable
>>> r.extend([2])
>>> r
[1, 2]
>>> # see now actual difference
>>> # if we try to add iterable using append
>>> # it will add complete ietrable as a single element
>>> r
[1, 2]
>>> r.append('Shital')
>>> r
[1, 2, 'Shital']
>>> # if we try to add same using extend then it will add each char/block
>>> # separatly
>>> r.extend('Shital')
>>> r
[1, 2, 'Shital', 'S', 'h', 'i', 't', 'a', 'l']
>>> ####### Example 2
>>> r
[1, 2, 'Shital', 'S', 'h', 'i', 't', 'a', 'l']
>>> r.append([10,20])
>>> r
[1, 2, 'Shital', 'S', 'h', 'i', 't', 'a', 'l', [10, 20]]
>>> r.extend([10,20])
>>> r
[1, 2, 'Shital', 'S', 'h', 'i', 't', 'a', 'l', [10, 20], 10, 20]
>>> # extend does not accepts int,float,complex,boolean
>>> r.extend(34.66)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    r.extend(34.66)
TypeError: 'float' object is not iterable
>>> r.extend(True)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    r.extend(True)
TypeError: 'bool' object is not iterable
>>> ######################
>>> # List of list
>>> g = [[10,20],[40,50]]
>>> g
[[10, 20], [40, 50]]
>>> g[0]
[10, 20]
>>> g[-1]
[40, 50]
>>> # change 40 to 400
>>> g[-1][0]
40
>>> g[-1][0] = 400
>>> g
[[10, 20], [400, 50]]
>>> # lets add name amruta in 10,20 list
>>> g
[[10, 20], [400, 50]]
>>> g[0]
[10, 20]
>>> g[0].append('Amruta')
>>> g
[[10, 20, 'Amruta'], [400, 50]]
>>> ##########
>>> help(k.index)
Help on built-in function index:

index(value, start=0, stop=9223372036854775807, /) method of builtins.list instance
    Return first index of value.
    
    Raises ValueError if the value is not present.

>>> k
[10, 20, 10, 30, 40, 10, 1, 2, 3, 'A', 'B']
>>> k.index('A')
9
>>> k.index(10)
0
>>> k.index(400)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    k.index(400)
ValueError: 400 is not in list
>>> ###############
>>> help(k.insert)
Help on built-in function insert:

insert(index, object, /) method of builtins.list instance
    Insert object before index.

>>> k
[10, 20, 10, 30, 40, 10, 1, 2, 3, 'A', 'B']
>>> # add 500 between 30 and 40
>>> k[4]
40
>>> k.insert(4,500)
>>> k
[10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 'B']
>>> # Interview question
>>> # add element 90 between A and B using -ve indexing
>>> k.insert(-1,90)
>>> k
[10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 90, 'B']
>>> # after B i want to add Hello using insert only
>>> k.insert(0,'Hello')
>>> k
['Hello', 10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 90, 'B']
>>> len(k)
14
>>> k.insert(14,'Hello')
>>> k
['Hello', 10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 90, 'B', 'Hello']
>>> len)k)
SyntaxError: invalid syntax
>>> len(k)
15
>>> k[-15]
'Hello'
>>> ####################
>>> help(k.pop)
Help on built-in function pop:

pop(index=-1, /) method of builtins.list instance
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.

>>> k
['Hello', 10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 90, 'B', 'Hello']
>>> k.pop()
'Hello'
>>> k
['Hello', 10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 90, 'B']
>>> k.pop()
'B'
>>> k
['Hello', 10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 90]
>>> # we can remove one element at a time
>>> # remove element at specific index
>>> # remove hello
>>> k.pop(0)
'Hello'
>>> k
[10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 'A', 90]
>>> # remove A
>>> k.pop(-2)
'A'
>>> k
[10, 20, 10, 30, 500, 40, 10, 1, 2, 3, 90]
>>> k.pop()
90
>>> k
[10, 20, 10, 30, 500, 40, 10, 1, 2, 3]
>>> # if element nt present in the list and we try to remove it
>>> k.pop(56)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    k.pop(56)
IndexError: pop index out of range
>>> ###############
>>> # pop is used to remove one element at a time
>>> # it can not remove multiple elements
>>> #####################
>>> # if we want to remove element by giving element as an input
>>> # then use remove()
>>> help(k.remove)
Help on built-in function remove:

remove(value, /) method of builtins.list instance
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.

>>> k
[10, 20, 10, 30, 500, 40, 10, 1, 2, 3]
>>> k.remove(10)
>>> k
[20, 10, 30, 500, 40, 10, 1, 2, 3]
>>> k.remove(3)
>>> # remove is value based
>>> # pop is index based
>>> # Q. difference between remove and pop
>>> #--------------------
>>> # pop removes and return an element
>>> # remove doesnt return an element
>>> #----------------------
>>> # pop() default removes last element
>>> # remove() needs value always
>>> k
[20, 10, 30, 500, 40, 10, 1, 2]
>>> k.remove()
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    k.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> k.pop()
2
>>> #--------------------------------
>>> help(k.reverse)
Help on built-in function reverse:

reverse() method of builtins.list instance
    Reverse *IN PLACE*.

>>> #Reverse *IN PLACE*. inplace means permanent change
>>> k
[20, 10, 30, 500, 40, 10, 1]
>>> k.reverse()
>>> k
[1, 10, 40, 500, 30, 10, 20]
>>> k.reverse()
>>> k
[20, 10, 30, 500, 40, 10, 1]
>>> # this reverse is permenant
>>> # if we want temp. reverse then use slicing
>>> k
[20, 10, 30, 500, 40, 10, 1]
>>> k[::-1]
[1, 10, 40, 500, 30, 10, 20]
>>> # using builtin function reversed() we can reverse the sequence
>>> k
[20, 10, 30, 500, 40, 10, 1]
>>> reversed(k) #it give output in the form of object
<list_reverseiterator object at 0x00000247F1D40240>
>>> # when we get an output in the form of object, then to see actual values
>>> # u need to convert it into another data type
>>> list(reversed(k))
[1, 10, 40, 500, 30, 10, 20]
>>> # Q. differentiate between reverse() and reversed()
>>> # reverse():is a method of list
>>> # reversed() is built in function (python)
>>> #----------------------
>>> # reveres(): in -place
>>> # reversed(): temp.
>>> k
[20, 10, 30, 500, 40, 10, 1]
>>> # reverse() : does not return anything
>>> # reversed(): returns output in the form of object
>>> #------------------------
>>> # sort()
>>> help(k.sort)
Help on built-in function sort:

sort(*, key=None, reverse=False) method of builtins.list instance
    Stable sort *IN PLACE*.

>>> d = [10,99,34,0,4,34,56,1,3]
>>> d
[10, 99, 34, 0, 4, 34, 56, 1, 3]
>>> d.sort()
>>> d
[0, 1, 3, 4, 10, 34, 34, 56, 99]
>>> # sort in ascending order default
>>> # but if i want to sort in descending order
>>> # use reverse = True
>>> d.sort(reverse=True)
>>> d
[99, 56, 34, 34, 10, 4, 3, 1, 0]
>>> h = [12,0,'A',300,'Z','B']
>>> h
[12, 0, 'A', 300, 'Z', 'B']
>>> h.sort()
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    h.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> o = ['Z','C','G','A','M']
>>> o
['Z', 'C', 'G', 'A', 'M']
>>> o.sort()
>>> o
['A', 'C', 'G', 'M', 'Z']
>>> 
