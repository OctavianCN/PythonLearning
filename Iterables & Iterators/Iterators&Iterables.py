"""
Iterators & Iterables

The collection is iterable but the iterator is responsible for iterating over the collection

The iterable is created once
The iterator is created every time we need to start a fresh iteration

Iterable:

An iterable is a Python object that implemets the iterable protocol
The iterable protocol requires that the object implement a single method:

__iter__ - returns a new instance of the iterator object used to iterate over the iterable

Iterators vs Iterables:

Iterables: - impleents: __iter__ -> returns an iterator
Iterator:  - implements: __iter__ -> returns itself
                         __next__ -> returns the next element

Iterators are themselves iterables but they are iterables that become exhausted
Iterables on the other hand never become exhausted
"""

class Cities:

    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._cities):
            raise StopIteration
        else:
            item = self._cities[self._index]
            self._index += 1
            return item

cities = Cities()

print(type(cities))
print(list(enumerate(cities)))
#print(next(cities)) - exception

class Cities:

    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']
        self._index = 0

    def __len__(self):
        return len(self._cities)

class CityIterator:

    def __init__(self, city_obj):
        self._city_obj = city_obj
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._city_obj):
            raise StopIteration
        else:
            item = self._city_obj._cities[self._index]
            self._index += 1
            return item

cities = Cities()
city_iterator = CityIterator(cities)
for city in city_iterator:
    print(city)

# in order to iterate again the cities you have to recreate just the City Iterator

# Now we implement the iterable protocol

class Cities:

    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']
        self._index = 0

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        print('Cities __iter__ called')
        return CityIterator(self)

class CityIterator:

    def __init__(self, city_obj):
        print('City iterator new object')
        self._city_obj = city_obj
        self._index = 0

    def __iter__(self):
        print('City iterator __iter__ called')
        return self

    def __next__(self):
        print('City iterator __next__ called')
        if self._index >= len(self._city_obj):
            raise StopIteration
        else:
            item = self._city_obj._cities[self._index]
            self._index += 1
            return item
cities = Cities()

# works because city is an iterable now
for city in cities:
    print(city)

for city in cities:
    print(city)

print("-------------------------")
city_iter_1 = cities.__iter__()
city_iter_2 = cities.__iter__()

print(city_iter_1 is not city_iter_2)

for city in city_iter_1:
    print(city)

for city in city_iter_1:
    print(city) # Now we get nothing back

del CityIterator
del Cities
print("================================")
class Cities:

    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']
        self._index = 0

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        print('Cities __iter__ called')
        return self.CityIterator(self)

    class CityIterator: # nested class

        def __init__(self, city_obj):
            print('City iterator new object')
            self._city_obj = city_obj
            self._index = 0

        def __iter__(self):
            print('City iterator __iter__ called')
            return self

        def __next__(self):
            print('City iterator __next__ called')
            if self._index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item

cities = Cities()

for city in cities:
    print(city)

print(list(enumerate(cities)))

print(sorted(cities, key = lambda x: len(x)))

cities_iterator = cities.__iter__()

for city in cities_iterator:
    print(city)

for city in cities_iterator: # now cities iterator is exhausted
    print(city)

s = {'a', 100, 'x', 'X'}

print(s.__iter__())
print(iter(cities))
print(iter(s))
set_iterator = iter(s) # get the iterator

for item in set_iterator:
    print(item)


print("====================================")
# This class is an iterable and now we make it a sequence type as well
class Cities:

    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']
        self._index = 0

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        print('Cities __iter__ called')
        return self.CityIterator(self)

    def __getitem__(self, s): # implemanted sequance protocol
        print('getting item ...')
        return self._cities[s]

    class CityIterator: # nested class

        def __init__(self, city_obj):
            print('City iterator new object')
            self._city_obj = city_obj
            self._index = 0

        def __iter__(self):
            print('City iterator __iter__ called')
            return self

        def __next__(self):
            print('City iterator __next__ called')
            if self._index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item

cities = Cities()
print(cities[0])

for city in cities: # Use iterable protocol ( if else it will use the sequence protocol)
    print(city)