"""
- Built-in module
when we want to use a module we need to import that module
---------------------------------
import math
print(math.factorial(4))
print(math.pi)
print('--------Module aliasing-------------')
import math as m
print(m.factorial(4))
print(m.pi)
----------------------------------
#if we want to access all the members of a module
directly
then use:
from module_name import function,variable, members
-------------------------
from math import *
# it will import everything inside math module
print(factorial(4))
print(e)
print(sin(45))
====================================
Now i want to import specific things from module
--------------------------
from math import pi,sqrt
print(pi)
print(sqrt(625))
---------------------------
from math import factorial as f
# member aliasing
print(f(4))
========================
Q. What is module and member aliasing???
====================================
from math import factorial as f,sqrt as s
print(f(2))
print(s(121))
================================
Recap:
import math
import math as m
from math import *
from math import factorial
from math import factorial,sqrt,pi,e
from math import factorial as f
========================================
# Assignment:
math
sys
os
random
itertools
collection
array
statistics
=============================================
User defined modules:
Module created by a user as per business requirement
now i want to import module_1.py in this file
========================
import Modules.module_1
print(Modules.module_1.name)
-----------------------
#module aliasing
import Modules.module_1 as m
print(m.place)
------------------------
from .....import
-----------------------
from Modules import module_1
print(module_1.name)
print(module_1.ls)
# ---------------
from Modules import module_1 as m
print(m.name)
------------------------
# Access only specific elements
from Modules.module_1 import name,place
print(name)
print(place)
-------------------------------------
# member aliasing
from Modules.module_1 import name as n,pincode as p
print(n,p)
------------------------------
# Access all members directly
from Modules.module_1 import *
print(name,place,pincode,ls)
=========================
Access dev.py file present in another dir
from flow_control_blocks import dev
# while accessing file from any other dir follow the hierarchy
-------------------------------
import math
print(dir())
print('----------------------')
from math import *
print(dir())
#-------------------------------
from math import pi,e,sqrt
print(dir())
====================================
High level===> machine_level/low==>high_level
"""












