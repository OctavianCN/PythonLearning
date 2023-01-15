"""
Iterators

The iterator Protocol:
    - A protocol is a way of saying that our class is going to implement certain functionality that Python
    can count on

To let Python know our class can be iterated over using __next__ we implement the iterator protocol
The iterator protocol - the class needs to implement two methods:
    - __iter__  - this method should just return the object itself
    - __next__ - this method is responsible for handing back the next element
                from the collection and raising the StopIteration exception when all elements have
                been handed out
If an object is an iterator, we can use it with for loops, comprehensions, etc

Still one issue:
    - The iterator cannot be "restarted"
    Once we habe looped through all items the iterator has been exhausted
    To loop a second time through the collection we have to create a new instance and loop through that
"""

class Squares:

    def __init__(self, length):
        self.length = length
        self.i = 0

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

sq = Squares(3)
print(next(sq))
print(next(sq))
print(next(sq))
# print(next(sq)) - exception

class Squares:

    def __init__(self, length):
        self.length = length
        self.i = 0

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

    def __iter__(self):
        return self

sq = Squares(5)

for item in sq:
    print(item)

for item in sq:
    print(item) # now we get nothing because we exhausted the iterator

# print(next(sq)) - exception

l = ['a', 'b', 'c']
print(list(enumerate(l))) # [(0,'a), (1,'b'),(2,'c')]

s = {100, 'x', 'a', 'X'}
for item in s:
    print(item) # order does not matter

sq = Squares(5)

print(list(enumerate(sq))) # this iterator have order (but we can have iterators that does not have order)
sq = Squares(5)

print(sorted(sq, reverse=True))

sq = Squares(5)

while True:
    try:
        item = next(sq)
        print(item)
    except StopIteration:
        break

class Squares:

    def __init__(self, length):
        self.length = length
        self.i = 0

    def __next__(self):
        print('__next__ called')
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

    def __iter__(self):
        print('__iter__ called')
        return self

sq = Squares(5)
for item in sq: # __iter__ is called first and then __next__ is called
    print(item)

# this is what python is doing in for loop
sq = Squares(5)
sq_iterator = iter(sq)
print(id(sq), id(sq_iterator)) # same object
while True:
    try:
        item = next(sq_iterator)
        print(item)
    except StopIteration:
        break