#!/bin/python3

dict = {'key': "value"}

# Add
dict.update({'key': "value2"})
print(dict)

# Remove
if 'key' in dict:
    del dict['key']

dict.pop('key', None)

# Silent KeyError if key doesn't exist.
#   mydict.get('key', default)
dict.get('key', None)