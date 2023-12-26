import sys

print(sys)

import collections

print(collections)

import importlib # import dinamically

mod_name = 'math'

importlib.import_module(mod_name)

print('math' in sys.modules) # true
print('math' in globals()) # false
#print(math.sqrt(2)) #not working because math was not added  in globals
                     # it was added only in sys.modules

math2 = sys.modules['math'] # import math as math2

print(math2.sqrt(2))

print(math2 is sys.modules['math']) # True


# * finder - finder find where is the module stored - returns a module spec
print(math2.__spec__) # this came from finder
# * loader - after finder tells loader where it is the module stored it loads it compile it execute it and put it in the globals
# finder + loder == importer

print(sys.meta_path) # this are the finders that Python has

#import module1 #  Python will go to all Finders and ask if they know about module 1 and return module.__spec__
# You can add your finder to the meta_path

print(importlib.util.find_spec('decimal')) # ask about the spec of the decimal module

# with open('module1.py', 'w') as code_file:
#     code_file.write("print('running module1.py ..............')")
#     code_file.write("a = 100")
#
# print(importlib.util.find_spec('module1'))
#
# import module1 - works
#
# print('module1' in globals()) # True

# import os
#
# ext_module_path = os.environ('HOMEPATH')
# file_abs_path = os.path.join(ext_module_path, 'module2.py')
#
# with open(file_abs_path, 'w') as code_file:
#     code_file.write("print('running module2.py ..............')")
#     code_file.write("x = 'python")
#
# importlib.util.find_spec('module2') # return nothing

print(sys.path) # python looks for the module name in this paths

# sys.path.append(ext_module_path) - you can append external module path and Python will be able to find that module

# In order to not hardcode the module in sys.path.append use .pth files