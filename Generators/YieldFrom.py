"""
Delegating to another iterator

Often we may neeed to delegate yielding elements to another iterator

file1.csv file2.csv file3.csv

def read_all_data():
  for file in ('file1.csv', 'file2.csv', 'file3.csv'):
    with open(file) as f:
      for line in f:
        yield line

def read_all_data():
  for file in ('file1.csv', 'file2.csv', 'file3.csv'):
    with open(file) as f:
        yield from f
"""

def matrix(n):
    gen = ( (i*j for j in range(1, n+1))
        for i in range(1, n+1)
    )
    return gen

m = list(matrix(5))
print(m) # generators

def matrix_iterator(n):
    for row in matrix(n):
        for item in row:
            yield item

for item in matrix_iterator(3):
    print(item)

def matrix_iterator(n):
    for row in matrix(n):
        yield from row

for item in matrix_iterator(3):
    print(item)

