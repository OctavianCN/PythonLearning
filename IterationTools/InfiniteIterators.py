"""
Infinite Iterators

itertools.count -> lazy iterator

The count function is an infinite iterator
similar to range -> start, step
different from range -> no stop -> infinite
                     -> start and step can be any numeric type float, complex, Decimal, bool False -> 0  True -> 1

Example:
    count(10, 2) -> 10, 12, 14, ...
    count(10.5, 0.1) -> 10.5, 10.6, 10.7, ...
    takewhile(lambda x: x < 10.8, count(10.5, 0.1)) -> 10.5, 10.6, 10.7

itertools.cycle -> lazy iterator

The cycle function allows us to loop over a finite iterable indefinitely

Example:
    cycle(['a', 'b', 'c']) -> 'a', 'b', 'c', 'a', 'b', 'c', ...

If the argument of cycle is itself an iterator -> iterators necomes exhausted
cycle will still produce an infinite sequence -> does not stop after the iterator becomes exhausted

itertools.repeat -> lazy iterator

The repeat function simply yields the same value indefinitely

    repeat('spam') -> 'spam', 'spam', 'spam', ...
Optionally you can specify a count to make the iterator finite
    repeat('spam', 3) -> 'spam', 'spam', 'spam'

Caveat: The items yielded by repeat are the same object, they each reference the same object in memory

"""

from itertools import count, cycle,repeat, islice

###### Count ############

g = count(10) # default step 1

print(list(islice(g, 5)))

# range(10,20,0.5) - not working

g = count(1, 0.5) # the parameters can be any numeric types
print(list(islice(g, 5)))

g = count(1+1j, 1+2j)
print(list(islice(g, 5)))

from decimal import Decimal

g = count(Decimal('0'), Decimal('0.1'))
print(list(islice(g, 5)))

####### Cycle

g = cycle(('red','green', 'blue'))
print(list(islice(g,5)))

def colors():
    yield 'red'
    yield 'green'
    yield 'blue'

cols = colors()
g = cycle(cols)
print(list(islice(g, 10)))
#print(next(cols)) - exhausted

###Example

from collections import namedtuple

Card = namedtuple('Card', 'rank suit')

def card_deck():
    ranks = tuple(str(num) for num in range(2,11)) + tuple('JQKA')
    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    for suit in suits:
        for rank in ranks:
            yield Card(rank,suit)

hands = [list() for _ in range(4)] # 4 empty lists

index = 0
for card in card_deck(): # give a card to each hand
    index = index % 4
    hands[index].append(card)
    index += 1

print(hands) # cards to each hand

# we can do the same by using cycle

hands = [list() for _ in range(4)] # 4 empty lists

index_cycle =cycle ([0, 1, 2, 3])

for card in card_deck():
    hands[next(index_cycle)].append(card)

print(hands)

####### Other way
hands = [list() for _ in range(4)] # 4 empty lists
hands_cycle = cycle(hands)
for card in card_deck():
    next(hands_cycle).append(card)
print(hands)

############# Repeat #########################

g = repeat('Python')
for _ in range(5):
    print(next(g)) # can repeat infinite nr of times

g = repeat('Python', 4)
print(list(g)) # have Python 4 times

hands = [[]] * 4

print(hands) # [[], [], [], []]
print(hands[0] is hands[1]) # True
hands[0].append(10)
print(hands) #[[10], [10], [10], [10]]

g = repeat([] , 4)
g_list = list(g)
print(g_list) # [[], [], [], []]
g_list[0].append(10)
print(g_list) # [[10], [10], [10], [10]] all lists same memory address
