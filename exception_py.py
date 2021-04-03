#!/bin/python3

# Try and catch exception
try:
    print("Try some instruction")
except Exception as e:
    print(e)
    
# Raise / throw an exception
i = 2.99
if isinstance(i, int) is False:
    raise Exception("ERROR: {} must be an integer!".format(i))