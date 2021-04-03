#!/bin/python3

import json

# Simple dictionary.
mydict = {}
mydict['key'] = 'value'
print(mydict)   # {'key': 'value'}


# Add dictionary in dictionary.
term_dict = {'search': 33, 'replace': 99}
mydict['key'] = term_dict
print(mydict)   # {'key': {'search': 33, 'replace': 99}}

# Display json format from dictionary.
print(json.dumps(mydict, indent=4, sort_keys=True))
# {
#    "key": {
#        "replace": 99,
#        "search": 33
#    }
# }

# Dump json format to file.
json_text_formatted = json.dumps(mydict, indent=4, sort_keys=True)
with open('json.test.json', 'w') as fh:
    fh.write(json_text_formatted)

# Read json format string back to dictionary.
with open('json.test.json', 'r') as fh:
    json_text = fh.read()
new_dict = json.loads(json_text)
print(new_dict) # {'key': {'replace': 99, 'search': 33}}
print(new_dict['key']['replace'])

# Dictionary to json format.
fruits_list = ('banana', 'apple')
mydict = {}
mydict['fruits'] = fruits_list

print(mydict)
print(json.dumps(mydict, indent=4, sort_keys=True))