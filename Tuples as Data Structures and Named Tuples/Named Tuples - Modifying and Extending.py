########### Named Tuples - Modifying and Extending ###################

from collections import namedtuple

Point2D = namedtuple('Point2D', 'x y')

pt = Point2D(10,20)

print(id(pt))
pt = Point2D(100, pt.y)
print(id(pt)) # the memory address is changed

Stock = namedtuple('Stock', 'symbol year month day open high low close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
print(djia)

*values, _ = djia
values.append(26_394)
djia = Stock(*values)
print(djia)

a = [1,2,3]
print(id(a))
a += [4,5]
print(id(a)) # the id has changed because of +

a = [1,2,3]
print(id(a))
a.append(4)
print(id(a)) # same id

values = djia[:7]

print(values) # is a tuple

values += (100,) # create a new tuple by concatenating it

djia = Stock(*values)
print(djia)

djia = djia._replace(year=2020) # _replace creates a new tuple with new value
print(djia)

djia = Stock._make(values) # make expects any iterable to create the tuple
print(djia)

print(Point2D._fields)
Point3D = namedtuple('Point3D', Point2D._fields + ('z',))
print(Point3D._fields)

pt3d = Point3D(*pt, 100) #create a point3d with pt values and 100
print(pt3d)