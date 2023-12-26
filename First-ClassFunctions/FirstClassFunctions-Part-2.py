#######DOCSTRINGS AND ANNOTATIONS#############

# Docstrings

help(print)   # returns some documentation for print

#  If the first line in the function body is a string ( not assigned, or comment)
# just a string, it will be interpreted as a docstring

def my_func(a):
    "documentation for my_func"
    return a

help(my_func)

# Where are docstirng stored -> In the function __doc__property

def func(n):
    # comment -> it is not compiled and then the docstring remains the first line
    """ Multiline string is the best way
       to write documentation for your functions""" # it is not ignored by python interpreter
    return n

print(func.__doc__) # where documentation is stored
help(func) # returns function header and then doc string


# Function Annotations

def my_func(a: 'annotation for a',
            b: 'annotation for b' = 1) -> 'annotate return value':
    """documentation for my func"""
    return a*b

help(my_func)
print(my_func.__doc__) # just documentation
print(my_func.__annotations__) # just annotation

x = 3
y = 5

def my_func(a: 'some character', b = max(x,y)) -> 'character a repeated ' + str(max(x,y)) + ' times':
# def my_func is evaluated just one time if  x or y change they are
# not changing in the function parameters (in annotations)
        print(b)
        return a * max(x,y)

print(my_func('a'))
print(my_func.__annotations__)
x = 10
print(my_func('a')) # it is a 10 times
print(my_func.__annotations__) # it still says 5 times even if the max is 10


def my_func(a: str,
            b: 'int > 0' = 1,
            *args: 'some extar poz args',
            k1: 'keyword only arg 1',
            k2: 'keyword only arg 2' = 100,
            **kwargs: 'some extra keyword args') -> 'something':
    print(a,b,args,k1,k2,kwargs)
# annotations don't change your code
help(my_func)
print(my_func.__annotations__)
my_func(1,2,3,4,5,k1=10,k3=300,k4=200)