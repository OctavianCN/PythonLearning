# Integers - Constructors and Bases

# An integer number is an object - an instance of the int class
# The int class provides multiple constructors
# a = int (10)
# a = int (-10)
# a = int (10.9)   -> truncation a = 10
# a = int (-10.9)  -> truncation a = 10
# a = int (True)    a = 1
# a = int (Decimal("10.9")) -> truncation a = 10
# For strings:
# a = int("10")    a = 10
# int("123")  -> (123) base 10
# With string you have an optional second parameter: base 2 <= base <= 36
# default base = 10
# int("1010", 2) = 10 (print decimal equivalent) int("1010", base = 2) = 10
# int ("A12F", base=16) = 41263 not case sensitive int("a12f", base = 16)
# int("A", base = 11) = 10
# int("B", base = 11) = ValueError, B not valid for base 11

# Reverse Process: changing an integer from base 10 to another base
# built-in functions: bin() bin(10) -> '0b1010' 0b->binary number
#                     oct() oct(10) -> '0o12'
#                     hex() hex(10) -> '0xa'
# The prefixes in the strings help document the base of the number
# These prefixes are consistent with literal integers using a base prefix
a = 0b1010 # number 1010 base 2
a = 0o12
a = 0xA

# What about other bases? - Custom code

# Encodings - Typically we use 0-9 and A-Z for digits required in bases higher than 10
# But we don't have to use letters or even standard 0-9 digits to encode our numbers
# We just need to map between the digits in our number, to a character of our choice

# For Encoding Python uses 0-9 and a-z (case insensitive) and is therefore limited to base <=36
# Choice of characters to represent the digits is your encoding map
# Encoding:
# base b (>=2)
# map = ' ... ' (of length b)
# digits = [...]
# encoding = map[digits[0]] + map[digits[1]] + ...
