#!/bin/python3

# Find string and cut it.
str = "hello world"
index = str.find('world')
if index == -1:
    print("String not found.")
else:
    print("{} is the index postion of the found string".format(index))
    
    hello = str[0:index]
    print(hello)
    
    world = str[index:]
    print(world)
    
# Replace
str = "hello world"
str.replace('o', 'A')     # Replace all occurrences.
str.replace('o', 'A', 3)  # Replace the 1st 3 occurrences.

