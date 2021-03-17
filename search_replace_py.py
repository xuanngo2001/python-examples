#!/bin/python3

# Tip data extraction.
#   - Print your string as a list to see all hidden characters.
#   - If string size is big, in MB or plus, slim the string using string.find() and cut it(e.g. str[i:j])
#   - Remove \xa0: import unicodedata; new_str = unicodedata.normalize("NFKD", unicode_str)

# str.replace() doesn't recognize regular expression.

# Search and replace using regex.
import re
s = "Example string"
r = re.sub("Ex.* ", "Ex-", s)
print(r)    # Ex-string

# Search using regex.
import re
txt = "The rain in Spain"
f = re.findall(" .*ain ", txt)
print(f)


import re
txt = "The rain in Spain"
f = re.search(" .*ain ", txt).group()
print(f)

# Match any 5 characters or more
#.{5,}

# Search and replace using lower and upper case.
import re
s = "Example string"
r = re.sub("[eE]", "X", s)
print(r)    # Ex-string

# ################# re ##########################
re.search('regex', 'text') # search the regular expression pattern and return the first occurrence
re.match('regex', 'text')  # Don't use re.match(): It checks for a match only at the beginning of the string. So, if a match is found in the first line, it returns the match object. But if a match is found in some other line, the Python RegEx Match function returns null.

# Case insensitive
re.search('test', 'TeSt', re.IGNORECASE)
re.match('test', 'TeSt', re.IGNORECASE)
re.sub('test', 'xxxx', 'Testing', flags=re.IGNORECASE)

# Remove white spaces trick.
s = ''.join(s.split())
re.sub('[\W_]', '', s)
re.sub('[^a-zA-Z0-9_]', ' ', trust_value_tmp) # Same as above.

# Remove all non-word characters (everything except numbers and letters)
s = re.sub(r"[^\w\s]", '', s)

# Replace all runs of whitespace with a single dash
s = re.sub(r"\s+", '-', s)