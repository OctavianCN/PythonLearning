######## Decorators - Part 1 ########

def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("Function {0} (id={1}) was called {2} times".format(fn.__name__,id(fn),count))
        return fn(*args,**kwargs)
    return inner

def add(a:int,b: int = 0):
    """
        adds two values
    """
    return a+b

help(add)
print(id(add))
print(add(3,6))

add = counter(add) # now we decorated add function (counter return a closure)

print(id(add)) # different id the add function is the closure
help(add) # it's help on function inner
print(add(3,6)) # id of fn will be the id of original add

def mult(a: int, b: int, c: int = 1,*,d):
    """
        multiplies four values
    """
    return  a*b*c*d

print(mult(1,2,3,d=4))
print(mult(1,2,d=3))
help(mult)
mult = counter(mult) # this is called decorating a function count->decorator mult->decorated
help(mult) # all signatures gone

@counter # same thing as my_funct = counter(my_func)
def my_func(s: str,i: int) -> str:
    return s*i

help(my_func)
print(my_func('a',10))
print(mult.__name__) # inner
print(mult.__doc__) # None

def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        """
            this is the inner closure
        """
        nonlocal count
        count += 1
        print("Function {0} (id={1}) was called {2} times".format(fn.__name__,id(fn),count))
        return fn(*args,**kwargs)
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner

@counter
def mult(a: int, b: int, c: int = 1,*,d):
    """
        multiplies four values
    """
    return  a*b*c*d

help(mult) # argumets still incoret using:
           #      inner.__name__ = fn.__name__
           #     inner.__doc__ = fn.__doc__

from functools import wraps # wraps is a closure

def counter(fn):
    count = 0
    @wraps(fn) # v1: fix the documentation of the function decorate inner with wraps by using fn documentation
    def inner(*args, **kwargs):
        """
            this is the inner closure
        """
        nonlocal count
        count += 1
        print("Function {0} (id={1}) was called {2} times".format(fn.__name__,id(fn),count))
        return fn(*args,**kwargs)
    #inner = wraps(fn)(inner) #v2: fix the documentation of the function
    return inner

@counter
def mult(a: int, b: int, c: int = 1,*,d):
    """
        multiplies four values
    """
    return  a*b*c*d

help(mult) # everything is good including signature