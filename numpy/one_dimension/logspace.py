from array import *

print("\nUsing logspace")
st_roll = logspace(1,5,num=5,base=4)      # base says to the power of 4, num says number of column

for i in range(len(st_roll)):
    print(i,":",st_roll[i])