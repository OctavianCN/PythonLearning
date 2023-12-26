import csv


"""
When  it reach the return the context manager close the file before we can iterate it
"""
def read_data():
    with open('text2.csv') as f:
        return csv.reader(f,delimiter=',',quotechar='"')

reader = read_data()

print(type(reader)) # _csv.reader

# for row in reader:
#     print(row) # value error closed file

def read_data():
    with open('text2.csv') as f:
        yield from csv.reader(f,delimiter=',',quotechar='"') # if we use list we put entier file into memory

reader = read_data()

print(type(reader)) # generator

for row in reader: # when it is completly iterated the file is closed
    print(row)