"""
The zip Function -> lazy iterator

We have already seen the zip function
It takes a variable number of positional arguments - each of which are iterables
It returns an iterator that produces tuples containing the elements of the iterables, iterated one
at a time
It stops immediately once one of the iterables has been completly iterated over -> zips based on the shortest iterable

zip([1,2,3], [10, 20], ['a','b','c','d']) -> (1, 10, 'a'), (2, 20, 'b')

itertools.zip_longest(*args, [fillvalue=None])

Sometimes we want to zip, but based on the longest iterable
    -> need to provide a default value for the "holes" -> fill value

zip_longest([1,2,3], [10, 20], ['a','b','c','d']) -> (1, 10, 'a'), (2, 20, 'b'), (3, None, 'c'), (None, None, 'd')

zip_longest([1,2,3], [10, 20], ['a','b','c','d'], -1) -> (1, 10, 'a'), (2, 20, 'b'), (3, -1, 'c'), (-1, -1, 'd')

"""

######## Zipping ##############

l1 = [1,2,3,4,5]
l2 = [1,2,3,4]
l3 = [1,2,3]
results = zip(l1, l2, l3)
print(iter(results) is results) # True
print('__next__' in dir(results)) # True

print(list(results))

def integer(n):
    for i in range(n):
        yield i

def squares(n):
    for i in range(n):
        yield i**2

def cubes(n):
    for i in range(n):
        yield i**3

iter1 = integer(6)
iter2 = squares(5)
iter3 = cubes(4)

print(list(zip(iter1, iter2, iter3)))

from itertools import zip_longest

help(zip_longest)

l1 = [1,2,3,4,5]
l2 = [1,2,3,4]
l3 = [1,2,3]

print(list(zip_longest(l1, l2, l3, fillvalue='N/A')))

def squares():
    i = 0
    while True:
        yield i**2
        i += 1

def cubes():
    i = 0
    while True:
        yield i ** 3
        i +=1

iter1 = squares()
iter2 = cubes()

print(list(zip(range(10),iter1, iter2)))