"""
Mapping and Accumulation

Mapping -> applying a callable to each element of an iterable -> map(fn, iterable)
Accumulation -> reducing an iterable down to a single value
    -> sum(iterable)
    -> min(iterable)
    -> max(iterable)
    -> reduce(fn, iterable, [initializer]) -> fn is a function of two arguments
                                           -> applies fn cumulatively to elements of iterable

############# map ####################
map(fn, iterable) - applies fn to every element of iterable and returns an iterator(lazy)
    -> fn must be a callable that requires a single argument
map(lambda x: x**2, [1,2,3,4]) -> 1, 4, 9, 16 -> lazy iterator

We can easly do the same using a generator expression:

maps = (fn(item) for item in iterable)

################ reduce ####################

Suppose we want to find the sum of all elements in an iterable: l = [1, 2, 3, 4]
sum(l) -> 1+2+3+4 = 10
reduce(lambda x, y: x+ y, l) -> 1 -> 1 + 2 = 3 -> 3 + 3 = 6 -> 6 + 4 = 10

To find the product of all elements:

reduce(lambda x, y: x*y, l) -> 1 -> 1*2=2 -> 2*3=6 -> 6*4=24

We can specify a different start value in reduction

reduce(lambda x, y: x+y, l, 100) -> 110


################# itertools.starmap ###################

starmap is very similar to map:
    -> it unpacks every sub element of the iterable argument, and passes that to the map function
    -> useful for mapping a multi-argument function on an iterable of iterables

l = [[1, 2], [3, 4]] map(lambda item: item[0] * item[1], l) -> 2, 12

We can use starmap: starmap(operator.mul, l) -> 2, 12
    or we could just use a generator expression:
        (operator.mul(*item) for item in l)
We can of course use iterables that contain more than just two values:
l = [ [1, 2, 3], [10, 20, 30], [100, 200, 300] ]

starmap(lambda x, y, z: x+y+z, l) -> 6, 60, 600

#################### itertools.accumulate(iterable, fn) -> lazy iterator ################

The accumulate function is very similar to the reduce function

But it returns a lazy iterator producing all the intermediate results
    -> reduce only returns the final result

Unlike reduce, it does not accept an initializer

-> in accumulate fn is optional (defaults to addition)

l = [1, 2, 3, 4]

functools.reduce(operator.mul, l) -> 1 -> 1*2=2 -> 2*3=6 -> 6*4=24 -> 24
itertools.accumulate(l, operator.mul) -> 1,2,6,24

"""


maps = map(lambda x: x**2, range(5))
print(type(maps)) # map
print(iter(maps) is maps) # True
print('__next__' in dir(maps)) # True
print(list(maps))


def add(t):
    return t[0] + t[1]

print(list(map(add, [(0,0), [1, 1], range(2,4)])))

def add(x, y):
    return x + y

t = 2, 3
print(add(*t))

print([add(*t) for t in [(0,0), [1, 1], range(2,4)]])

from itertools import starmap
print(list(starmap(add, [(0,0), [1, 1], range(2,4)])))

print(sum(range(10,40,10)))

from functools import reduce

print(reduce(lambda x, y: x*y, [1,2,3,4])) # 24

print(reduce(lambda x, y: x*y, [1,2,3,4], 10)) # 240

def sum_(iterable):
    it = iter(iterable)
    acc = next(it)
    yield acc
    for item in it:
         acc += item
         yield acc

for item in sum_([10, 20, 30]):
    print(item)

def running_reduce(fn, iterable, start=None):
    it = iter(iterable)
    if start is None:
        acc = next(it)
    else:
        acc = start
    yield acc

    for item in it:
        acc = fn(acc, item)
        yield acc

print(list(running_reduce(lambda x, y: x + y, [10, 20, 30])))

import operator

print(list(running_reduce(operator.add, [10, 20, 30])))

print(list(running_reduce(operator.mul, [10, 20, 30])))
print(list(running_reduce(operator.mul, [10, 20, 30], 10)))

from itertools import  accumulate

print(list(accumulate([10, 20, 30])))

print(list(accumulate([10, 20, 30], operator.mul)))

from itertools import chain

chain([10], [1, 2, 3, 4])

print(list(accumulate(chain((10,),[10, 20, 30]), operator.mul)))