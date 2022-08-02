######## Closures Applications ############


def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

counter1 = counter()
print(counter1()) # 1
print(counter1()) # 2

def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__,cnt))
        return fn(*args,**kwargs)
    return inner

def add(a, b):
    return a + b
def mult(a, b):
    return a*b

counter_add = counter(add)
print(counter_add.__closure__) # fn and int - free vars
result = counter_add(10,20)
print(result)
result = counter_add(10,20)
print(result)

counter_mult = counter(mult)
print(counter_mult(2,5))
print(counter_mult(3,5))

counters = dict()

def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        # global counters no need for this because it will check at leas the global variable after not finding it in local and nonlocal scopes
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__,cnt))
        counters[fn.__name__] = cnt
        return fn(*args,**kwargs)
    return inner

couter_add = counter(add)
counter_mul = counter(mult)
couter_add(10,20)
couter_add(30,50)
counter_mul(10,20)

print(counters)


def counter(fn,counters): # in order to not hardcode the global dictionary
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__,cnt))
        counters[fn.__name__] = cnt # find counter as a non local variable
        return fn(*args,**kwargs)
    return inner

c = dict()
counter_add = counter(add,c)
counter_mult = counter(mult, c)
counter_add(3,4)
counter_add(5,6)
counter_add(6,8)
counter_mult(5,10)
counter_mult(7,3)

print(c)


def fact(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

fact(3)
fact(5)

counter_fact = counter(fact, c)

print(c)
fact = counter(fact, c) # fact was modified to do something more but it is not the same function
print(fact.__closure__)

fact(10) # it works the same but it was modified from the original function
print(c)
