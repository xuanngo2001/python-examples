#!/usr/bin/python3
import matplotlib
matplotlib.use('Agg') # Bypass the need to install Tkinter GUI framework

import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import datetime

#from matplotlib.finance import candlestick
from mpl_finance import candlestick_ohlc

from matplotlib.dates import num2date

# data in a text file, 5 columns: time, opening, close, high, low
# note that I'm using the time you formated into an ordinal float
##data = np.loadtxt('apple.csv', delimiter='\t')

my_headers = ['date', 'open', 'high', 'low', 'close', 'volume']
my_dtypes = {'date': 'str', 'open': 'float', 'high': 'float', 'low': 'float', 
                                                'close': 'float', 'volume': 'int'}
my_parse_dates = ['date']
data = pd.read_csv('apple.csv', sep='\t', header=1, names=my_headers, 
                            dtype=my_dtypes, parse_dates=my_parse_dates)
                            

# determine number of days and create a list of those days
ndays = np.unique(np.trunc(data[:,0]), return_index=True)
xdays =  []
for n in np.arange(len(ndays[0])):
    xdays.append(datetime.date.isoformat(num2date(data[ndays[1],0][n])))

# creation of new data by replacing the time array with equally spaced values.
# this will allow to remove the gap between the days, when plotting the data
data2 = np.hstack([np.arange(data[:,0].size)[:, np.newaxis], data[:,1:]])

# plot the data
fig = plt.figure(figsize=(10, 5))
ax = fig.add_axes([0.1, 0.2, 0.85, 0.7])
    # customization of the axis
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.tick_params(axis='both', direction='out', width=2, length=8,
               labelsize=12, pad=8)
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
    # set the ticks of the x axis only when starting a new day
ax.set_xticks(data2[ndays[1],0])
ax.set_xticklabels(xdays, rotation=45, horizontalalignment='right')

ax.set_ylabel('Quote ($)', size=20)
ax.set_ylim([177, 196])

candlestick_ohlc(ax, data2, width=0.5, colorup='g', colordown='r')

plt.savefig('m3-apple.png')