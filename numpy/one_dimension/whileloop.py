from array import *

st_roll = array('f',[101,102,103,104,105,106])
n = len(st_roll)

for i in range(n):
    print(i,":", st_roll[i])

i = 0
while i < n:
    print(i,"",st_roll[i])
    i+=1


print("\nUsing While loop")
i=0
while i < len(st_roll):
    print(st_roll[i])
    i+=1
