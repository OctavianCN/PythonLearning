"""
Iterating Callables
"""


def counter():
    i = 0

    def inc():
        nonlocal i
        i += 1
        return i

    return inc

cnt = counter()

print(cnt())
print(cnt())
print("==============")
# Infinite iterator
class CounterIterator:

    def __init__(self, counter_callable):
        self.counter_callable = counter_callable

    def __iter__(self):
        return self

    def __next__(self):
        return self.counter_callable()

cnt = counter()
cnt_iter = CounterIterator(cnt)

for _ in range(5):
    print(next(cnt_iter))

print("==============")
# Finite iterator

class CounterIterator:

    def __init__(self, counter_callable,sentinel):
        self.counter_callable = counter_callable
        self.sentinel = sentinel

    def __iter__(self):
        return self

    def __next__(self):
        result = self.counter_callable()
        if result == self.sentinel:
            raise StopIteration
        else:
            return result

cnt = counter()

print(type(cnt))
cnt_iter = CounterIterator(cnt, 5)
for c in cnt_iter:
    print(c)

next(cnt_iter) # works is a problem because cnt_iter is not 6 (not equal to 5)

print("==============")
# Finite iterator

class CounterIterator:

    def __init__(self, counter_callable,sentinel):
        self.counter_callable = counter_callable
        self.sentinel = sentinel
        self.is_consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_consumed:
            raise StopIteration
        else:
            result = self.counter_callable()
            if result == self.sentinel:
                self.is_consumed = True
                raise StopIteration
            else:
                return result

cnt = counter()
cnt_iter = CounterIterator(cnt,5)
for c in cnt_iter:
    print(c)
# next(cnt_iter) - now we get exception

print("==============")
# Finite iterator

class CallableIterator:

    def __init__(self, callable_,sentinel):
        self.callable_ = callable_
        self.sentinel = sentinel
        self.is_consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_consumed:
            raise StopIteration
        else:
            result = self.callable_()
            if result == self.sentinel:
                self.is_consumed = True
                raise StopIteration
            else:
                return result

cnt = counter()
cnt_iter = CallableIterator(cnt, 5)
for c in cnt_iter:
    print(c)
help(iter)
print("---------")
cnt = counter()
cnt_iter = iter(cnt, 5)
for c in cnt_iter:
    print(c)

#next(cnt_iter) - exception

print("-----------")

import random
random.seed(0)
for i in range(10):
    print(i, random.randint(0, 10))

random_iter = iter(lambda :random.randint(0, 10), 8)
random.seed(0)
for num in random_iter:
    print(num)

print("=================")

def countdown(start = 10):
    def run():
        nonlocal  start
        start -= 1
        return start
    return run

takeoff = countdown(10)

takeoff_iter = iter(takeoff, -1)
for num in takeoff_iter:
    print(num)