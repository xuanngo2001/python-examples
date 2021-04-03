#!/bin/python3

# File all files.
base_dir = 's1-form'
pattern = "results_*.html"

for path, subdirs, files in os.walk(base_dir):
    for name in files:
        if fnmatch(name, pattern):
            print(os.path.join(path, name))
#~ fnmatch patterns:            
#~ *     : matches everything
#~ ?     : matches any single character
#~ [seq] : matches any character in seq
#~ [!seq]: matches any character not in seq            