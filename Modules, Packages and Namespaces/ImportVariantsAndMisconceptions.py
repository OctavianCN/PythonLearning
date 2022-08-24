

import sys

for key in sorted(sys.modules.keys()):
    print(key) # alot of standard libraries are loaded with sys

print('cmath' in sys.modules) # False

print('cmath' in globals()) #False

from cmath import exp


print('cmath' in globals()) #False
print('exp' in  globals()) # True

print('cmath' in sys.modules) # True

cmath = sys.modules['cmath']

print('cmath' in globals()) # True
from math import sin
print(sin) # this is sin function from math
from cmath import * #every single symbol from cmath in gloabal
print(sin) # now it is overwritten with the one from cmath
         # problem solution using alias as c_sin
print(globals())

## Efficiency

def my_func(a):
   import math # math loaded to the local namespace of my_func
   return math.sqrt(a)


######## To Be Done ########