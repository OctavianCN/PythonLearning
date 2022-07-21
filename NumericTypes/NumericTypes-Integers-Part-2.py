# Integer Operations

# Integers support all the standard arithmetic operations: +, -, *, /, **
# Resulting type of each operation:
# int + int -> int
# int - int -> int
# int * int -> int
# int ** int -> int
# int / int -> float  (Ex. 3/4 = 0.75 (float), 10/2 = 5 (float))

# Two more operators in integer arithmetic
#      - // floor division (div)
#      - % modulo (mod)
# n = d * (n // d) + (n % d)
#     Ex. 155 = 4 * 38 + 4
#         155 = 4 * (155 // 4) + (155 % 4)

# Floor division
#   - floor of a real number a is the largest ( in standard number order) integer <= a
#   floor(1.999) = 1
#   floor (3.14) = 3
#   floor(2) = 2
#   floor(-3.1) = -4 (largest int less than -3.1)
#   a//b = floor(a/b)

import math

print(type(1+1)) # int
print(type(2*3)) # int
print(type(4-10)) # int
print(type(3 ** 6)) # int
print(type(2/3)) # float
print(type(10/2)) # float

print(math.floor(3.15)) # 3
print(math.floor(3.999999)) # 3
print(math.floor(-3.14)) # -4
print(math.floor(-3.000000001)) # -4
print(math.floor(-3.0000000000001)) # -4
print(math.floor(-3.0000000000000001)) # -3 (float have limited precision)

a = 33
b = 16
print("For a = {0} and b = {1}".format(a,b))
print(a/b) # 2.0625
print(a//b) # 2
print(math.floor(a/b)) # 2

a = -33
b = 16
print("For a = {0} and b = {1}".format(a,b))
print(a/b) # -2.0625
print(a//b) # -3
print(math.floor(a/b)) # -3
print(math.trunc(a/b)) # -2 gives the integer portion of the floating point number
                       # floor != trunc
a = -33
b = -16
print("For a = {0} and b = {1}".format(a,b))
print(a/b)  # 2.0625
print(a//b) # 2
print(math.floor(a/b)) # 2

a = 33
b = -16
print("For a = {0} and b = {1}".format(a,b))
print(a/b) # -2.0625
print(a//b) # -3
print(math.floor(a/b)) # -3

a = 13
b = 4
print('{0}/{1} = {2}'.format(a,b,a/b))
print('{0}//{1} = {2}'.format(a,b,a//b))
print('{0}%{1} = {2}'.format(a,b,a%b))
print( a == b * (a//b) + a%b ) # True

a = -13
b = 4
print('{0}/{1} = {2}'.format(a,b,a/b))
print('{0}//{1} = {2}'.format(a,b,a//b))
print('{0}%{1} = {2}'.format(a,b,a%b))
print( a == b * (a//b) + a%b ) # True