from numpy import *

a = array([101,102,103,105,107])
b = array([101,102,113,105,117])
a2 = array([101,102,103,105,107])

c = a==a2
print(any(c))   # if anyone of the comparison is ture?
print(all(c))   # if all of them is true ?