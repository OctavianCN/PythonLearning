# Lists vs Tuples


"""
Constant folding - is the process of recognizing and evaluating constant expressions
                    at compile time rather than computing them at runtime

"""
import sys
from dis import dis

print((1,2,3))
print([1,2,3])

"""
For tuples:
It takes one step to compile the tuple load into a constant and then return it
(Constant folding)
"""
dis(compile('(1,2,3,"a")', 'string', 'eval'))

"""
For lists
It have to load each individual constant up first then it builds the lists
and then return it
"""
dis(compile('[1,2,3,"a"]', 'string', 'eval'))
dis(compile('[1,2,3,"a", [1,2,"a"]]', 'string', 'eval')) # it loads every constant of the respective list and then build the lists

# Tuples are more efficient than lists

from timeit import timeit

print(timeit("(1,2,3,4,5,6,7,8,9)", number=10_000_000)) # tuple - 0.05
print(timeit("[1,2,3,4,5,6,7,8,9]", number=10_000_000)) # list - 0.35

def fn1():
    pass

dis(compile('(fn1,10,20)','string','eval')) # because of fn now it has to load things individualy
dis(compile('([1,2,3],10,20)','string','eval')) # same if it have lists in it


l1 = [1, 2,3,4,5,6,7,8,9]
t1 = (1,2,3,4,5,6,7,8,9)
print(id(l1), id(t1))

l2 = list(l1)
print(l1 is l2) #False different memory addresses

t2 = tuple(t1)
print(t1 is t2) #True same memory address

print(timeit('tuple((1,2,3,4,5))',number=5_000_000)) # is faster
print(timeit('list((1,2,3,4,5))', number=5_000_000))


# Storage Efficiency
print("Storage Efficiency For Tuples")
t = tuple()
prev = sys.getsizeof(t)
for i in range(10):
    c = tuple(range(i+1))
    size_c = sys.getsizeof((c))
    delta, prev = size_c - prev, size_c # when a tuple got one elem longer it needed only extra 8 bytes
    print(f'{i+1} items: {size_c}, delta = {delta}')

print("Storage Efficiency For Lists")
l = list()
prev = sys.getsizeof(l)
for i in range(10):
    c = list(range(i+1))
    size_c = sys.getsizeof((c))
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, delta = {delta}')

print("Watching list storage how it is used")
c = list()
prev = sys.getsizeof(c)
print(f'0 items: {prev}') # for one item 56 bytes
for i in range(255):
    c.append(i)
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, delta = {delta}') # one item it jmped with 32 bytes
    # lists preallocate space and then when it runs out of memory it expands
    # the amount that the list preallocate it gets bigger while the list grows


# Retriving Elements

t = tuple(range(100_000))
l = list(t)
print(timeit('t[99_999]', globals=globals(), number=10_000_000)) # 0.18 - tuples have direct access (refference) to their elements
print(timeit('l[99_999]', globals=globals(), number=10_000_000)) # 0.20 - lists have to access another array that contains pointers to the elements (this is in C python implementation)

