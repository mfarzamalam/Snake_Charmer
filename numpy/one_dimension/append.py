from numpy import *

st_id = array('i',[])

print("Enter 0 to break")
while True:
    your_id = int(input("Enter all of your id's: "))
    st_id.append(your_id)

    if your_id == 0:
        break

all_id = len(st_id)

for i in range(all_id):
    print(st_id[i])