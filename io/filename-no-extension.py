#!/usr/bin/python3
import os

# File path example.
path="/some/file.with-weird.dot.docx"
 
# Use splitext() to get file path and extension.
(file, ext) = os.path.splitext(path)

# Remove parent directory path.
basename = os.path.basename(path)

# Re-split again without the filename.
(file, ext) = os.path.splitext(basename)

# Print outcome.
print("Filename without extension =", file)
print("Extension =", ext)