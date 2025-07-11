from datetime import datetime, timedelta

# timedelta represent a duration

dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
print(dt1)
dt2 = datetime. now()

duration = dt2 - dt1  # we  get a timedelta object from this subtraction
print(duration)
print('days: ', duration.days)
print('seconds: ', duration.seconds)
print('Total_seconds: ', duration.total_seconds())
