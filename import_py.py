#!/bin/python3

# import x VS from x import y.
#   Always use "from x import y". This allow you to know what are being imported.

# From datetime modue, import date, datetime and timedelta class.
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
