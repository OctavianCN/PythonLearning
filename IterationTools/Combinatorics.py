"""
The itertool module contains a few functions for generating permutations and combinations

It also has a function to generate the Cartesian products of multiple iterables
All these functions return lazy iterators

Cartesian Product

{1, 2, 3} x {a, b, c}

Let's say we want to generate the Cartesian product of two lists:
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c', 'd']

def cartesian_product(l1, l2):
    for x in l1:
        for y in l2:
            yield (x,y)

cartesian_product(l1, l2) -> (1, 'a'), (1, 'b'), (1, 'c'), (1, 'd'), ..., (3, 'd')

itertools.product(*args) -> lazy iterator

product(l1, l2) -> (1, 'a'), (1, 'b'), (1, 'c'), (1, 'd'), ..., (3, 'd')

l3 = [ 100, 200]

product(l1, l2, l3) -> (1, 'a', 100), (1, 'a', 200) ..., (3,'d', 200)

Permutations

This function will produce all the possible permutations of a given iterable
In addition, we can specify the length of each permutation -> maxes out at the length of the iterable

itertools.permutations(iterable, r=None)
    -> r is the size of the permutation
    -> r = None means length of each permutation is the length of the iterable

Elements of the iterable are considered unique based on their position, not their value
-> if iterable produces repeat values then permutations will have repeat values too

Combinations

Unlike permutations, the order of elements in a combination is not considered -> OK to always sort the elements of a combination

Combinations of length r, can be picked from a set
    -> without replacement -> once an element has been picked from the set it cannot be picked again
    -> with replacement -> once an element has been picked from the set it can be picked again

itertools.combinations(iterable, r)
itertools.combinations_with replacement(iterable, r)

Just like for permutations the elements of an iterable are unique based on their position, not their value
The different combinations produced by these functions are sorted based on the original ordering in the iterable
"""

import itertools

def matrix(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            yield f'{i} x {j} = {i*j}'

print(list(itertools.islice(matrix(10), 10, 20)))

l1 = ['x1', 'x2', 'x3', 'x4']
l2 = ['y1', 'y2', 'y3', 'y4']

for x in l1:
    for y in l2:
        print((x,y), end=' ')
    print('')

print(list(itertools.product(l1,l2)))

def matrix(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            yield (i,j,i*j)

def matrix(n):
    for i,j in itertools.product(range(1, n+1), range(1, n+1)):
        yield (i, j, i*j)

print(list(matrix(4)))

def matrix(n):
    return ((i, j, i*j)
            for i,j in itertools.product(range(1, n+1), range(1, n+1)))

print(list(matrix(4)))

from itertools import tee

def matrix(n):
    return ((i, j, i*j)
            for i,j in itertools.product(*tee(range(1, n+1), 2)))

print(list(matrix(4)))

def grid(min_val, max_val, step, *, num_dimensions = 2):
    axis = itertools.takewhile(lambda x: x<= max_val,
                        itertools.count(min_val, step))
    axes = itertools.tee(axis, num_dimensions)
    return itertools.product(*axes)

print(list(grid(-1, 1, 0.5, num_dimensions=3)))

sample_space = list(itertools.product(range(1, 7), range(1, 7)))
print(sample_space)

outcomes = list(filter(lambda x: x[0] + x[1] == 8, sample_space))
print(outcomes)

print(len(outcomes)/len(sample_space))

from fractions import Fraction
odds = Fraction(len(outcomes), len(sample_space))
print(odds)
### Permutations

l1 = 'abc'
print(list(itertools.permutations(l1)))

print(list(itertools.permutations(l1, 2)))

l1 = 'abca'
print(list(itertools.permutations(l1)))

### Combinations

print(list(itertools.combinations([1,2,3,4], 2))) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
print(list(itertools.combinations_with_replacement([1,2,3,4], 2))) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]


SUITS = 'SHDC'
RANKS = tuple(map(str, range(2, 11))) + tuple('JQKA')

deck = [rank + suit for suit in SUITS for rank in RANKS]

print(deck[0:5])

print(list(itertools.product(SUITS, RANKS)))

deck = [rank + suit for suit, rank in itertools.product(SUITS,RANKS)]

from collections import namedtuple

Card = namedtuple('Card', 'rank suit')

deck = [Card(rank, suit)
        for suit,rank in itertools.product(SUITS,RANKS)]

print(deck[0:5])

deck = [Card(rank, suit)
        for suit,rank in itertools.product(SUITS,RANKS)]

sample_space = itertools.combinations(deck, 4)

total = 0
acceptable = 0

for outcome in sample_space:
    total += 1
    for card in outcome:
        if card.rank != 'A':
            break
    else: # no break: if for finish without the break then else will be executed
        acceptable += 1

print(f'total = {total}, acceptable = {acceptable}')
print('odds = {}'.format(Fraction(acceptable, total)))
print('odds = {:.10f}'.format(acceptable/total))


deck = [Card(rank, suit)
        for suit,rank in itertools.product(SUITS,RANKS)]

sample_space = itertools.combinations(deck, 4)

total = 0
acceptable = 0

for outcome in sample_space:
    total += 1
    if all(map(lambda x: x.rank == 'A', outcome)):
        acceptable += 1

print(f'total = {total}, acceptable = {acceptable}')
print('odds = {}'.format(Fraction(acceptable, total)))
print('odds = {:.10f}'.format(acceptable/total))
