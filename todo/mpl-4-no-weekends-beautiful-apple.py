#!/usr/bin/python3
# rm -f *.png; ./m2.py ; viewpic&
# Ref: https://matplotlib.org/api/finance_api.html
## https://stackoverflow.com/questions/46992263/plotting-candlestick-with-matplotlib-for-time-series-w-o-weekend-gaps/47229291#47229291
## https://stackoverflow.com/questions/9673988/intraday-candlestick-charts-using-matplotlib
import numpy as np


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


# Preserve dates to be re-labelled later.
x_dates = loaded_data['date']

# Override loaded_data['date'] with a list of incrementatl integers.
#   This will not create gaps in the candle stick graph.
data_size = len(loaded_data['date'])
loaded_data['date'] = np.arange(start = 0, stop = data_size, step = 1, dtype='int')

# Re-arrange so that each line contains values of a day: 'date','open','high','low','close'.
quotes = [tuple(x) for x in loaded_data[['date','open','high','low','close']].values]
                 
# Plot candlestick.
##########################
fig, ax = plt.subplots()
candlestick_ohlc(ax, quotes, width=0.5, colorup='g', colordown='r');




# Go through each x-tick label and rename it.
#   For every 5th tick, show the date.
x_tick_labels = []
x_tick_indices = []
i=0
for l_date in x_dates:
    if (i%5==0):
        date_str = l_date.strftime('%b-%d')
        x_tick_labels.append(date_str)
    else:
        x_tick_labels.append("")
    x_tick_indices.append(i)
    i=i+1

ax.set(xticks=x_tick_indices, xticklabels=x_tick_labels)


# Customize graph.
##########################
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Apple')


plt.gcf().autofmt_xdate()   # Beautify the x-labels
plt.autoscale(tight=True)

# Save graph to file.
plt.savefig('mpl-4-no-weekends-beautiful-apple.png')

