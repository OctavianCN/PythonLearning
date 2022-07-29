##### Function Introspection ########
#dummy code
i = 100

# TODO: Fix this function
# blablalaallals
def my_func(a: "Mandatory psoitional",
            b: "optional positional" =1,
            c=2,
            *args: "add extra positional",
            kw1,
            kw2=100,
            kw3=200,
            **kwargs: "provide extra kw-only here") -> "does nothing":
    """This funcrtion does nothing but have various parameters
    and annotations"""
    i = 10
    j = 20
    a = i+j
    return a
    # if return not defined it will return None

print(my_func.__doc__)
print(my_func.__annotations__)
my_func.short_description = "this function that does nothing" # add an attribute to the function
print(my_func.short_description)

print(dir(my_func)) # look at attributes of my_func

print(my_func.__name__)

print(id(my_func))
def func_call(f):
    print(id(f))
    print(f.__name__)

func_call(my_func)


print(my_func.__defaults__) # default positional args tuple
print(my_func.__kwdefaults__) # default kw args dictionary

print(my_func.__code__)
print(dir(my_func.__code__))

print(my_func.__code__.co_name) # my func
print(my_func.__code__.co_varnames) # parameters + variables inside my func

print(my_func.__code__.co_argcount) # 3 - show just positional arguments

import inspect
from inspect import isfunction, ismethod, isroutine

a = 10
print(isfunction(a)) # False
print(isfunction(my_func)) # True

print(ismethod(my_func)) # False

class MyClass:
    def f(self):
        pass

print(isfunction(MyClass.f)) # True
my_obj = MyClass()
print(isfunction(my_obj.f)) # False it is a method
print(ismethod(my_obj.f))

print(isroutine(my_obj.f)) # True if you don't care if it is a method or a function
print(isroutine(MyClass.f)) # True


print(inspect.getsource(my_func)) # entire code
print(inspect.getmodule(my_func)) # where is defined my_func
print(inspect.getmodule(print))

import math
print(inspect.getmodule(math))

print(inspect.getcomments(my_func)) # return comments of my func (TODO keyword)

print(inspect.signature(my_func)) # object of type attributes

print(inspect.signature(my_func).return_annotation) # return return annotation

sig = inspect.signature(my_func)
print(sig.parameters) # dictionary

for k, v in sig.parameters.items():
    print(k, type(v))

for param in sig.parameters.values():
    print('Name:', param.name)
    print('Default:', param.default)
    print('Annotation:', param.annotation)
    print('Kind', param.kind)
    print('-------------------')

help(divmod) # divmod(x,y,/) - / means positional only arguments
print(divmod(4,3)) # (1,1)
#print(divmod(x=3,y=3)) - Not working x y are positional only arguments

for param in inspect.signature(divmod).parameters.values():
    print('Kind', param.kind) # Kind is positional only

def my_f(x,y,/):
    print(x,y)

my_f(1,2)
# my_f(x=1,y=2) -> Not working

for param in inspect.signature(my_f).parameters.values():
    print('Kind', param.kind) # Kind is positional only

###### Callables #######

# - is any object that can be called using ()
# - will always return a value (Ex. functions and methods)
# - to see if a object is callable we can use the function: callable

print(callable(print))
print(callable('abc'.upper))
print(callable(str.upper))
print(callable(callable))
print(callable(10))

# Types of callables:
#     - built-in functions print len callable
#     - built-in methods a_str.upper, a_list.append
#     - user defined functions
#     - methods
#     - classes:  - __new__ -> create the object
#                 - __init__
#     - generators, coruoutines

class MyClass:
    def __init__(self,x = 0):
        print("Initialzing ...")
        self.counter = x

print(callable(MyClass)) #true
a = MyClass(100)
print(callable(a)) # False


class MyClass:
    def __init__(self,x = 0):
        print("Initialzing ...")
        self.counter = x
    def  __call__(self, x=1):
        print("Updating counter ..")
        self.counter += x

b = MyClass()
MyClass.__call__(b,10)
print(b.counter)
print(callable(b)) # True
b()
print(b.counter)