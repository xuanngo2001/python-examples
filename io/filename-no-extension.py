#!/usr/bin/python3
import os

# File path example.
path="/some/file.with-weird.dot.docx"
 
# Use splitext() to get file path and extension.
(file, ext) = os.path.splitext(path)

# Remove parent directory path.
filename = os.path.basename(path)

# Re-split again with the filename only.
(file, ext) = os.path.splitext(filename)

# Print outcome.
print("Filename without extension =", file)
print("Extension =", ext)