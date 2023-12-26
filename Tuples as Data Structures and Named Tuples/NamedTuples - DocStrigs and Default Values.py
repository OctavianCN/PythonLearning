########### Named Tuples - DocStrings and Default Values ##############

from collections import namedtuple

Point2D = namedtuple('Point2D', 'x y')


print(Point2D.__doc__)
print(Point2D.x.__doc__)
print(Point2D.y.__doc__)

help(Point2D)

Point2D.__doc__ = '2D Cartesian coordinate'
Point2D.x.__doc__ = 'x coordinate'
Point2D.y.__doc__ = 'y coordinate'

print(Point2D.__doc__)
print(Point2D.x.__doc__)
print(Point2D.y.__doc__)


### Prototype - for defaults

Vector2D = namedtuple('Vector2D', 'x1 y1 x2 y2 origin_x origin_y')
print(Vector2D._fields)
v1 = Vector2D(0, 0, 10, 10, 0, 0)
print(v1)

vector_zero = Vector2D(0, 0, 0, 0, 0, 0)
v2 = vector_zero._replace(x1= 10, y1=10, x2=20, y2=20)
v3 = vector_zero._replace(x1= 15, y1= 20, x2=12, y2=30)


def func(a, b=10, c=20):
    print(a,b,c)

func(1)
print(func.__defaults__)
func.__defaults__ = (100, 200, 300)
print(func.__defaults__)
func()


print(Vector2D.__new__.__defaults__)
Vector2D.__new__.__defaults__ = (0, 0) # last two arguments are gonna be keyword args
v1 = Vector2D(10, 10, 20)
print(v1)
Vector2D.__new__.__defaults__ = (-10, -10)
v1 = Vector2D(10, 10, 20, 20)
print(v1)