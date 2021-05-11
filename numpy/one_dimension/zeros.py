from array import *

print("\nUsing zeros() Function")
st_roll = zeros(50, dtype=float)      # generate all zero, dtype is data type

for i in range(len(st_roll)):
    print(i,":",st_roll[i])