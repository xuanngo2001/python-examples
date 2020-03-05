#!/usr/bin/python3
import os

# File path example.
path="/some/file.with-weird.dot.docx"
 
# Use splitext() to get file path and extension.
(file, ext) = os.path.splitext(path)

# Print full file path and extension.
print("Full file path without extension =", file)
print("Extension =", ext)
