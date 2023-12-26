import os

def create_module_file(module_name, **kwargs):
    """
        Create a module file named <module_name>.py
        Module has a single function that will print the suppliked kwargs
    """
    module_file_name = f'{module_name}.py'
    module_rel_file_path = module_file_name
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'w') as f:
        f.write(f'# {module_name}.py \n\n')
        f.write(f"print('running {module_file_name}...')\n\n")
        f.write(f'def print_values():\n')
        for key, value in kwargs.items():
            f.write(f"\tprint('{str(key)}', '{str(value)}')\n")

create_module_file('test', k1=10, k2='python')

import test

test.print_values()

create_module_file('test', k1 = 10, k2='python',k3 = 'cheese')

import test

test.print_values() # still get the original 2 without changes

import sys

print('test' in sys.modules) # True

del sys.modules['test'] # delete test from sys module

print('test' in sys.modules) # False

# this is not a good approch because if test was reloaded somehere else in the code
# it would still have the same refference of the old module
import test # reimport test
test.print_values()


print(id(test))
create_module_file('test', k1 = 10, k2 = 'python', k3 = 'cheese', k4 = 'parrots')

import importlib

importlib.reload(test)

print(id(test)) # same address as before it changed only the content at that memory address ( the content was mutated)

test.print_values()

create_module_file('test2', k1 = 'python')
from test2 import print_values

print("test2" in globals()) # False
print('test' in sys.modules) # True

create_module_file('test2', k1 = 'python', k2 = 'cheese')

#importlib.reload(test2) # not working test2 not in globals

importlib.reload(sys.modules['test2'])

print_values() # still prints the old version (the print values still refference the old one)

# so you have to do
print_values = sys.modules['test2'].print_values # works but it could break somone else code
print_values()

# Conclusion: Reload Not Safe