"""
Iter Function


When iter() is called:
    - Python first looks for an __iter__ method
            -> if it's there, use it
            -> if it's not
                    - look for a __getitem__ method
                        -> if it's there create an iterator object and return that
                        -> if it's not there, raise a TypeError exception (not an iterable)

"""

l = [1, 2, 3, 4]
l_iter = iter(l)
print(type(l_iter)) #list iterator
print(next(l_iter))

class Squares:
    def __init__(self, n ):
        self._n = n

    def __len__(self):
        return self._n

    def __getitem__(self, item): # we are doing a sequence type
        if item >= self._n:
            raise IndexError
        else:
            return item**2

sq = Squares(5)
print(sq[3])
for i in sq:
    print(i)

sq_iter = iter(sq) # return an iterator even if we didn't implement __iter__ function is squares
print(type(sq_iter)) # is an iterator

print(next(sq_iter))

class Squares:
    def __init__(self, n ):
        self._n = n

    def __len__(self):
        return self._n

    def __getitem__(self, item): # we are doing a sequence type
        if item >= self._n:
            raise IndexError
        else:
            return item**2

class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= len(self._sequence):
            raise StopIteration
        else:
            result = self._sequence[self._i]
            self._i += 1
            return result

sq = Squares(5)

sq_iterator = SequenceIterator(sq)
print(next(sq_iterator))
print(next(sq_iterator))
print(next(sq_iterator))

class SimpleIter:
    def __init__(self):
        pass

    def __iter__(self):
        return 'Nope'

s = SimpleIter()
print('__iter__' in dir(s)) # True
#iter(s) - Exception

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

print(is_iterable(s)) # False
print(is_iterable(Squares(5))) # True

