#!/usr/bin/python3

# Dictionary can't have duplicate keys.
#   Create a dictionary, using the List items as keys.
#   Convert dictionary back to list.
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)