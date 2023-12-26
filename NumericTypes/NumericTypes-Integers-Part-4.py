# Integers - Constructors and Bases

print(type(10))
help(int)
a = int()
print(a) # 0
print(int(10.5)) # 10
int(10.999999) # 10
int(True) # 1
int(False) # 0
import fractions

a = fractions.Fraction(22,7)
print(a) # 22/7
print(float(a)) # 3.14..
print(int(a)) # 3

print(int("12345")) # 12345
print(int("101", 2)) # 5
print(int("FF", 16)) # 255
print(int("ff", 16)) # 255

print(bin(10)) # 0b1010
print(oct(10)) # 0o12
print(hex(10)) # 0xa

a = int('101',2)
b = 0b101
print(a is b) # True
print(a == b) # True


# Custom base conversions

def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError("Number n must be >= 0")
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        # m, n = n % b, n //b
        n, m = divmod(n,b)
        digits.insert(0, m)
    return digits

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode the digits")
    #encoding = ''
    #for d in digits:
    #    encoding += digit_map[d]
    #return encoding
    encoding = ''.join([digit_map[d] for d in digits])
    return encoding
print(from_base10(10, 2))
print(encode(from_base10(255, 16), '0123456789ABCDEF'))
