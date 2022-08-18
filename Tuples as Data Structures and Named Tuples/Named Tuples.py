####### Named Tuples #########

class Point3D: # if you want immutability a better way is to use named tuples
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

from collections import namedtuple # namedtuple is a class

Point2D = namedtuple('Point2D', ['x', 'y']) # valid names identifiers and don't start with _

pt1 = Point2D(10, 20)
print(pt1)

pt3d_1 = Point3D
print(pt3d_1) # needs to implemet a __repr__ to get a nice display

Pt2D = namedtuple('Point2D', ('x', 'y'))

pt2 = Pt2D(10,20)
print(pt2)

p = Point3D(x=10,y=20,z=30)
print(isinstance(p,tuple)) # false
p = Point2D(x=10, y= 20)
print(isinstance(p,tuple)) # true - Point2D inheart from tuple

a = (10, 20)
b = (10, 20)
print(a is b) # False
print(a == b) # True

pt1 = Point2D(10, 20)
pt2 = Point2D(10, 20)
print(pt1 is pt2) # False
print(pt1 == pt2) # True

pt1 = Point3D(1,2,3)
pt2 = Point3D(1,2, 3)
print(pt1 is pt2) # False
print(pt1 == pt2) # False

pt1 = Point2D(10, 20)
pt2 = Point3D(10, 20, 30)

print(max(pt1))
#print(max(pt2)) # not workig Point3D not an iterable

def dot_product_3d(a,b):
    return a.x * b.x + a.y*b.y + a.z*b.z

pt1 = Point3D(1,2,3)
pt2 = Point3D(1,1,1)
print(dot_product_3d(pt1,pt2))

a = (1,2)
b = (1,1)
print(list(zip(a,b)))

def dot_product(a,b):
    return sum(e[0] *  e[1] for e in zip(a,b))

print(dot_product(a,b))

Vector3D = namedtuple('Vector3D', 'x y z')
v1 = Vector3D(1,2,3)
v2 = Vector3D(1,1,1)

print(dot_product(v1,v2))

print(v1[0:2])

Circle = namedtuple('Circle', 'center_x center_y    radius')

c = Circle(0,0,10)
print(c)
print(c.radius)

Stock = namedtuple('Stock', ''' symbol year month 
                 day open high low close''')

djia = Stock('DJIA', 2018 ,1, 25,26_313,26_458, 26_260,26_393) # 26_313 = 26313
for item in djia:
    print(item)
x, y = p
print(x)
print(y)

symbol, year, month, day, *_, close =djia

print(year)
print(_) # rest of the values

#Person = namedtuple('Person', 'name age _ssn') #Error field names cannot start with underscore (named tuples disallow it because have a propriety rename to rename invalid args)
Person = namedtuple('Person', 'name age _ssn', rename=True)
print(Person._fields) # name age _2
print(Point2D._fields)
print(Stock._fields)

# print(c._source) # source code of class stock (removed in python 3.7)

d = djia._asdict() # convert named tuple to dictionary

print(d) # dictionary guarantee the key order in the latest versions of python