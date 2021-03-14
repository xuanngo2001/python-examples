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