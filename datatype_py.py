#!/bin/python3

# String to int.
i = int("233")  # Can't be decimal string or None.
print(i)

# Decimal to int.
f = float("23.3")
i = int(f)
print(i)

# Is it an integer
if isinstance(i, int):
    print("It is an integer.")
    
# Decimal to float.
f = float("66.98") # Can't be None.
print(f)