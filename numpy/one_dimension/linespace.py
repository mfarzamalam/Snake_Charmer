from array import *

print("\nUsing linspace")
st_roll = linspace(1,8,5)      # divide 32 item in 5 people
print(st_roll)
for i in range(len(st_roll)):
    print(i,":",st_roll[i])