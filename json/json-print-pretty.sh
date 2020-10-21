#!/usr/bin/python3
import json
import sys


# Use open() to read the json file and 
#   then parse it using json.load() 
#   which saves the results in the dictionary called json_content. 
json_filename = sys.argv[1]
with open(json_filename, "r") as fp: 
    json_content = json.load(fp)

# Print pretty.
print(json.dumps(json_content, sort_keys=True, indent=4))
