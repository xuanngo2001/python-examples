#!/usr/bin/python3

my_list = [ 1, 5, 2, 4, 2, 5 ]

seen = set()
unique = []
duplicate = []
for x in my_list:
    if x not in seen:
        unique.append(x)
        seen.add(x)
    else:
        duplicate.append(x)
        
print(duplicate, " are duplicates.")
print(unique, " are unique.")
