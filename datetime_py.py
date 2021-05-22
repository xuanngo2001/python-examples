#!/bin/python3

from datetime import datetime
from datetime import date
from datetime import timedelta

# Today / now
print( datetime.now() )
print( date.today() )

# String to date
str = "2019-06-27"
dt = datetime.strptime(str, '%Y-%m-%d')
print(dt)

str = "Jun 1 2005 1:35:49PM"
dt = datetime.strptime(str, '%b %d %Y %I:%M:%S%p')
str = "2007-11-04T15:23:01Z"
dt= datetime.strptime(str, '%Y-%m-%dT%H:%M:%SZ')

# Date to string.
dt_str = dt.strftime("%m/%d/%Y, %H:%M:%S")
print( dt_str )

# Access date properties.
print( dt )
print( "Y={}, M={}, D={}".format(dt.year, dt.month, dt.day) )
print( dt.weekday() ) # where Monday is 0 and Sunday is 6

# Assign specific properties.
d1_1990 = datetime(1990, 5, 23, 23, 59, 59)
print( d1_1990.replace(month=7) )

# Add / subtract time: weeks, days, hours, minutes, seconds.
print(dt)
delta_time = timedelta(weeks=3, days=2, hours=3, minutes=27, seconds=13)
dt_new = dt - delta_time
print(dt_new)
dt_new = dt + delta_time
print(dt_new)

# Note: add 8 weeks or add 2 months are not equivalent.
from datetime import date, datetime, timedelta
from calendar import calendar, monthrange

def addMonths(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, monthrange(year,month)[1])
    return date(year, month, day)
    
a_date = date(2019, 4, 13)
print(a_date)
r = addMonths(a_date, 4)
print(r)

# Time difference between 2 datetime objects.
import time
start_dt = datetime.now()
time.sleep(3)
end_dt = datetime.now()
diff_dt = end_dt - start_dt
print("difference time = {}".format(diff_dt))
print("difference time in days = {}".format(diff_dt.days))
print("difference time in secs = {}".format(diff_dt.seconds))

# Comparison
if d1_1990 > dt_new:
    print(" date is greater ")
    
# Different between 2 dates
date_1 = date(2020, 10, 6)
date_2 = date(2021, 4, 8)
diff = date_2 - date_1
print(diff)