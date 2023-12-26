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

    def __setitem__(self, s, value):
        try:
            rhs = [Point(*pt) for pt in value]
            is_single = False
        except TypeError:
            try:
                rhs = Point(*value)
                is_single = True
            except TypeError:
                raise TypeError('Invalid Point or iterable of Points')

        if isinstance(s, int) and is_single \
            or (isinstance(s, slice) and not is_single):
            self._pts[s] = rhs
        else:
            raise TypeError('Incompatible index/slice assignment')

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('can only concatenate with another Polygon')

    def __delitem__(self, s):
        del self._pts

    def pop(self, i):
        return self._pts.pop(i)

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

p = Polygon((0,0), (1,1), (2,2))
print(id(p), p)

print(p[0:2])
p[0:2] = [(10, 10), Point(20, 20), [30, 30]]
print(id(p), p)
p[0] = Point(10, 10)
print(id(p), p)

# p[0:2] = Point(20, 20)
# p[0] = [Point(10, 10), Point(20, 20)]

p = Polygon((0,0), (1,1), (2,2), (3,3))
# p[0] = [(0,0), (1,1)]
# p[0:2] = Point(0, 0)
# p[0] = ('a', 'b')
print(p.pop(2))
print(p)