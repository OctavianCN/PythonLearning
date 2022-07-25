###########Rational numbers#############

from fractions import Fraction

x = Fraction(3, 4) # 3/4
y = Fraction(22,7)

#Fractions are automatically reduced Fraction(6,10) -> Fraction(3,5)
#Negative sign is always attached to the numerator
# Fraction(1,-4) -> Fraction(-1,4)

#Fraction('10') -> Fraction(10,1)
#Fraction('20/7') -> Fraction(20,7)
print(x.numerator) # 3
print(x.denominator) # 4

# float objects have finite precision => any float object can be written as a fraction
Fraction(0.75) # Fraction(3,4)

import math

x = Fraction(math.pi) # pi is irrational but python will find an aproximation

# Given a Fraction object we can find an approximate equivalent fraction with a constrained denominator using limit_denominator(max_denominator=100000) instance method
print(x)
print(x.limit_denominator(10))