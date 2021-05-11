from numpy import *

a = array([101,102,0,105,127,0])
b = array([105,102,113,105,117])
a2 = array([101,102,103,105,107])

c = nonzero(a)      # return all the index of array who are not zero
print(c)