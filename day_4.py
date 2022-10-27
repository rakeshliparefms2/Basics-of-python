Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Data types in Python
>>> # Numeric: int, float, complex
>>> # int: base 10 [0-9]
>>> type(10)
<class 'int'>
>>> 125827682743687624876782468234
125827682743687624876782468234
>>> # in python we dont have a limit for int value
>>> # float: floating values
>>> 1.3
1.3
>>> 14.55
14.55
>>> 456.22
456.22
>>> type(456.22)
<class 'float'>
>>> # complex: real + img
>>> 3 + 0j
(3+0j)
>>> type(3+0j)
<class 'complex'>
>>> 3 + 0J
(3+0j)
>>> 4j
4j
>>> type(4j)
<class 'complex'>
>>> #########################
>>> # Boolean:True False
>>> # when we are comparing the objects/ doing the conditional check
>>> # it result boolean output
>>> True
True
>>> False
False
>>> 2 > 3
False
>>> 3 == 3
True
>>> #######################
>>> # String
>>> # Global data type
>>> # bcz it accepts everything
>>> # syntax: '' or ""
>>> ''
''
>>> ""
''
>>> type('')
<class 'str'>
>>> type("")
<class 'str'>
>>> type('''''')
<class 'str'>
>>> ####
>>> '123123214'
'123123214'
>>> '$^%$^%&^#!'',.;'
'$^%$^%&^#!,.;'
>>> '$^%$^%&^#!'',.;
SyntaxError: EOL while scanning string literal
>>> '$^%$^%&^#!'',.;'
'$^%$^%&^#!,.;'
>>> "$^%$^%&^#!'',.;"
"$^%$^%&^#!'',.;"
>>> ################
>>> 'my name is 'Amruta''
SyntaxError: invalid syntax
>>> # Rule: if we have single quote outside , inside u must use " viceversa
>>> "''"
"''"
>>> '""'
'""'
>>> ''''


''''
SyntaxError: EOL while scanning string literal
>>> 'my name is "Amruta"'
'my name is "Amruta"'
>>> "my name is 'Amruta'"
"my name is 'Amruta'"
>>>  #####################
>>> # Features of a String
>>> # Background data structure : Array
>>> s = 'pythonist'
>>> s
'pythonist'
>>> # if i want to count total elements in a list
>>> # will use len() fucntion
>>> len(s)
9
>>> len(s)-1
8
>>> # indexing gives an access to a single element
>>> # access t
>>> s[
	]
SyntaxError: invalid syntax
>>> s[2]
't'
>>> s[6]
'i'
>>> s[1]
'y'
>>> type(s)
<class 'str'>
>>> s
'pythonist'
>>> s[8]
't'
>>> # space is also oen block
>>> a = 'amit shaha'
>>> a
'amit shaha'
>>> a[4]
' '
>>> a[3]
't'
>>> b = '@#$%'
>>> b[2]
'$'
>>> b[0]
'@'
>>> #################
>>> s
'pythonist'
>>> s[2]
't'
>>> # to access a subpart/substring from main string then use Slicing
>>> s[:]
'pythonist'
>>> #[start:stop]
>>> # [start_index:stop_index]
>>> # lets acces thon
>>> s[2:5]
'tho'
>>> # stop is exclusive
>>> s[5]
'n'
>>> s[2:6]
'thon'
>>> # python
>>> s[0:6]
'python'
>>> # slicing always starts from 0
>>> s[:6]
'python'
>>> # onist
>>> s[4:9]
'onist'
>>> # slicing readches upto end if index not provided
>>> s[:]
'pythonist'
>>> s[4:]
'onist'
>>> # slicing also has step option
>>> s[::]
'pythonist'
>>> # s[start:stop:step]
>>> s[::1]
'pythonist'
>>> s[::2]
'ptoit'
>>> s[::20000]
'p'
>>> # We have +ve and - ve indexing
>>> s[0]
'p'
>>> s[-9]
'p'
>>> s[-5]
'o'
>>> #slicing
>>> s
'pythonist'
>>> s[-7:]
'thonist'
>>> # when we hv step 1 it progress from left to right always
>>> s
'pythonist'
>>> s[-5:]
'onist'
>>> # BUT if WE HAVE STEPING OF -1
>>> # THen it progress from right to left
>>> s
'pythonist'
>>> s[::1]
'pythonist'
>>> s[::-1] #go from right to left/ will get reverse order
'tsinohtyp'
>>> # reverse the string
>>> a
'amit shaha'
>>> a[::-1]
'ahahs tima'
>>> #############
>>> a
'amit shaha'
>>> a[-4::]
'haha'
>>> a[-4::-1]
'hs tima'
>>> # haha reverse
>>> # ahah
>>> a[-1::-1]
'ahahs tima'
>>> a[-1:-5:-1]
'ahah'
>>> a
'amit shaha'
>>> # reverse amit
>>> # tima
>>> a[-7::-1]
'tima'
>>> #####################
>>> a
'amit shaha'
>>> # String methods
>>> a.upper()
'AMIT SHAHA'
>>> # A of amit Capital
>>> a.capitalize()
'Amit shaha'
>>> #  so A and S should be capital
>>> a.title()
'Amit Shaha'
>>> # repalce shaha with patil
>>> a.replace('shaha','Patil')
'amit Patil'
>>> #all these changes are temp.
>>> a
'amit shaha'
>>> # how to give multiline string
>>> 'jkhjhjks lksjldkfj'
'jkhjhjks lksjldkfj'
>>> 'jkhskjfh \
jkbsjkfbkjbkj \
bksdfkjbkjsdf\
234235345345
SyntaxError: EOL while scanning string literal
>>> 'jkhskjfh \
jkbsjkfbkjbkj \
bksdfkjbkjsdf\
234235345345'
'jkhskjfh jkbsjkfbkjbkj bksdfkjbkjsdf234235345345'
>>> 'jkhskjfh\n\
jkbsjkfbkjbkj\n\
bksdfkjbkjsdf\n\
234235345345'
'jkhskjfh\njkbsjkfbkjbkj\nbksdfkjbkjsdf\n234235345345'
>>> print('jkhskjfh\n\
jkbsjkfbkjbkj\n\
bksdfkjbkjsdf\n\
234235345345')
jkhskjfh
jkbsjkfbkjbkj
bksdfkjbkjsdf
234235345345
>>> s
'pythonist'
>>> s[::2]
'ptoit'
>>> s[1::2]
'yhns'
>>> 'madam'[::-1]
'madam'
>>> s1 = 'madam'
>>> s2 = 'Madam'
>>> s1 == s2
False
>>> s1[::-1] == s2[::-1]
False
>>> '121' == '121'[::-1]
True
>>> s
'pythonist'
>>> 
