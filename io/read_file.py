#!/usr/bin/python3

# Load the whole file into a string variable.
with open("myfile.txt", "r") as file:            
    content=file.read()
    
# Load every lines into lines[] and suffix with newline character.
lines = []
with open("myfile.txt", "r") as file:            
    lines = content=file.readlines()