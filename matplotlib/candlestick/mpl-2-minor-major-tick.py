#!/usr/bin/python3
# rm -f *.png; ./m2.py ; viewpic&
# Ref: https://matplotlib.org/api/finance_api.html
## https://stackoverflow.com/questions/46992263/plotting-candlestick-with-matplotlib-for-time-series-w-o-weekend-gaps/47229291#47229291
## https://stackoverflow.com/questions/9673988/intraday-candlestick-charts-using-matplotlib

import pandas as pd
from mpl_finance import candlestick_ohlc

from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
    
import matplotlib
matplotlib.use('Agg') # Bypass the need to install Tkinter GUI framework
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Avoid FutureWarning: Pandas will require you to explicitly register matplotlib converters.
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Load data from CSV file.
##########################
my_headers = ['date', 'open', 'high', 'low', 'close', 'volume']
my_dtypes = {'date': 'str', 'open': 'float', 'high': 'float', 'low': 'float', 
                                                'close': 'float', 'volume': 'int'}
my_parse_dates = ['date']
loaded_data = pd.read_csv('apple.csv', sep='\t', header=1, names=my_headers, 
                            dtype=my_dtypes, parse_dates=my_parse_dates)


# Convert 'Timestamp' to 'float'.
#   candlestick_ohlc needs time be in float days format - see date2num.
loaded_data['date'] = [mdates.date2num(d) for d in loaded_data['date']]

# Re-arrange so that each line contains values of a day: 'date','open','high','low','close'.
quotes = [tuple(x) for x in loaded_data[['date','open','high','low','close']].values]
                 
# Plot candlestick.
##########################
fig, ax = plt.subplots()
candlestick_ohlc(ax, quotes, width=0.5, colorup='g', colordown='r');


# Customize graph.
##########################
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Apple')

# Format time.
#ax.xaxis_date()
#ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()                  # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
ax.xaxis_date()

plt.gcf().autofmt_xdate()   # Beautify the x-labels
plt.autoscale(tight=True)

# Save graph to file.
plt.savefig('mpl-2-minor-major-tick-apple.png')
