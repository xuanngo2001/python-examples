#!/bin/python3

# Find and replace: No regular expression
s = 'Find and replace'
r = s.replace('Find', 'Search')
print(r) # Output: Search and replace

# Find and replace within list.
words = ['ad', 'add']
r = [w.replace('ad', 'XX') for w in words]
print(r) # Output: ['XX', 'XXd']

# Find and replace whole words with list.
import re
words = ['ad', 'add']
# r for raw string(literal), \b for boundary.
r = [re.sub(r'\bad\b', 'XX', w) for w in words]
print(r) # Output: ['XX', 'add']

# ---------------------- Use replacements dictionary.
# https://stackoverflow.com/a/17730939
import re

replacements = {'ad':'XX', 
                'add':'SSSS'}

words = ['ad', 'add']
def replace(match):
    return replacements[match.group(0)]

r =  [re.sub('|'.join(r'\b%s\b' % re.escape(s) for s in replacements)
            , replace
            , w)
            for w in words]
print(r) # Output: ['XX', 'SSSS']

# ---------------------- Use replacements dictionary from file.
import re
import json

with open("find_replace.json", "r") as file:            
    replacements_json_str = file.read()
replacements = json.loads(replacements_json_str)

def replace(match):
    return replacements[match.group(0)]

words = ['ad', 'add']
words =  [re.sub('|'.join(r'\b%s\b' % re.escape(s) for s in replacements)
                    , replace
                    , w)
                    for w in words]

print(words) # Output: ['XX222', 'SSSS22']