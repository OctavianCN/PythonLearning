"""
Cyclic Iterators

1 2 3 4 5 6 7 8 9 ...

N S W E

1N 2S 3W 4E 5N ....
"""
# Infinite
class CyclicIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.lst[self.i % len(self.lst)]
        self.i += 1
        return result

iter_cycl = CyclicIterator('NSWE')

for _ in range(10):
    print(next(iter_cycl))

#Finite
class CyclicIterator:
    def __init__(self, lst, length):
        self.lst = lst
        self.i = 0
        self.length = length

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.lst[self.i % len(self.lst)]
            self.i += 1
            return result

iter_cycl = CyclicIterator('NSWE', 15)

for item in iter_cycl:
    print(item)


# Infinite
class CyclicIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.lst[self.i % len(self.lst)]
        self.i += 1
        return result

iter_cycl = CyclicIterator([10,20,35])

for _ in range(10):
    print(next(iter_cycl))

numbers = range(1,11)

iter_cycl = CyclicIterator('NSWE')

print(list(zip(list(numbers), iter_cycl)))# 1-N 2-S 3-W 4-E 5-N etc


n = 10
iter_cycl = CyclicIterator('NSWE')
for i in range(1, n+1):
    directorion = next(iter_cycl)
    print(f'{i}{directorion}')

n = 10
iter_cycl = CyclicIterator('NSWE')
items = [ str(i) + next(iter_cycl) for i in range(1,n+1)]

n = 10
iter_cycl = CyclicIterator('NSWE')

items = [str(number)  + direction
            for number, direction  in zip(range(1, n+1),iter_cycl)]

print(items)


print(list(zip(range(1, 11), 'NSWE' * 30))) # will be a list of length 10 and it is not as efficent as cyclic iterator

items = [str(number) + direction
            for number, direction in zip(range(1, n+1),'NSWE' *(n//4 +1))]
print(items)


import itertools

n = 10
iter_cycl = CyclicIterator('NSWE')
items = [f'{i}{next(iter_cycl)}'for i in range(1, n + 1)]

print(items)

n = 10
iter_cycl = itertools.cycle('NSWE')
items = [f'{i}{next(iter_cycl)}'for i in range(1, n + 1)] # same thing as above

help(itertools.cycle) # Return elements from the iterable until it is exhausted. Then repeat the sequence indefinitely.

s = {100, 'a', 'X', 'x', 200}

class CyclicIterator:

    def __init__(self,iterable):
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        iterator = iter(self.iterable)
        item = next(iterator)
        return item

iter_cycl = CyclicIterator('abc')
for i in range(5):
    print(i, next(iter_cycl)) # we will get a every time because we create iterator every time we call next

# class CyclicIterator:
#
#     def __init__(self,iterable):
#         self.iterable = iterable
#         self.iterator = iter(self.iterable)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         item = next(self.iterator)
#         return item
#
# iter_cycl = CyclicIterator('abc')
# for i in range(5):
#     print(i, next(iter_cycl)) # we get stop iteration exception (or nothing because the iterator gets exhausted_


class CyclicIterator:

    def __init__(self,iterable):
        self.iterable = iterable
        self.iterator = iter(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            item =next(self.iterator)
        finally:
            return item

print("=================")
iter_cycl = CyclicIterator('abc')
for i in range(10):
    print(i, next(iter_cycl))