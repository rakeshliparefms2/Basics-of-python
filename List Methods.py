a = [10,20,30,40,50,60]
print(a)
print(id(a))
a[1:3]=[100,300]
print(a)
print(id(a))
print(a)
print(a.append('Manisha'))
print(a)
print(a.append('Rakesh'))
print(a)
print(dir(a))
print(a.clear())
##### Shallow copy ####
a = [10,20,30,40,50,60]
b = a.copy()
print(b)
##### Deep copy ####
c=a
print(a)
print(c)
a[2]='Lipare'
print(c)
print(a)
c[-3]='Dhumal'
print(c)
print(a)





















