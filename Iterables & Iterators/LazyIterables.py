"""
Lazy Iterables

Lazy Iteration - not calculating something until it is needed
"""

import math


class Circle:

    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self.area = math.pi * (r **2)

c = Circle(1)

print(c.radius)
print(c.area)

c.radius = 2

print(c.area) # area calculated every time we change the radius


class Circle:

    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r

    @property
    def area(self):
        print("Calculating area")
        return math.pi * (self.radius **2)

c =  Circle(1)

print(c.area)
c.radius = 2
print(c.area) # area calculated every time it is requested


class Circle:

    def __init__(self, r):
        self.radius = r
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * (self.radius **2)
            print("Calculating area")
        return self._area

c = Circle(1)
print(c.area)
print(c.area)
c.radius = 2

print(c.area) # area calclculated when it is requested and radius changed ( else it uses the cache)


class Factorials:

    def __iter__(self):
        return self.FactIter()

    class FactIter:
        def __init__(self):
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            result = math.factorial(self.i)
            self.i += 1
            return result

facts = Factorials()

facts_iter = iter(facts)

for _ in range(10): # calculate first 10 factorials using lazy iteration
    print(next(facts_iter))