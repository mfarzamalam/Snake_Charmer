from array import *

print("\nUsing arange() Function")
st_roll = arange(10,101,10)      # 3rd value shows the stepsize. how many number it won't use

for i in range(len(st_roll)):
    print(i,":",st_roll[i])