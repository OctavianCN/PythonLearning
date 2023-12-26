"""
Aggregators:

Functions that iterate through an interable and return a single value (usually) takes into account
every element of the iterable

min(iterable) -> minimum value in the iterable
max(iterable) -> maximum value in the iterable
sum(iterable) -> sum of all the values in the iterable


Associated Truth Values:

Every object in Python has an associated truth value bool(obj) -> True/False

Every object has a True value, except:
- None
- False
- 0 in any numeric type (eg: 0, 0.0, 0 + 0j, ..)
- empty sequences (eg: list,tuple,string,..)
- empty mapping types (eg: dictionary, set, ..)
- custom classes that implement a __bool__ or __len__
method that returns False or 0

The any and all functions:

any(iterable) -> returns True if any (one or more) element in iterable is truthy
              -> False otherwise

all(iterable) -> returns True if all the elemets in iterable are truthy
              -> False otherwise

Leveraging the any and all functions:

Often, we are not particulary intereested in the direct truth value of the elements in our iterables

-> want to know if any, or all, satisfy some condition -> if the condition is True

A function that takes a single argument and returns True or Flase is called a predicate

We can make any and all more useful by first applying a predicate to each element of the iterable

Example:

    Suppose we have some iterable l = [1, 2, 3, 4, 100]
    and we want to know if: every element is less than 10

First define a suitable predicate: pred = lambda x: x < 10

Apply this predicate to every element of the iterable:
    results = [pred(1), pred(2), pred(3), pred(4), pred(100)]

Then we use all on these results all(results) -> False

How do we apply that predicate?

The map function: map(fn, iterable) -> applies fn to every element of iterable
A comprehension: (fn(item) for  item in iterable)

Or even:

new_list = []
for item in iterable:
    new_list.append(fn(item))


"""


def squares(n):
    for i in range(n):
        yield i**2

print(list(squares(5)))
print(min(squares(5)))
print(max(squares(5)))
print(sum(squares(5)))

sq = squares(5)
print(min(sq)) # now sq is exhausted
# print(max(sq)) # exhausted

print(bool(10))# True
print(bool(0+0j))# False
print(bool(0+1j))#True

sq = squares(5)
print(min(sq))
print(bool(sq)) # True

class Person:
    pass

p = Person()
print(bool(p))# True

class Person:
    def __bool__(self):
        return False

p = Person()
print(bool(p)) # False

class Person:
    def __bool__(self):
        return False

p  = Person()
print(bool(p)) # False


class Person:
    def __bool__(self):
        return True

    def __len__(self):
        return 0


p = Person()
print(bool(p)) # True - first check bool and if not exist check len if both not exist returns True by default

class MySeq:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self): # just for implementing sequence protocols
        pass

my_seq = MySeq(0)

print(bool(my_seq)) # False

my_seq = MySeq(10)
print(bool(my_seq)) # True


print(any([0,'',None])) # False

print(any([0,'',None, 1]))# True

print(all([0,'',None, 1]))# False

print(all([10,'hello'])) # True


###########Example 1######################

from numbers import Number

print(isinstance(10,Number)) # True
print(isinstance(10.5,Number)) # True

print(isinstance(2+3j,Number)) # True

from decimal import Decimal

print(isinstance(Decimal('10.5'), Number)) # True

print(isinstance('100.5',Number)) # False

print(isinstance([10,20], Number))# False

l = [10, 20, 30, 40]

is_all_numbers = True
for item in l:
    if not isinstance(item,Number):
        is_all_numbers = False
        break

print(is_all_numbers)

l = [10, 20, 30, 40]

def is_numeric(v):
    return isinstance(v, Number)

pred_l = map(is_numeric, l)

print(list(pred_l))

pred_l = (is_numeric(item) for item in l)

print(list(pred_l))

pred_l = map(lambda x: isinstance(x,Number), l)

print(list(pred_l))

print(all(pred_l))

###### Example 2 ######################

with open('car-brands.txt') as f:
    for row in f:
        print(len(row), row, end='')

with open('car-brands.txt') as f:
    result = all(map(lambda row: len(row) >= 4, f)) # if all brand have more than 3 characters ( 4 because the last one is \n)
    print(result)

with open('car-brands.txt') as f:
    result = any(map(lambda row: len(row) > 10, f)) # if any brand have more than 10 characters
    print(result)