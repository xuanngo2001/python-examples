#!/bin/python3

import os

# Create directory.
path="/tmp/xuan"
try:
    os.mkdir(path)
except OSError:
    print ("ERROR: Create directory {} failed".format(path))
else:
    print ("{} directory created!".format(path))

# Create multi-level subdirectories.
path_subdirs = "/tmp/xuan2/a/b/b/d"
os.makedirs(path_subdirs)    


# Remove directory.
os.rmdir(path)
