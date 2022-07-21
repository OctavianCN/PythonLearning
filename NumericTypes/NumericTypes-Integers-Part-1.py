###############Integers###############

# int data type: Ex: 0, 10, -100, ...
# Integers are represented internally using binary (base 2)
# Largest integer in base 10 using 8 bits is: 255 (if we don't care about negative numbers)
# If we care about negative numbers the largest number is 127 ( first bit is the sign bit)
# Since 0 does not require a sign we can squeeze out an extra number
# so with 8 bits we can represent a range of [-128, 127] numbers [-2^7, 2^7 -1]
# so for n bits you can get a range of  [-2^(n-1),2^(n-1)-1] numbers
# unsigned integer it would be double because we don't care about ngative numbers [0,2^n]

# In a 32-bit OS:
#    memory spaces(bytes) are limited by their address number -> 32 bits
#    2^32 (4 GB) bytes of addressable memory

# So how large an integer can be depends on how many bits are used to store the number
# Some languages (Java, C ..) provide multiple distinct integer data types that use a fixed number of bits:
# Java: Byte ( signed 8 bit numbers [-128,127],short 16 bit numbers, int 32 bit numbers, long 64 bit numbers etc...)
# Some languages lets you define unsinged variables ( only positive numbers wider range)

# Python does works this way:
# int - object uses a variable number of bits
# Can use 4 bytes, 8 bytes, 12 bytes etc..
# ints are actually objects
# Python integer - theoretically limited only by the amount of memory available
# larger numbers = more memory and standard operators +,* etc will run slower
import sys

print(type(100))
print(sys.getsizeof(0)) # everytime you create an integer you will use at least 24 bytes ( 1 byte = 8 bits)

print(sys.getsizeof(1)) # 28 bytes = 24 bytes ( overhead) + 4 bytes to actually store the int
print(sys.getsizeof(2**1000)) # 160 bytes - ( 160 - 24 ) * 8 bits to store this value

import time

def calc(a):
    for i in range(10000000):
        a * 2
# the larger the number the slower the operation:

start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end - start) # aprox: 0.22128404200000001

start = time.perf_counter()
calc(2**100)
end = time.perf_counter()
print(end - start) # aprox: 0.384672791

start = time.perf_counter()
calc(2**10000) # aprox: 6.014865041999999
end = time.perf_counter()
print(end - start)


