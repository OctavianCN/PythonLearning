####Parameters Default - Notes 2#######

def add_item(name, quantity, unit, grocery_list):
    grocery_list.append("{0} ({1} {2})".format(name, quantity,unit))
    return grocery_list

store1 = []
store2 = []

add_item('bannana',2,'kg',store1)
add_item('milk',1, 'liter',store1)

print(store1)

add_item('python',1,'medium-rare',store2)

print(store2)
del store1
del store2
# For mutable types
def add_item(name, quantity, unit, grocery_list=[]): #default list already created (this run once)
    grocery_list.append("{0} ({1} {2})".format(name, quantity,unit))
    return grocery_list

store1 = add_item('bannana',2,'kg') # store1 will be created (mutated)
add_item('milk',1, 'liter',store1) # now store1 is created
print(store1)

store2 = add_item('python',1,'medium-rare')
print(store2) # we have the items from store1 in store2

print(store1 is store2) # True

#Solution:

def add_item(name, quantity, unit, grocery_list=None):
    if not grocery_list:
        grocery_list = [] # this code will run everytime the function is called (dfifferent function scope each time)
    grocery_list.append("{0} ({1} {2})".format(name, quantity,unit))
    return grocery_list

store1 = add_item('bannana',2,'kg')
add_item('milk',1, 'liter',store1)
print(store1)

store2 = add_item('python',1,'medium-rare')
print(store2)

print(store1 is store2) # False


# Exemple when we want the same memory address at function param

def factorial(n):
    if n < 1:
        return 1
    else:
        print('calculating {0}'.format(n))
        return n*factorial(n-1)

print(factorial(3))

#Not user friendly but better than before
def factorial_v2(n,*,cache):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}'.format(n))
        result = n * factorial_v2(n-1, cache = cache)
        cache[n] = result
        return result

cache = {}
print(factorial_v2(3,cache = cache))
print(factorial_v2(3,cache = cache)) # no more calculation
print(factorial_v2(4,cache = cache)) # will calculate just 4!

# Good for cache already created (memorazation)
def factorial_v3(n,cache = {}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}'.format(n))
        result = n * factorial_v3(n-1)
        cache[n] = result
        return result

print(factorial_v3(3))
print(factorial_v3(3))
print(factorial_v3(4))