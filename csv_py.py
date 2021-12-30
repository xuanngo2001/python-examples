#!/bin/python3
import csv

csv_file = "csv_py.csv"

with open(csv_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(csvreader, None)  # skip the headers
    for row in csvreader:
        i=0
        firstname=row[i].strip(); i+=1
        lastname=row[i].strip(); i+=1
        age=row[i].strip(); i+=1
        
        line = "{}, {}, {}".format(firstname, lastname, age)
        print(line)