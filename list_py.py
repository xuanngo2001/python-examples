#!/bin/python3

# Define list.
fruits = ['apple', 'banana', 'pinapple']

# Add item.
fruits.append('orange')

# Loop through list.
for f in fruits:
    print(f)
    
# Find value in list.
if 'apple' in fruits:
    print('apple found in list.')

if 'kiwi' in fruits:
    print('wiki NOT found in list.')