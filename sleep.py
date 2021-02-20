import time
from datetime import date
# sleep method

for i in range(10):
    # print(i)
    if i == 5:
        pass
        # time.sleep(3)

#Calculate The age

current_date = date.today()
print(current_date)
print("1999-02-21")
                                  #    01234567
dob = int(input("Enter your birth year(yyyymmdd)\n:"))
dobstring = str(dob)
yearString = dobstring[:4]
monthString = dobstring[4:6]
dayString = dobstring[6:]

yearInt = int(yearString)
monthInt = int(monthString)
dayInt = int(dayString)

ageInYear = current_date.year - yearInt

if current_date.month <= monthInt:
    if current_date.day < dayInt:   
        print(ageInYear-1)
    else:
        print(ageInYear)
else:
    print(ageInYear)