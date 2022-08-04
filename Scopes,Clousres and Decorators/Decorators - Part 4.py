###### Decorator Application (Memoization) ###############

def fib(n):
    print('Calculation fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) * fib(n-2)

print(fib(10))


class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self,n):
        if n not in self.cache:
            print('Calculating fib({0})'.format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]

f = Fib()
print(f.fib(10))

def fib():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            print('Calculating fib({0})'.format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]

    return calc_fib

f = fib()
print(f(10))

def memoize(fn):
    cache = dict()
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner

@memoize
def fib(n):
    print('Calculation fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) * fib(n-2)

print(fib(10))
print(fib(10))
print(fib(11))

@memoize
def fact(n):
    print('Calculating {0}!'.format(n))
    return 1 if n < 2 else n* fact(n-1)

print(fact(6))
print(fact(7))

from time import perf_counter

start = perf_counter()
fib(35)
end =perf_counter()
print(end - start)

from functools import lru_cache # least recently used cache

@lru_cache(maxsize=8) # lru cache is the best for using cache for fucntions (more efficient if maxsize power of 2) if None unlimited cache
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(10))
print(fib(11))
print(fib(8))
print(fib(16))
print(fib(1)) # now fib 1 should be recalculated because it expiered (maxsize=8)