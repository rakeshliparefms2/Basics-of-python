Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # String and its methods
>>> s =
SyntaxError: invalid syntax
>>> s = 'today its nice day'
>>> s
'today its nice day'
>>> # upper: all elements will be in caps
>>> s.upper()
'TODAY ITS NICE DAY'
>>> s1 =  'JOSEPH'
>>> s1
'JOSEPH'
>>> # i want in lower case
>>> s1.lower()
'joseph'
>>> #####
>>> s
'today its nice day'
>>> # t i want in caps
>>> s.title()
'Today Its Nice Day'
>>> s.capitalize()
'Today its nice day'
>>> #####
>>> # count
>>> s
'today its nice day'
>>> # count i
>>> s.count('i')
2
>>> # if something is not present
>>> s
'today its nice day'
>>> s.count('zebra')
0
>>> s.count('I')
0
>>> s.count('Today')
0
>>> ######
>>> # index
>>> s
'today its nice day'
>>> # returns an index of given substring/character
>>> s.index('a')
3
>>> s[3]
'a'
>>> s.index('its')
6
>>> # we try to findout index of missing substring
>>> s.index('java')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.index('java')
ValueError: substring not found
>>> # Q. if we try to find out index and count of something which is nt present then what will happn?
>>> s
'today its nice day'
>>> s.index('a')
3
>>> # index gives u lowest index of it
>>> # we can also use slicing to check index of next char/substring
>>> s
'today its nice day'
>>> s[6:]
'its nice day'
>>> s[6:].index('a')
10
>>> # to get index of highest char use rindex
>>> s.rindex('a')
16
>>> s[16]
'a'
>>> s.index('a')
3
>>> s.rindex('a')
16
>>> #####
>>> 'aaaaa'.index('a')
0
>>> 'aaaaa'.rindex('a')
4
>>> #########
>>> # find()
>>> # will return an index
>>> s
'today its nice day'
>>> s.find('nice')
10
>>> s[10]
'n'
>>> s.index('nice')
10
>>> # difference is
>>> s.find('java')
-1
>>> s.index('java')
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s.index('java')
ValueError: substring not found
>>> # differentiate between find and index of a string
>>> #########
>>> nm = '     rakesh lipare    '
>>> nm
'     rakesh lipare    '
>>> # remoce spaces present in suffix and prefix
>>> # use strip() method
>>> nm.strip()
'rakesh lipare'
>>> # above change is temp.
>>> nm
'     rakesh lipare    '
>>> nm = '****rakesh lipare******'
>>> nm
'****rakesh lipare******'
>>> nm.strip('*')
'rakesh lipare'
>>> nm = '****rakesh lipare$$$$'
>>> nm
'****rakesh lipare$$$$'
>>> nm.strip('*$')
'rakesh lipare'
>>> nm.strip('$*')
'rakesh lipare'
>>> nm
'****rakesh lipare$$$$'
>>> nm.strip('*re')
'akesh lipare$$$$'
>>> nm.strip('*re$')
'akesh lipa'
>>> #########
>>> nm = 'may$$**    uri'
>>> nm
'may$$**    uri'
>>> nm.strip('$* ')
'may$$**    uri'
>>> # in this case use repalce
>>> # replace
>>> nm.replace('$',' ')
'may  **    uri'
>>> nm.replace('$','')
'may**    uri'
>>> nm.replace('** ','')
'may$$   uri'
>>> nm
'may$$**    uri'
>>> nm
'may$$**    uri'
>>> nm.replace('$* ','')# this will work in new python
'may$$**    uri'
>>> nm.replace('$','').replace('*','').replace(' ','')
'mayuri'
>>> ############
>>> nm = 'AsHwIn'
>>> nm
'AsHwIn'
>>> nm.casefold()
'ashwin'
>>> 'ashwin' == nm
False
>>> 'ashwin' == nm.casefold()
True
>>> 'AmiTabhBachHaN'
'AmiTabhBachHaN'
>>> 'AmiTabhBachHaN'.casefold()
'amitabhbachhan'
>>> 'AmiTabhBachHaN'.lower()
'amitabhbachhan'
>>> # differencce betwen lower and casefold????
>>> ####################
>>> nm
'AsHwIn'
>>> s
'today its nice day'
>>> # s. after dot wait for 3-4 sec it will listout all methods of string
>>> # shortcut to use method of str.
>>> # after s. hit the tab and if u know the start of any method then give it and tab
>>> # it will appear
>>> ##########
>>> s
'today its nice day'
>>> # convert string to list of string
>>> s.split()
['today', 'its', 'nice', 'day']
>>> k = s.split()
>>> k
['today', 'its', 'nice', 'day']
>>> type(k)
<class 'list'>
>>> k
['today', 'its', 'nice', 'day']
>>> k[::-1]
['day', 'nice', 'its', 'today']
>>> # spliting criteria is a space
>>> # if we want to choose another splitting criteria
>>> s
'today its nice day'
>>> # split on the basis of nice
>>> s.split('nice')
['today its ', ' day']
>>> 'ramesh,suresh,dinesh'.split(',')
['ramesh', 'suresh', 'dinesh']
>>> ##############
>>> k
['today', 'its', 'nice', 'day']
>>> # i want to convert into a str.
>>> k.join(' ')
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    k.join(' ')
AttributeError: 'list' object has no attribute 'join'
>>> ' '.join(k)
'today its nice day'
>>> '--'.join(k)
'today--its--nice--day'
>>> ''.join(k)
'todayitsniceday'
>>> ##############
>>> fname = 'aarti patil'
>>> fname
'aarti patil'
>>> # check fname start with a or nt
>>> fname.startswith('a') #return boolean output
True
>>> fname.startswith('D')
False
>>> # if we want to check end
>>> fname.endswith('l')
True
>>> fname.endswith('patil')
True
>>> fname.endswith('Patil')
False
>>> 'patil' == 'Patil'
False
>>> 
