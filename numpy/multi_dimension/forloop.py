from numpy import *

a = array([
        [10,20,30,40,50],
        [60,70,80,90],
    ], dtype=object)

for i in range(len(a)):
    # print(a[i])
    for j in range(len(a[i])):
        print(a[i][j])