###### Tuples as Data Structures #########


(10, 20, 30) # Homogenious tuple
a = (10, 20, 30)
b = 10, 20, 30

print(type(a))
print(type(b))

def print_tuple(t):
    for e in t:
        print(e)

# print_tuple(10,20,30) not working python think they are pos args
print((10,20,30))

a = 'a', 10, 200,300, 'b', 1, 100
print(a[0])
print(a[2])

print(a[2:5])

a = 2, 3, 'b'

x, y, z  = a

print(x)
print(y)
print(z)


a = 1,2,3,4,5,6,7,8,9

x, *_, y, z = a # _ convention for not caring about the values

print(x) # 1
print(y) # 8
print(z) # 9
print(_) # list of the rest of the elements


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}(x = {self.x}, y = {self.y})'

pt = Point2D(10, 20), Point2D(34, 20)
pt[0].x = 100 # because tuple is immutable you cannot change the reference of pt[0] but you can change pt[0].x
print(pt)

s = 'python'

print(id(s))
s += 'rocks'
print(id(s)) # different + creates a new string

a = 1, 2, 3
print(id(a))
a += (4, 5)
print(id(a)) # this is a new tuple not a changed one

london = 'London', 'UK', 8_780_000 # heteroginious tuple different data types
new_york = 'New York', 'USA', 8_500_000
bucuresti = 'Bucuresti', 'Romania', 2_000_000

cities = [london, new_york, bucuresti] #lists are tiplically homoginious (can be heteroginious but tipyically homogineous)

print(sum(city[2] for city in cities)) # total population

record = 'DJA', 2018, 1, 19, 25_987, 10
first, *_, last = record
print(first, last)
print(_)

for city, country, population in cities: # unpack tuple in for loop
    print(city, country,population)

for index, city in enumerate(cities):
    print(index, city) # index will be 0, 1, 2

from random import uniform
from math import sqrt

def random_shot(radius):
    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)

    if sqrt(random_x ** 2 + random_y ** 2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False

    return random_x, random_y, is_in_circle

num_attempts = 1000000
count_inside = 0

for i in range(num_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1

print(f'Pi is approximately in : { 4 * count_inside / num_attempts}')