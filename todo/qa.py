#!/usr/bin/python3
import matplotlib
matplotlib.use('Agg') # Bypass the need to install Tkinter GUI framework

import quandl
import numpy as np
from mpl_finance import candlestick_ohlc
import matplotlib.pyplot as plt



# getting data and modifying it to remove gaps at weekends
r = quandl.get('WIKI/AAPL', start_date='2016-01-01', end_date='2017-11-10')
date_list = np.array(r.index.to_pydatetime())
plot_array = np.zeros([len(r), 5])
plot_array[:, 0] = np.arange(plot_array.shape[0])
plot_array[:, 1:] = r.iloc[:, :4]

print(plot_array)
# plotting candlestick chart
fig, ax = plt.subplots()
num_of_bars = 100  # the number of candlesticks to be plotted
candlestick_ohlc(ax, plot_array[-num_of_bars:], colorup='g', colordown='r')
ax.margins(x=0.0, y=0.1)
ax.yaxis.tick_right()
x_tick_labels = []
ax.set_xlim(right=plot_array[-1, 0]+10)
ax.grid(True, color='k', ls='--', alpha=0.2)
# setting xticklabels actual dates instead of numbers
indices = np.linspace(plot_array[-num_of_bars, 0], plot_array[-1, 0], 8, dtype=int)

for i in indices:
    date_dt = date_list[i]
    date_str = date_dt.strftime('%b-%d')
    print(date_str)
    x_tick_labels.append(date_str)
ax.set(xticks=indices, xticklabels=x_tick_labels)


# Save graph to file.
plt.savefig('quandl-apple.png')