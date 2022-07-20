##########Python Optimization - Peephole#############

24 * 60 # Python will actually pre-caluclate 24 * 60 -> 1440 and store it in memory

(1, 2) * 5 # is less than 20 in length and it is gonna get pre-calculated and stored

'the quick brwon fox' * 10 # is more than 20 characters and it is not gonna be stored

e = 1
if e in [1, 2, 3]:  # in this case [1,2,3] is constand and is replaced by its immutable counterpart
    pass            # [1,2,3] list is replaced to (1,2,3) tuple
#lists -> tuples
#sets -> frozensets

# Set membership is much faster than list or tuple membership (sets are basically like dictionaries)

# instead of using: e in [1,2,3] or e in (1,2,3)
# write e in {1,2,3} - much faster

def my_func():
    a = 24 * 60
    b = (1,2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 5
    f = ['a', 'b'] * 3

print(my_func.__code__.co_consts) # show the constats that were precalculated

def my_func(e):
    if e in [1,2,3]:
        pass

print(my_func.__code__.co_consts) # list [1,2,3] becomes (1,2,3) mutable -> immutable

def my_func(e):
    if e in {1,2,3}:
        pass

print(my_func.__code__.co_consts) # set {1,2,3} to frozenset({1,2,3})

import string
import time

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

print(char_list)
print(char_tuple)
print(char_set) # no order and no duplicates

def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass
start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print('list', end - start)

start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print('tuple', end - start)
start = time.perf_counter()

membership_test(10000000, char_set)
end = time.perf_counter()
print('set', end - start)