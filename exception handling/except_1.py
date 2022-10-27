"""
Exception means error.
Example:
    NameError
    TypeError
    ValueError
    .
    .
# Why to handle exception???

print(100)
print(list(range(5)))
print(a)
print('Hello gm')
print(234234255)
----- if we look at above scenario
bcz of a next 2 lines wont b executed
so in order to avoid this
problem we need Exception handling
-----------------------------------
How to handle exception:
We have 4 blocks to deal with this
try:
    test the code here
except:
    if exception occurs in try then handle it here
    in except
else:
   if exception doesnt occurs in try then else
finally:
    it dont care abt exception occur or nt
    this block will be executed always
    irrespective of exception
===================================
"""
try: #we put a code to test an error
    print(a)

except:# come here if error occurs
    print('Error present')
print('Hello I m ready to execute')
