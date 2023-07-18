"""
Slicing

itertools.islice

We know that we can slice sequence types seq[i:j:k]
                                         seq[slice(i,j,k)]

We can also slice general iterables (including iterators of course)

-> islice(iterable, start, stop, step)

form itertools import isclice

l = [1, 2, 3, 4]
result = islice(l, 0, 3)
list(result) -> [1, 2, 3]

-> islice returns a lazy iterator
list(result) -> []
"""


l  = [1,2,3,4,5]
print(l[0:2])

s = slice(0,2)
print(l[s])

import math

def factorials(n):
    for i in range(n):
        yield math.factorial(i)

facts = factorials(100)

#print(facts[0:2]) # not working

def slice_(iterable, start, stop):
    for _ in range(0,start):
        next(iterable)
    for _ in range(start,stop):
        yield next(iterable)

print(list(slice_(factorials(100),0, 10)))

print(list(slice_(factorials(100),3, 10)))

from itertools import islice

print(list(islice(factorials(100),3,10)))

help(islice)

print(list(islice(factorials(100),5))) # 5 is the end
print(list(islice(factorials(100),3, 10, 2)))

def factorials():
    index = 0
    while True:
        print(f'yielding factorial ({index} ) ...')
        yield math.factorial(index)
        index += 1

facts = factorials()
for _ in range(0,5):
    print(next(facts))

print(islice(factorials(),3, 10)) # iterable not starting iterate yet

print(list(islice(factorials(),3, 10)))

facts = factorials()
islice(facts, 0, 5)

next(facts)
next(facts)

print(list(islice(facts, 0, 5))) # the first two elements of facts were consumed

print(next(facts)) # the previous elements of facts were consumed