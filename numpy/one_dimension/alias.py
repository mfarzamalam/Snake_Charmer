from numpy import *

a = array([101,102,0,105,127,0])
b = array([105,102,113,105,117])
a2 = array([101,102,103,105,107])

c = a 

print(id(a))
print(id(c))     # array is same. compiler won't create a new array. to check use id function