# Create a Custom Immutable Sequence Type

my_list = [1, 2, 3, 4, 5]

print(len(my_list))
print(my_list.__len__())

print(my_list[2])
print(my_list.__getitem__(2))

print(my_list[::-1])
print(my_list.__getitem__(slice(None, None, -1)))

for item in my_list:
    print(item ** 2)

index = 0

while True:
    try:
        item = my_list.__getitem__(index)
    except IndexError:
        break
    print(item ** 2)
    index += 1

class Silly:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        print('Called __len__')
    #   return 'this is silly' # error the len method needs to be an integer
        return self.n

    def __getitem__(self, item):
        print(f'You requested item at index {item}')
        if item >= self.n or item < 0:
            raise IndexError # in order to iterate you need this index error
        return 'This is a silly element'

silly = Silly(10)
print(len(silly))

#print(silly.__getitem__(100)) # index error
#print(silly.__getitem__(200)) # this is a sequence where every element is the same

for item in silly:
    print(item)

print([item * 2 for item in silly]) # works

from functools import lru_cache




class Fib:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = self.n + s
            if s < 0 or s >= self.n:
                raise IndexError
            return Fib._fib(s)
        else: # if it is not an int we assume that it is a slice and let python raise the exception if it is not a slice
        #    range_tuple = s.indices(self.n)
        #    print(range_tuple)
            start, stop, step = s.indices(self.n)
            rng = range(start, stop, step)
            return [Fib._fib(i) for i in rng]

    @staticmethod
    @lru_cache(2 ** 10)
    def _fib(n):
        if n < 2:
            return 1
        else:
            return Fib._fib(n - 1) + Fib._fib(n - 2)

fib = Fib(10)
print(list(fib))

print(fib[9])
print(fib[-2])
print(fib[0:4])
print(fib[-1:-4:-1])
