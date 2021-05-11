from numpy import *

a = array([101,102,103,105,127])
b = array([105,102,113,105,117])
a2 = array([101,102,103,105,107])

c = where(a>b, a,b)     # compare both array and whichever is greater will make it to the result
print(c)