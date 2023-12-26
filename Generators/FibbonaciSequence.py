"""Fibonacci Sequence"""

'''1 1 2 3 5 8 13 ...'''

'''`Fib(n) = Fib(n-1) + Fib(n-2)
Fib(0) = 1
Fib(1) = 1'''
from timeit import timeit

def fib_recursive(n):
    if n <= 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


print([fib_recursive(i) for i in range(7)])

print(timeit('fib_recursive(30)', globals=globals(), number=10))

from functools import lru_cache

@lru_cache()
def fib_recursive(n):
    if n <= 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

print(timeit('fib_recursive(30)', globals=globals(), number=10))

#print(timeit('fib_recursive(2000)', globals=globals(), number=10)) maximum recursion depth exceeded

def fib(n):
    fib_0 = 1
    fib_1 = 1
    for i in range(n-1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1

print(timeit('fib(5000)', globals=globals(), number=10))


class FibIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            result = fib(self.i)
            self.i += 1
            return result

fib_iter = FibIter(7)

for num in fib_iter:
    print(num)

def fib_gen(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1
    yield fib_1
    for i in range(n-2):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1

gen = fib_gen(7)
for num in gen:
    print(num)

print(timeit('list(FibIter(5000))', globals=globals(), number=1))#0.7340902910000295
print(timeit('list(fib_gen(5000))', globals=globals(), number=1)) #0.00052624999989348