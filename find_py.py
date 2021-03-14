#!/bin/python3

base_dir = 's1-form'
pattern = "results_*.html"

for path, subdirs, files in os.walk(base_dir):
    for name in files:
        if fnmatch(name, pattern):
            print(os.path.join(path, name))