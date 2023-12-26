############# Iterating Collections ################



s = {'x', 'y', 'b', 'c', 'a'}

for item in s:
    print(item) # order not the same because s is not a sequence type (no concept of the first element)

#print(s[0]) not working

class Squares:
    def __init__(self):
        self.i = 0

    def next_(self):
        result = self.i ** 2
        self.i += 1
        return result

sq = Squares()
print(sq.next_())
print(sq.next_())
print(sq.next_())
print(sq.next_())

sq = Squares()
for i in range(5):
    print(sq.next_()) # this is an infinite collection


class Squares:
    def __init__(self,length):
        self.i = 0
        self.length = length

    def next_(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

    def __len__(self):
        return self.length


sq = Squares(3)
print(len(sq))
print(sq.next_())
print(sq.next_())
print(sq.next_())
#print(sq.next_()) # exception
print("---------------")
sq = Squares(10)
while True:
    try:
        print(sq.next_())
    except StopIteration:
        break

class Squares:
    def __init__(self,length):
        self.i = 0
        self.length = length

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

    def __len__(self):
        return self.length
print("------------")
sq = Squares(3)
print(next(sq))
print(sq.__next__())
while True:
    try:
        print(next(sq))
    except StopIteration:
        break

# for item in sq: - not working it is not an iterable
#     print(sq)

import random


class RandomNumbers:

    def __init__(self, length, *, range_min=0, range_max=10):
        self.length = length
        self.range_min = range_min
        self.range_max = range_max
        self.num_requested = 0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.num_requested >= self.length:
            raise StopIteration
        else:
            self.num_requested += 1
            return random.randint(self.range_min, self.range_max)

numbers = RandomNumbers(3)
print(next(numbers))
print(next(numbers))
print(next(numbers))

numbers = RandomNumbers(10)
while True:
    try:
        print(next(numbers))
    except StopIteration:
        break
