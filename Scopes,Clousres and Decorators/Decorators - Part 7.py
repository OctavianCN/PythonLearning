############ Decorating Classes ####################

from fractions import Fraction

f = Fraction(2,3)
print(f.denominator)
print(f.numerator)

# f.speak() not working now

Fraction.speak = 100
print(f.speak) # works

Fraction.speak = lambda self, message: 'Fraction says: {0}'.format(message)
print(f.speak('This is a late parrot'))

f2 = Fraction(10,5)
print(f2.speak('This is called monkey paching')) # we modify classes from outside


Fraction.is_integral = lambda self: self.denominator == 1

f1 = Fraction(2,3)
f2 = Fraction(8,1)
print(f1.is_integral())
print(f2.is_integral())


def dec_speak(cls):
    cls.speak = lambda self, message: '{0} says {1}'.format(self.__class__.__name__,message)
    return cls

Fraction = dec_speak(Fraction)
f1 = Fraction(2,3)
print(f1.speak('hello'))


class Person:
    pass

Person = dec_speak(Person)
p = Person()
print(p.speak('this works!'))


from datetime import datetime,timezone


def info(self):  # here more efficient
    results = []
    results.append('time: {0}'.format(datetime.now(timezone.utc)))
    results.append('Class: {0}'.format(self.__class__.__name__))
    results.append('id: {0}'.format(hex(id(self))))
    for k, v in vars(self).items():
        results.append('{0}: {1}'.format(k, v))
    return results
def debug_info(cls):
    # def info(self): # is not a closure because there are no free variables
    #     results = []
    #     results.append('time: {0}'.format(datetime.now(timezone.utc)))
    #     results.append('Class: {0}'.format(self.__class__.__name__))
    #     results.append('id: {0}'.format(hex(id(self))))
    #     for k,v in vars(self).items():
    #         results.append('{0}: {1}'.format(k,v))
    #     return results
    cls.debug = info
    return cls # it is not technically necessary because the class is mutated
               # but it is needed for the decoration of the class because Person = debug_info(Person)
               # so debug_info should return a class

@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi(self):
        return 'Hello there!'

p = Person('John',1939)
print(p.debug())

@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError('Speed cannot exceed top_speed')
        else:
            self._speed = new_speed

favorite = Automobile('Ford', 'Model T', 1908, 45)
print(favorite.debug())

#favorite.speed = 100 - Exception
favorite.speed = 40
print(favorite.debug())

from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)

p1,p2,p3 = Point(2,3), Point(2,3),Point(0,0)
print(abs(p1))
print(p1 is p2)
print(p2 is p3)
print(p1 == p2) # will be false

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other): # functionality for equal operator
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other): # fun# ctionality for less than operator
        if isinstance(other, Point):
            return  abs(self) < abs(other)
        else:
            return NotImplemented
    # def __le__(self): # this is less than or equal to
    #     pass
    # def __gt__(self, other): # this is grater
    #     pass
    # def __ge__(self,other): # this is greater or equal
    #     pass
    # def __ne__(self, other): # this is not equal
    #     pass
p1,p2,p3 = Point(2,3), Point(2,3),Point(0,0)
print(abs(p1))
print(p1 is p2)
print(p2 is p3)
print(p1 == p2) # now this will be true
print(p3 < p1) # True

p4 = Point(100,100)
print(p4 < p1)
print(p4 > p1) # works (python will check for a greater then
               # don't find it so it do a reflection of lt
#print(p1 <= p4) # this is not working without less than or equal to method

#Now we assume that lt and eq were defined
# and we monkey patch the rest of operations

def complete_ordering(cls): # in this case it is safe to do but usally not recommanded to monkey pach python methods
    if '__eq__' in dir(cls) and '__lt__' in dir(cls): # not a good implementation
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not(self < other) and not(self == other)
        cls.__ge__ = lambda self, other: not (self < other)
    return cls

@complete_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other): # functionality for equal operator
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other): # fun# ctionality for less than operator
        if isinstance(other, Point):
            return  abs(self) < abs(other)
        else:
            return NotImplemented

p1,p2,p3,p4 = Point(2,3), Point(2,3),Point(0,0), Point(100, 200)

print(p1 <= p4)
print(p4 >= p2)

from functools import total_ordering

@total_ordering # it is from standard library and as soon as you have defined two crucial ordering will complete the rest
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other): # functionality for equal operator
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other): # fun# ctionality for less than operator
        if isinstance(other, Point):
            return  abs(self) < abs(other)
        else:
            return NotImplemented

p1,p2,p3,p4 = Point(2,3), Point(2,3),Point(0,0), Point(100, 200)

print(p1 <= p4)
print(p4 >= p2)