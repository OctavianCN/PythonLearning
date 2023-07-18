"""
Chaining Iterables itertools.chain(*args) -> lazy iterator

This analogous to sequence concatenation but not the same!
    -> dealing with iterables (including iterators)
    -> chaining is itself a lazy iterator

We can manually chain iterables this way iter1 iter2 iter3
for it in (iter1, iter2, iter3):
    yield from it

Or we can use chain as follows:
for item in chain(iter1, iter2, iter3):
 print(item)

Variable number of positional arguments - each argument must be an iterable

Chaining Iterables

What happens if we want to chain from iterables contained inside another, single, iterable?

l = [iter1, iter2, iter3]
chain(l) -> l
What we really want is to chain iter1, iter2 and iter3
We can try this using unpacking: chain(*l) -> produces chained elements from iter1, iter2 and iter3

But unpacking is eager - not lazy

If l was a lazy iterator, we essentially iterated through l ( not the sub iterators), just to unpack!
This could be a problem if we really wanted the entire chaining process to be lazy

itertools.chain.from_iterable(it) -> lazy iterator
We could try this approach
def chain_lazy(it):
 for sub_it in it:
   yield from sub_it

Or we can use chain.from_iterable
chain.from_iterable(it)

This achives the same result:
    -> iterates lazily over it
        -> in turn, iterates lazily over each iterable in it

Copying Iterators itertools.tee(iterable, n)

Sometimes we need to iterate through the same iterator multiple times, or even in parallel
We could create the iterator multiple times manually

iters = []
for _ in range(10):
    iters.append(create_iterator())

Or we can use tee in itertools
    -> returns independent iterators in a tuple

tee(iterable, 10) -> (iter1, iter2, ..., iter10) - all differnet objects

Teeing Iterables

One important thing to note
The elements of the returned tuple are lazy iterators:
    -> always
    -> even if the original argument was not

l = [1, 2, 3, 4]
tee(l, 3) -> (iter1, iter2, iter3) - all lazy iterators not lists!
"""

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

for gen in l1, l2, l3:
    for item in gen:
        print(item)

def chain_iterables(*iterables):
    for iterable in iterables:
        yield from iterable

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

for item in chain_iterables(l1, l2, l3):
    print(item)

from itertools import chain

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

for item in chain(l1, l2, l3):
    print(item)

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))
list_ = [l1, l2, l3]

for item in chain(list_):
    print(item) # is the generator object

for item in chain(list_):
    for i in item:
        print(i)


l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))
list_ = [l1, l2, l3]

for item in chain(*list_):
    print(item)

def squares():
    print(f'yielding 1st item')
    yield (i ** 2 for i in range(4))
    print(f'yielding 2nd item')
    yield (i ** 2 for i in range(4, 8))
    print(f'yielding 3rd item')
    yield (i ** 2 for i in range(8, 12))

for item in chain(*squares()): # this unpaking is not lazy it had to call squares 3 times to get the yield so squares became consumed
    print(item)

def read_values(*args):
    print('finished reading argumenets')

read_values(squares()) # finished reading argumenets
read_values(*squares()) # yielding 1st item, yielding 2nd item, yielding 3rd item finished reading argumenets


c = chain.from_iterable(squares())
for item in c:
    print(item)
"""
yielding 1st item
0
1
4
9
yielding 2nd item
16
25
36
49
yielding 3rd item
64
81
100
121

"""
def chain_iterable(*iterable):
    for item in iterable:
        yield from item

def chain_from_iterable(iterable): # now we expect an iterable
    for item in iterable:
        yield from item

for item in chain_from_iterable(squares()):
    print(item)

##################### Tee ################
from itertools import tee

def squares(n):
    for i in range(n):
        yield i**2

gen = squares(10)

iters = tee(gen, 3)
print(gen) # different from the rest
print(iters) # tree different objects

iter1, iter2, iter3 = iters
# independent copies
print(next(iter1), next(iter1), next(iter1))
print(next(iter2), next(iter2))
print(next(iter3))

l = [1, 2, 3, 4]

lists = tee(l, 2)
print(lists[0]) # is not a list is an iterable

print(list(lists[0]))
print(list(lists[0])) # exhausted