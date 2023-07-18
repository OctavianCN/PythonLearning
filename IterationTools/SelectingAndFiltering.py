"""
The filter function:

filter(predicate, iterable) -> reutnrs all elements of iterable where predicate(element) is True

predicate can be None - in which case it is the identify function f(x) -> x
 in other words, thruthy elements only will be retained

-> filter returns a lazy iterator

We can achive the same result using generator expressions:

(item for item in iterable if pred(item)) predicate is not None

(item for item in iterable if item) - predicate is None
or (item for item in iterable if bool(item)

Example:

    filter(lambda x: x < 4, [1, 10, 2, 10, 3, 10]) -> 1,2,3
    filter(None, [0, '', 'hello', 10, False]) -> 'hello', 100

remember that filter returns a lazy iterator


itertools.filterfalse

    This works the same way as the filter function but instead of retaining elements where the predicate evaluates to True
it retains elements where the predicate evalutaes to False

Example:

    filterflase(lambda x: x<4, [1,10,2,10,3,10]) -> 10, 10, 10
    filterfalse(None, [0,'','hello',100,False]) -> 0,'', False

-> filterfalse returns a lazy iterator


itertools.compress

It is basically a way of filtering one iterable using the truthiness of items in another iterable

data = ['a', 'b', 'c', 'd', 'e']
selectors = [True, False, 1, 0] None

compress(data, selectors) -> a,c

compress returns a lazy iterator



itertools.takewhile

takewhile(pred, iterable)

The takewhile function returns an iterator that will yield items while pred(item) is Truthy
-> at that point the iterator is exhausted even if there are more items in the iterable whose predicate
would be thruthy

takewhile(lambda x: x<5, [1,3,5,2,1]) -> 1,3

takewhile -> returns a lazy iterator



itertools.dropwhile

dropwhile(pred, iterable)

The dropwhile function returns an iterator that will start iterating(and yield all remaning elements)
once pred(item) becomes Falsy

dropwhile(lambda x: x<5, [1,3,5,2,1] -> 5,2,1

dropwhile -> returns a lazy iterator
"""

def gen_cubes(n):
    for i in range(n):
        print(f'yielding {i}')
        yield i**3

def is_odd(x):
    return x % 2 == 1

print(is_odd(4),is_odd(41))

filtered = filter(is_odd, gen_cubes(10))
print(list(filtered))

def is_even(x):
    return x % 2 == 0

filtered = filter(is_even, gen_cubes(10))
print(list(filtered))

from itertools import filterfalse

filtered = filterfalse(is_odd, gen_cubes(10))
print(list(filtered)) # get all even numbers

##### dropwhile and takewhile #########

from itertools import dropwhile, takewhile

from math import sin, pi

def sine_wave(n):
    start = 0
    max_ = 2 * pi
    step = (max_ - start) / (n-1)

    for _ in range(n):
        yield round(sin(start), 2)
        start += step


print(list(sine_wave(15)))

result = takewhile(lambda x: 0 <= x <= 0.9, sine_wave(15))

print(list(result))
# print(next(result)) - result was exhausted

l = [1, 3, 5, 2, 1]

print(list(dropwhile(lambda x: x < 5, l)))

########### Compress ##################

data = ['a', 'b', 'c', 'd', 'e'] # data = list('abcde')
selectors = [True, False, 1, 0] # remaning terms remain None

print(list(zip(data,selectors))) # [('a', True), ('b', False), ('c', 1), ('d', 0)]

print([item for item,truth_value in zip(data,selectors) if truth_value]) # ['a', 'c']

from itertools import compress

print(list(compress(data,selectors))) # ['a', 'c']