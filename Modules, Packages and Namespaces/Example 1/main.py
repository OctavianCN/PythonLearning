import sys

print(' ========================')
print('Running main.py - module name: {0}'.format(__name__))

#now the code for module1 will get executed
import module1 # module name will not be main will be module1 (if you run module1.py the module name is __main__

print(module1)
print(module1.print_dict('main.globals', globals()))

print(sys.path)
print(sys.modules['module1'])

print('importing module1 again')
import  module1 # this will not run Python will just look in the cache

# del globals()['module1'] - delete a module

print('=========================')