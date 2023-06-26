"""
Yielding and Generators

The yield keyword does the following:
    - it emits a value
    - the function is effectively suspended (but it retains its current state)
    - calling next on the function resumes running the function right after the yield statement
    - if function returns something instead of yielding (finishes running) -> StopIteration exception

Generators:
    - a function that uses the yield statement is called a generator function
    - we can think of functions that contain the yield statement as generator factories
    - the generator is created by Python when the function is called -> gen = my_func()
    - the resulting generator is executed by calling next() -> next(gen)
        the function body will execute until it encounters a yield statement it yields the value
        (as return value of next()) then it suspends itself until next is called againd -> suspended function resumes execution
        if it encounters a return before a yield -> StopIteration exception occurs
    (Remember that if a function terimnates without an explicit return, Python essentially returns
    a None value for us)
    - generators implement iterator protocol
    - generators are inherntly lazy iterators (and can be infinite)
    - generators are iterators, and can be used in the same way (for loops, comprehensions, etc)
    - generators become exhausted once the function returns a value
"""

import math

class FactIter:

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            result = math.factorial(self.i)
            self.i += 1
            return result

fact_iter = FactIter(5)

print(list(fact_iter))
print(list(fact_iter)) # now empty

# next(fact_iter) 0 raise StopIteration

def fact():
    i = 0
    def inner():
        nonlocal i
        result = math.factorial(i)
        i += 1
        return result
    return inner

f = fact()

print(f())#1
print(f())#1
print(f())#2
print(f())#6

fact_iter = iter(fact(), math.factorial(5))# stop at the factorial 5

print(list(fact_iter))

def my_func():
    print('line 1')
    yield 'Flying'
    print('line 2')
    yield 'Circus'

print(type(my_func)) # function

f = my_func() # nothing printed

print(type(f)) # generator

print('__iter__' in dir(f)) # True

print('__next__' in dir(f)) # True

# f is an iterable it implements iterator protocol

print(iter(f) is f) # True

print(f.__next__()) # prin line 1 and it also yield the value Flying

result = f.__next__() # print line 2
print(result) # print Circus

def silly(): # it returns None by default
    yield 'the'
    yield 'ministry'
    yield 'of'
    yield 'silly'
    yield 'walks'

gen = silly()
print(type(gen)) # generator
for line in gen:
    print(line) # works

def silly():
    yield 'the'
    yield 'ministry'
    yield 'of'
    yield 'silly'
    if True:
        return 'Sorry all done!'
    yield 'walks'

print("------")
gen = silly()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#next(gen) # now we get the Stop iteration exception Sorry all done

print("-----------")

def fact(n):
    for i in range(n):
        yield math.factorial(i)

gen = fact(5)
print(next(gen))
print(next(gen))

for num in gen:
    print(num) # consume the remaining elements

print(list(gen)) # exhausted

print("-----------")

def squares(n):
    for i in range(n):
        yield i**2

sq = squares(5)
print(list(sq))


