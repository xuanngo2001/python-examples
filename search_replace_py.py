#!/bin/python3

# str.replace() doesn't recognize regular expression.

import re
s = "Example string"
r = re.sub("Ex.* ", "Ex-", s)
print(r)    # Ex-string