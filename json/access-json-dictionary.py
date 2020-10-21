#!/usr/bin/python3
import json

# Use open() to read the json file and 
#   then parse it using json.load() 
#   which saves the results in the dictionary called json_content. 
json_filename = "curl-post-content.json"
with open(json_filename, "r") as fp: 
    json_content = json.load(fp)

# Print
#~ print(json_content)

# Print pretty.
#~ print(json.dumps(json_content, sort_keys=True, indent=4))

print(json_content['body'][0]['value'])