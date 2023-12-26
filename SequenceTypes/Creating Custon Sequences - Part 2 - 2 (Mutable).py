import numbers

class Point:

    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = x, y
        else:
            raise TypeError('Point co-ordinates must be real numbers')

    def __repr__(self):
        return f'Point( x = {self._pt[0]}, y = {self._pt[1]})'

    def __len__(self):
        return len(self._pt)

    def __getitem__(self, s):
        return self._pt[s]


p1 = Point(10, 2)
x, y = p1
print(x, y)
print("---")
p2 = Point(*p1)
print(p1, id(p1))
print(p2, id(p2))

class Polygon:

    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]

    def __repr__(self):
        pts_str = ', '.join(str(pt) for pt in self._pts)
        return f'(Polygon({pts_str}))'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('can only concatenate with another Polygon')

    def append(self, pt):
        self._pts.append(Point(*pt))

    def insert(self, i, pt):
        self._pts.insert(i, Point(*pt))

    def extend(self, pts):
        if isinstance(pts, Polygon):
            self._pts += pts._pts
        else:
            points = [Point(*pt) for pt in pts]
            self._pts += points

    def __iadd__(self, other):
        self.extend(other)
        return self

p = Polygon((0, 0), Point(1, 1))
print(p)
p1 = Polygon(Point( x = 0, y = 0), Point( x = 1, y = 1))

p1 = Polygon((0, 0), (1, 1))
p2 = Polygon((2, 2), (3, 3))
print(id(p1), id(p2))
result = p1 + p2
print(id(result),result)

p1 = Polygon((0, 0), (1, 1))
p2 = Polygon((2, 2), (3, 3))
print(id(p1), p1)
print(id(p2), p2)
p1 += p2
print(id(p1), p1)
p1 += [(2,2), (3,3), Point(4, 4)]
print(id(p1), p1)

p1 = Polygon((0, 0), (1, 1))
p2 = Polygon((2, 2), (3, 3))
print(id(p1), p1)
print(id(p2), p2)
p1.append([10,10])
print(id(p1), p1)
p1.insert(1, Point(-1, -1))
print(id(p1), p1)
p1.extend(p2)
print(id(p1), p1)

p1.extend([(0,0), Point(10, 10)])
print(id(p1), p1)

