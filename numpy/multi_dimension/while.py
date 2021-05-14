from numpy import *

a = array([
        [10,20,30,40,50],
        [60,70,80,90],
    ], dtype=object)

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j])
        j += 1
    i+=1