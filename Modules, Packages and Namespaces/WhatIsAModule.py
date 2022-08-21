# A Module - is an instance of the module type

def func():
    a = 10
    return a

print(func)

print(globals()) # func is in the main module

f = globals()['func']
print(f is func) # true

print(locals()) # identical to globals
print(locals() is globals()) # True
a = 100
print(globals())
def func():
    a = 10
    b = 10
    print(locals()) # locals have a and b

func()

import math  # import math module

print(math)
import fractions

print(fractions)

junk = math
print(junk.sqrt(2))
print(junk is math) # true

print(globals()['math'])

print(type(globals())) # dict
print(type(math)) # module

print(id(math))
import math
print(id(math)) # same refferences (the module is added into the systemcach)

import sys
print(type(sys.modules)) #dict
print(sys.modules['math']) # find mayh module
print(id(sys.modules['math'])) # same id as before

# when importing a module python first checks if it was loaded
# in sys.modules and if it is present than it dosen't reload it again

print(math.__name__)
print(math.__dict__) # all attributes in math module

f = math.__dict__['sqrt']
print(f(2))

import fractions

print(sys.modules['fractions']) #written in python

print(dir(fractions))

# modules - get loaded from files( not always )
#         - are regular data type (module data type)
#         - they have a namespaces
#         - are a container of global variables
#         - is an execution environment (gets loaded from someware and you can run code inside it)

import types

print(isinstance(fractions, types.ModuleType)) # true
print(isinstance(math, types.ModuleType)) # true

mod = types.ModuleType('test', 'This is a test module')

print(isinstance(mod, types.ModuleType)) # True

print(mod.__dict__)

mod.pi = 3.14
mod.hello = lambda : 'Hello!'
print(mod.__dict__)
print(mod.hello())

# from mod import hello - cannot do it yet mod is a module type but python does not know it is a module