from numpy import *

#### Converting 1D array into 2D or 3D and vice versa

a = array([1,23,4,5,6,7,8,10,9,15])
b = reshape(a, (2,5))   # first is row, second is column
print(b)

print()

c = array([[1,2,3], [4,5,6]])
d = reshape(c, (6))
print(d)

print()

#### Converting 2D or 3D array into 1D using flatten() method
f = array([[1,2,3], [4,5,6]])
g = f.flatten()
print(g)