"""
Caveat of Using Iterators as Function Arguments
"""

import random

class Randoms:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            self.i += 1
            return random.randint(0, 100)

random.seed(0)
l = list(Randoms(10))
print(l)
print(min(l), max(l))

random.seed(0)
l = Randoms(10)
print(min(l))
#print(max(l)) # at max we get an exception because l is already exhausted

f = open('cars.csv')

for row in f:
    print(row, end='')
f.close()

def parse_data_row(row):
    row = row.strip('\n').split(';')
    return row[0], float(row[1])

def max_mpg(data):
    max_mpg = 0
    for row in data:
        _, mpg = parse_data_row(row)
        if mpg > max_mpg:
            max_mpg = mpg
    return max_mpg

f = open('cars.csv')
next(f)
next(f)
print(max_mpg(f))
f.close()

def list_data(data, mpg_max):
    for row in data:
        car, mpg = parse_data_row(row)
        mpg_perc = mpg / mpg_max * 100
        print(f'{car}: {mpg_perc:.2f}%')

f = open('cars.csv')
next(f)
next(f)
list_data(f, 46.6)
f.close()


print("=================")

with open('cars.csv') as f:
    next(f)
    next(f)
    max_ = max_mpg(f)
    print(max_)
    list_data(f, max_) # now f is exhausted

print("=================")

with open('cars.csv') as f:
    cars = f.readlines()[2:] # now we have the entire file load into memory
max_ = max_mpg(cars)
list_data(cars, max_)

print("=================")
with open('cars.csv') as f:
    next(f), next(f)
    max_ = max_mpg(f)
    # now we are done with f because it is exhausted

f = open('cars.csv')
next(f),next(f)
list_data(f, max_)
f.close()

print("==============")
def list_data(data):
    if iter(data) is data:
        raise ValueError('data cannot be an iterator')
    max_mpg = 0
    for row in data:
        _, mpg = parse_data_row(row)
        if mpg > max_mpg:
            max_mpg = mpg

    for row in data:
        car, mpg = parse_data_row(row)
        mpg_perc = mpg / max_mpg * 100
        print(f'{car}: {mpg_perc:.2f}%')

# with open('cars.csv') as f:
#     next(f), next(f)
#     list_data(f)

def list_data(data):
    if iter(data) is data:
        data = list(data)
    max_mpg = 0
    for row in data:
        _, mpg = parse_data_row(row)
        if mpg > max_mpg:
            max_mpg = mpg

    for row in data:
        car, mpg = parse_data_row(row)
        mpg_perc = mpg / max_mpg * 100
        print(f'{car}: {mpg_perc:.2f}%')

with open('cars.csv') as f:
    next(f), next(f)
    list_data(f)