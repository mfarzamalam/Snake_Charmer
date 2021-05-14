from numpy import *

a = array([ [10,20,30,40,50,60,70,80,90],
            [11,21,31,41,51,61,71,81,91],
            [12,22,32,42,52,62,72,82,92],
            [13,23,33,43,53,63,73,83,93],
            [14,24,34,44,54,64,74,84,94],
            [15,25,35,45,55,65,75,85,95],
            [16,26,36,46,56,66,76,86,96],
            [17,27,37,47,57,67,77,87,97],
            [18,28,38,48,58,68,78,88,98],
            [19,29,39,49,59,69,79,89,99]])
            
print("Number of dimesions:", a.ndim)
print("Number of rows and columns:", a.shape)
print("Total number of elements in array:", a.size)
print("Number of size of a elements in bytes:", a.itemsize)
print("Array elements data-type:", a.dtype)