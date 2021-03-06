#!/usr/bin/python3
import pandas as pd

try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3

import matplotlib.dates as mdates



data="""Date,Stock,Open,High,Low,Close,Volume
2016-09-29,KESM,7.92,7.98,7.92,7.97,149400
2016-09-30,KESM,7.96,7.97,7.84,7.9,29900
2016-10-04,KESM,7.8,7.94,7.8,7.93,99900
2016-10-05,KESM,7.93,7.95,7.89,7.93,77500
2016-10-06,KESM,7.93,7.93,7.89,7.92,130600
2016-10-07,KESM,7.91,7.94,7.91,7.92,103000"""
df = pd.read_csv(StringIO(data), index_col='Date', parse_dates=True)
