######## Reducing Functions ###########


l = [5,8,6,10,9]

_max = lambda a,b: a if a > b else b

def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result

print(max_sequence(l))

_min = lambda a,b: a if a<b else b

def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result

print(min_sequence(l))


# Instead of doing the first two function we should make them more generic


def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result

print(_reduce(_max,l))
print(_reduce(_min,l))
# _reduce(_max, {1,2,3,4}) not working for sets

from functools import reduce # python have built in reduce functions

print(reduce(_max,l))
print(reduce(_min,l))
print(reduce(_max,{1,2,3,4,5,6,0,10})) # works now

# python built in functions (when you create with def functions with same name as built in functions you overwrite them)

print(min(l))
print(max(l))
print(max({3,4,10,0}))
print(sum(l))
print(sum({1,5,3,0,10}))

s = {True, 1,0, None}
print(all(s)) # False if all are true then return true else return false
print(any(s)) # True if any of items are true retruns true

l = [5,8,6,10,9] # calculate the multiply of elements

print(reduce(lambda a,b: a*b, l, 1)) # last item is default value