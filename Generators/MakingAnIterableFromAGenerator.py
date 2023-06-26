"""
Making an iterable from a generator
"""

def squares_gen(n):
    for i in range(n):
        yield i**2

sq = squares_gen(5)

print(type(sq)) # generator

for num in sq:
    print(num)

print(list(sq)) # is empty exhausted

class Squares:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return squares_gen(self.n)

sq = Squares(5)

for num in sq:
    print(num)

print(list(sq))

class Squares:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return Squares.squares_gen(self.n)

    @staticmethod
    def squares_gen(n):
        for i in range(n):
            yield i**2


sq = Squares(5)
print(list(sq))
print(list(sq))

def squares(n):
    for i in range(n):
        yield i**2

sq = squares(5)
enum_sq = enumerate(sq) # enumerate is lazy an is an iterator
                        # sq is lazy and an iterator

print(list(enum_sq))
print(list(enum_sq)) # now we get nothing back because enumerate is an iterator not an iterbale

sq = squares(5)

next(sq)
next(sq)

print(list(enumerate(sq)))  # it does for the remaning elements