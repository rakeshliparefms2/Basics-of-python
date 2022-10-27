Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # SET
>>> set()
set()
>>> s = {1,2,1,3,1}
>>> s
{1, 2, 3}
>>> # Set is mutable data type
>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> s
{1, 2, 3}
>>> s.add(10)
>>> s
{10, 1, 2, 3}
>>> # insertion order is nt preserved
>>> s.add('KGF')
>>> s
{1, 2, 3, 10, 'KGF'}
>>> # bcz its background data structure is Hash Table
>>> # a = {23,4,10,79,56,10,4}
>>> # for this working of Hash table
>>> # lets assume hash function is mod %
>>> 23 % 10
3
>>> 4 % 10
4
>>> 10 % 10
0
>>> 79 % 10
9
>>> 56 % 10
6
>>> ########################
>>> # Methods of set
>>> s
{1, 2, 3, 10, 'KGF'}
>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> # SET operations
>>> # intersection
>>> # Fetch common elements from 2 sets
>>> s1 = {1,2,3}
>>> s1
{1, 2, 3}
>>> s2 = {2,3,4,5}
>>> s2
{2, 3, 4, 5}
>>> s1.intersection(s2)
{2, 3}
>>> ms1 = 'this is sample program'
>>> ms2 = 'program is simple'
>>> # find out common contents from ms1 and ms2
>>> # COnveert string to set
>>> ms_1 = set(ms1)
>>> ms_1
{' ', 'e', 'g', 'r', 'm', 'p', 'i', 'l', 's', 'o', 'h', 't', 'a'}
>>> # here it gives characters
>>> # but we want  words
>>> # so need to convert into list of string
>>> ms1.split()
['this', 'is', 'sample', 'program']
>>> ms_1 = set(ms1.split())
>>> ms_1
{'is', 'program', 'sample', 'this'}
>>> ms_2 = set(ms2.split())
>>> ms_2
{'is', 'program', 'simple'}
>>> ms_1.intersection(ms_2)
{'is', 'program'}
>>> ####################
>>> # union
>>> # Take all elements from both set, without duplicates
>>> s1
{1, 2, 3}
>>> s2
{2, 3, 4, 5}
>>> s1.union(s2)
{1, 2, 3, 4, 5}
>>> ms_1.union(ms_2)
{'is', 'program', 'sample', 'this', 'simple'}
>>> ################
>>> # difference
>>> # fetch uncommon elements from set 1
>>> s1
{1, 2, 3}
>>> s2
{2, 3, 4, 5}
>>> s1.difference(s2)
{1}
>>> s2.difference(s1)
{4, 5}
>>> ##########
>>> # symmetric difference
>>> # fetch uncommon elements from set 1 and set 2 as well
>>> s1.symmetric_difference(s2)
{1, 4, 5}
>>> ####################################
>>> # Using operator if we want to apply set operations
>>> s1
{1, 2, 3}
s
>>> s2
{2, 3, 4, 5}
>>> s1 & s2
{2, 3}
>>> # & : intersection
>>> #######
>>> s1 | s2
{1, 2, 3, 4, 5}
>>> # | gives union
>>> ##########
>>> s1 - s2
{1}
>>> # - gives : difference
>>> s1.difference(s2)
{1}
>>> # Assignment : which operator is used for symmetric difference???
>>> ##################
>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> # if we want to perform set operation and we want to store result in set 1
>>> # then go with update options
>>> s
{1, 2, 3, 10, 'KGF'}
>>> id(s)
2687694096648
>>> s1
{1, 2, 3}
>>> # now use difference_update option
>>> s.difference(s1) #uncommon
{10, 'KGF'}
>>> s
{1, 2, 3, 10, 'KGF'}
>>> s1
{1, 2, 3}
>>> # no any set gets changed
>>> s.difference_update(s1)
>>> s
{10, 'KGF'}
>>> # union
>>> s
{10, 'KGF'}
>>> s1
{1, 2, 3}
>>> s.update(s1)
>>> s
{2, 1, 3, 10, 'KGF'}
>>> ##################
>>> help(s.update)
Help on built-in function update:

update(...) method of builtins.set instance
    Update a set with the union of itself and others.

>>> s
{2, 1, 3, 10, 'KGF'}
>>> s.update(range(101,103))
>>> s
{2, 1, 3, 101, 102, 10, 'KGF'}
>>> s.update(12)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    s.update(12)
TypeError: 'int' object is not iterable
>>> s
{2, 1, 3, 101, 102, 10, 'KGF'}
>>> s.add(12)
>>> s
{2, 1, 3, 101, 102, 10, 12, 'KGF'}
>>> # Iterable????
>>> # collection of elements/objects
>>> 10
10
>>> 12.5
12.5
>>> [10,12.5]
[10, 12.5]
>>> [23]
[23]
>>> s.add(12)
>>> s.update(120)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    s.update(120)
TypeError: 'int' object is not iterable
>>> s.update([120])
>>> s
{2, 1, 3, 101, 102, 10, 12, 'KGF', 120}
>>> # literables: string, list, tuple,set,range(),dict
>>> s
{2, 1, 3, 101, 102, 10, 12, 'KGF', 120}
>>> s.update(10,45)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    s.update(10,45)
TypeError: 'int' object is not iterable
>>> vishwas  = 10,45
>>> type(Vishwas)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    type(Vishwas)
NameError: name 'Vishwas' is not defined
>>> type(vishwas)
<class 'tuple'>
>>> s.update(vishwas)
>>> s
{2, 1, 3, 101, 102, 10, 12, 45, 'KGF', 120}
>>> s.update(('A','java'))
>>> s
{2, 1, 3, 101, 102, 'A', 10, 12, 45, 'KGF', 'java', 120}
>>> ###################
>>> # Difference and similarity between add and update
>>> ##############################
>>> s.discard(120)
>>> s
{2, 1, 3, 101, 102, 'A', 10, 12, 45, 'KGF', 'java'}
>>> # if it is a member then remove, but if its not then do nothing
>>> s.discard(120)
>>> s.discard(1200) #its nt present
>>> ###############
>>> help(s.pop)
Help on built-in function pop:

pop(...) method of builtins.set instance
    Remove and return an arbitrary set element.
    Raises KeyError if the set is empty.

>>> s.pop()
2
>>> s.pop()
1
>>> s
{3, 101, 102, 'A', 10, 12, 45, 'KGF', 'java'}
>>> s.pop()
3
>>> d = set()
>>> d
set()
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    d.pop()
KeyError: 'pop from an empty set'
>>> # Q. DIfference between pop and discard?????
>>> s
{101, 102, 'A', 10, 12, 45, 'KGF', 'java'}
>>> s.pop(102)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    s.pop(102)
TypeError: pop() takes no arguments (1 given)
>>> 
>>> s
{101, 102, 'A', 10, 12, 45, 'KGF', 'java'}
>>> s.discard('KL')
>>> d
set()
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    d.pop()
KeyError: 'pop from an empty set'
>>> d.discard(10)
>>> #################
>>> s
{101, 102, 'A', 10, 12, 45, 'KGF', 'java'}
>>> # remove
>>> s.remove(10)
>>> s
{101, 102, 'A', 12, 45, 'KGF', 'java'}
>>> s.remove(10)# already removed
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    s.remove(10)# already removed
KeyError: 10
>>> #############################
