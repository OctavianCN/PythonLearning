
# we can see that when we import a module
# Python first looks for it in sys.modules
# To make the point we put a key/value pair in sys.modules
# and then import it. In fact we put a function there instead of a module
# Python will first look in the cache and immediately just return the object
# if the name is found, basically just as if we had written:
import sys


sys.modules['test'] = lambda: 'Testing module caching'
import test

print(test) # it returns the lambda
test()
print(sys.modules['test'])