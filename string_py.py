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

# ----------------- Parameterize string format
# ---https://docs.python.org/3/library/string.html#format-specification-mini-language

print( "{z} {x}".format(x=32.23, z="hello") )   # hello 32.23
print( "{1} {0}".format(32.23, "hello") )       # hello 32.23

print( "{:,}".format(1234) )                    # 1,234

print( "{z:.4f}".format(z=561234.316546) )      # 561234.3165

print( "{z:+.3f}".format(z=-4.6546) )           # -4.655
print( "{z:+.3f}".format(z=4.6546) )            # +4.655

print( "[{:>7}]".format(4.52) )                 # [   4.52]

print( "{:05n}".format(7) )                     # 00007
print( "{:05d}".format(7) )                     # 00007
print( "7".zfill(5) )                           # 00007

import datetime
'{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

# Lowercase / uppercase
print(str.lower())
print(str.upper())

# Join / split
fruits = ('banana', 'kiwi', 'apple')
s = ', '.join(fruits)
print(s)