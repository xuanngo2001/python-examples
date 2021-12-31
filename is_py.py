#!/bin/python3

obj = 1

if type(obj) == int:
    print("Integer")
    
obj = 12.2312
if type(obj) == float:
    print("Float")
    
obj = 12.3213
if type(obj) == int or type(obj) == float:
    print("It is a number")
else:
    print("It is NOT a number")