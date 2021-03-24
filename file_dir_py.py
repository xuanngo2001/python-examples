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

# Delete file.
os.remove(path)

# Remove directory.
os.rmdir(path)

# Filename, file, extension.
path = "/some/file.with spaces.dot.docx"
filename = os.path.basename(path)

(file, ext) = os.path.splitext(filename)

print("Filename =", filename)
print("Filename without extension =", file)
print("Extension =", ext)

# Read, write, append mode.
with open(filename, 'r') as fh:
    pass
with open(filename, 'w') as fh:
    pass
with open(filename, 'a') as fh:
    pass    