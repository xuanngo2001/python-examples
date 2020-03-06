#!/usr/bin/python3
import pandas as pd

df = pd.DataFrame({'a': [1, 2],'b': [3, 4]})

# Print the outcome.
print(df)
# https://stackoverflow.com/questions/50741330/difference-between-df-reindex-and-df-set-index-methods-in-pandas



df = pd.DataFrame({'month': [1, 4, 7, 10],'year': [2012, 2014, 2013, 2014],'sale':[55, 40, 84, 31]})
print(df)

# https://stackoverflow.com/questions/51373222/pandas-dataframe-set-index-deletes-previous-index-and-column
