from datetime import datetime  # returns a datetime object
import time

dt1 = datetime(2018, 1, 1)  # create

dt2 = datetime.now()  # returns current date time

# converting a datetime strings to objects especially when gotten from a user
dt = datetime.strptime('2018/01/01', '%Y/%m/%d')
# converts timestamp to date time object
dt = datetime.fromtimestamp(time.time())
print(dt)

print(f'{dt.year}/{dt.month}')

# or

print(dt.strftime('%Y/%m'))

print(dt2 > dt1)
