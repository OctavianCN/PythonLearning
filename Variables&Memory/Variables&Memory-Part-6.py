###############Python Optimization Interning##################
import sys

a = 10 # same reference
b = 10 # same reference
print(hex(id(a)))
print(hex(id(b)))

a = 500 # Depends on the Python if is CPython will have different reference but now it have the same
b = 500
print(hex(id(a)))
print(hex(id(b)))


# Interning - reusing objects on-demand
# At startup, Python(CPython) pre-loads a global list of integers
# in range [-5,256]
# Any time an integer is referenced in that range, Python will use the
# cached version of that object
a = 10 # Python just have to point tot the existing reference for 10
a = 257 # Python does not use that global list and a new object is created

a = 10
b = int(10)
c = int('10')
d = int('1010',2)
print(id(a),id(b),id(c),id(d)) # same id

#############String Interning######################

# Some strings are automatically interned - but not all
# As the Python code is compiled identifiers are interned:
# - variable names                  Identifiers:
# - function names                      - must start with _ or a letter
# - class names                         - can only contain _, letters and numbers
# etc.
# Interning - it's all about optimization

a = "some_long_string"
b = "some_long_string"

print(a==b) # is compared character by character
print(a is b) # if we know that "some_long_string) has been interned than you can comapre the memory addresses ( much faster)

# Not all strings are automatically interned by Python
# But you can force string to be interned sys.intern() method

a = sys.intern('the quick brown fox')
b = sys.intern('the quick brown fox')
c = 'the quick brown fox'
d = 'the quick brown ' + 'fox'
print(a is b)
print(a is c) # usually when you intern one instance of a string you have to intern every instance of that string
print(a is d) # True for this version of python but not everytime
print(a == d) # True
# When should you do this: - dealing with large number of strings that could have high repetition (Ex. NLP)
#                          - lots of string comparisons

def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    print('Is a b? ( from equals)')
    print(a is b) # False it is not automatically interning
    for i in range(n):
        if a == b:
            pass

def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('a long string that is not interned' * 200)
    print('Is a b? (from interning)')
    print(a is b)
    for i in range(n):
        if a is b:
            pass

import time

start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()
print('equality', end - start)

start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()
print('interning', end - start)