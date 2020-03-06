#!/usr/bin/python3
import os

# File path example.
path="/some/file.with spaces.dot.docx"
 
# Get the filename only.
filename = os.path.basename(path)

# Use splitext() to get filename and extension separately.
(file, ext) = os.path.splitext(filename)

# Print outcome.
print("Filename without extension =", file)
print("Extension =", ext)