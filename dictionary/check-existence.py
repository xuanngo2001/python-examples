#!/bin/python3

d = {'1': 'one', '3': 'three', '2': 'two', '5': 'five', '4': 'four'}

# Check existence of index.
if '2' in d:
    print("'2' index is found")
else:
    print("'2' index is NOT found")


# Check existence of value.
if 'two' in d.values():
    print("'two' value is found")
else:
    print("'two' value is NOT found")
