"""
Grouping:

Sometimes we want to loop over an iterable of elements but we want to group those elements as we iterate through them

Suppose we have an iterable containing tuples and we want to group based on the first element of each tuple

key -> 1
(1, 10, 100)
(1, 11, 101)
(1, 12, 102)
key -> 2
(2, 20, 200)
(2, 21, 201)
key -> 3
(3, 30, 300)
(3, 31, 301)
(3, 32, 302)

for key, group in groups:
    print(key)
    for item in group:
        print(item)

itertools.groupby(data, [keyfunc]) -> lazy iterator
The groupby function allows us to do precisely that
    -> normally specify keyfunc which calculates the key we want to use for grouping

Here we want to group based on 1st element of each tuple:
    -> grouping key lambda x: x[0]

groupby(iterable, lambda x: x[0]) -> iterator -> of tuples(key, sub_iterator)

The sequence of elements produced from the "sub-iterators" are all produced from the same underlying iterator

groups = groupby(iterable, lambda x: x[0])

next(groups) actually iterates through all the elements of the current "sub-iterator" before proceeding to
            the next group



"""

import itertools

with open('cars_2014.csv') as f:
    for row in itertools.islice(f, 0, 20):
        print(row, end='')

from collections import defaultdict

makes = defaultdict(int)


with open('cars_2014.csv') as f:
    next(f)
    for row in f:
        make, _ = row.strip('\n').split(',')
        makes[make] += 1

for key, value in makes.items():
    print(f'{key}: {value}')

data = (1, 2, 2, 2, 3)

print(list(itertools.groupby(data)))

it = itertools.groupby(data)

for group_key, sub_iter in it:
    print(group_key, list(sub_iter))

data = ((1, 'abc'), (1,'bcd'), (2, 'pyt'), (2, 'yth'), (2, 'tho'), (3, 'hon'))

print(data)

groups = itertools.groupby(data, key=lambda x: x[0])
print(list(groups))
print(list(groups)) # empty now

groups = itertools.groupby(data, key=lambda x: x[0])
for group_key, sub_iter in groups:
    print(group_key, list(sub_iter))

def gen_groups():
    # key = 1
    for key in range(1, 4):
        for i in range(3):
            yield (key, i)

g = gen_groups()

print(list(g))
print(list(g)) # empty

g = gen_groups()

groups = itertools.groupby(g,key= lambda x: x[0])

for group in groups:
    print(group[0], group[1])

print(list(g)) # empty

with open('cars_2014.csv') as f:
    next(f)
    make_groups = itertools.groupby(f, lambda x: x.split(',')[0])

#print(list(make_groups)) # error I/O because make_groups is refferencing f and f is closed (make_group didn't iterate anything yet)
                         # group by is lazy iterator

with open('cars_2014.csv') as f:
    next(f)
    make_groups = itertools.groupby(f, lambda x: x.split(',')[0])
    make_counts = ((key, len(list(models))) for key, models in make_groups)
    print(list(make_counts))

def squares(n):
    for i in range(n):
        yield i**2

sq = squares(5)
i = 0
for item in sq:
    i += 1

print(i)

def len_iterable(iterable):
    i = 0
    for item in iterable:
        i+= 1
    return i

print(sum(1 for i in squares(8)))

print(len_iterable(squares(8)))

with open('cars_2014.csv') as f:
    next(f)
    make_groups = itertools.groupby(f, lambda x: x.split(',')[0])
    make_counts = ((key, len(list(models))) for key, models in make_groups)
    print(list(make_counts))

with open('cars_2014.csv') as f:
    next(f)
    make_groups = itertools.groupby(f, lambda x: x.split(',')[0])
    make_counts = ((key, sum(1 for model in models)) for key, models in make_groups)
    print(list(make_counts))