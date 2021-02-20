from time import localtime
from datetime import datetime
from datetime import timedelta, date

lt = localtime()

print(lt)
print(lt.tm_year)
print()
print("Today's Date(d/m/y) - "+str(lt.tm_mday) + "/" + str(lt.tm_mon) + "/" + str(lt.tm_year))

print()
dt = datetime.today()
print(dt)
print(dt.year)
print(dt.day)
print(dt.second)

forward_date = timedelta(days=30)
current_date = date.today()

required_date = current_date + forward_date
print(required_date)

print("Your subscription date is :" +str(current_date))
print("Your expiration date is :" +str(required_date))

dt2 = datetime.today()
formt_dt = dt2.strftime("%D")
print(formt_dt)