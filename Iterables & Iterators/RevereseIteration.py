"""
Reversed Iteration
"""

_SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
_RANKS = tuple(range(2,11)) + tuple('JQKA')

from collections import namedtuple

Card = namedtuple('Card', 'rank suit')

class CardDeck:
    def __init__(self):
        self.length = len(_SUITS) * len(_RANKS)

    def __len__(self):
        return self.length

    def __iter__(self):
        return self.CardDeckIterator(self.length)

    class CardDeckIterator:
        def __init__(self, length):
            self.length = length
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                suit = _SUITS[self.i // len(_RANKS)]
                rank = _RANKS[self.i % len(_RANKS)]
                self.i += 1
                return Card(rank, suit)

deck = CardDeck()

for card in deck:
    print(card)
print("-------------")
print("Get last 7 cards from the deck")
deck = list(CardDeck())

print(deck[:-8:-1]) # it is wastefull because in order to get the last 7 cards you have
                    # to create a list of all cards and then use only just a few


l = [1, 2, 3, 4]

print(list(reversed(l)))

#reversed_deck = reversed(CardDeck()) # not working right now  have to implement __reversed__ method




class CardDeck:
    def __init__(self):
        self.length = len(_SUITS) * len(_RANKS)

    def __len__(self):
        return self.length

    def __iter__(self):
        return self.CardDeckIterator(self.length)

    def __reversed__(self):
        return self.CardDeckIterator(self.length, reverse = True)

    class CardDeckIterator:
        def __init__(self, length, reverse = False):
            self.length = length
            self.i = 0
            self.reverse = reverse

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                if self.reverse:
                    index = self.length - 1 - self.i
                else:
                    index = self.i
                suit = _SUITS[index // len(_RANKS)]
                rank = _RANKS[index % len(_RANKS)]
                self.i += 1
                return Card(rank, suit)
print("===================")
deck = reversed(CardDeck())
for card in deck:
    print(card)


print("SEQUENCES")

class Squares:
    def __init__(self, length):
        self.squares = [i**2 for i  in range(length)] # instead of this it would be better if we would use lazy get item

    def __len__(self):
        return len(self.squares)

    def __getitem__(self, item):
        return self.squares[item]

for num in Squares(5):
    print(num)

for num in reversed(Squares(5)):
    print(num) # works (Python reverse function can reverse a sequence type but not an iterable) - but it needs the length of the sequence (if len is not implemented it wouldn't work)

reverse_iter = iter(reversed(Squares(5)))
print("-------")
for i in reverse_iter:
    print(i)
print("--------")
for i in reverse_iter:
    print(i) # it is exhaausted
print("---------")
print(f'Reverse iter = {type(reverse_iter)}')
# reversed function - returns an iterator

class Squares:
    def __init__(self, length):
        self.squares = [i**2 for i  in range(length)] # instead of this it would be better if we would use lazy get item

    def __len__(self):
        return len(self.squares)

    def __getitem__(self, item):
        return self.squares[item]

    def __reversed__(self):
        print('__reversed__ called')
        return 'Hello Python!'

for num in Squares(5):
    print(num)

for num in reversed(Squares(5)):
    print(num)

reverse_iter = reversed(Squares(5))

print(type(reverse_iter)) # a string because string is iterable (if it would be an int it wouldn't work)
