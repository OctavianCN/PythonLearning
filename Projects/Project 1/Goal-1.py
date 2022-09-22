import math
from math import sin, cos, pi

class Polygon:

    def __init__(self, vertices, circumradius):
        if vertices < 3:
            raise ValueError('Polygon must have at least 3 sides')
        self._n = vertices
        self._R = circumradius

    @property
    def edges(self):
        return self._n

    @property
    def vertices(self):
        return self._n

    @property
    def circumradius(self):
        return self._R

    @property
    def interior_angle(self):
        interior_angle = (self._n - 2) * (180 / self._n)
        return interior_angle

    @property
    def edge_length(self):
        s = 2 * self._R * sin(pi / self._n)
        return s
    @property
    def apothem(self):
        a = self._R * cos(pi / self._n)
        return a

    @property
    def area(self):
        return 1/2 * self._n * self.edge_length * self.apothem

    @property
    def perimeter(self):
        return self._n * self.edge_length

    def __repr__(self):
        return f'Polygon(vertices = {self._n}, circumradius = {self._R}'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.edges == other.edges \
                    and self.circumradius == other.circumradius
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.vertices > other.vertices
        else:
            return NotImplemented


# assert - evalutates if an expression is true
def test_polygon():
    rel_tol = 0.001
    abs_tol = 0.001
    try:
        p = Polygon(2, 10)
        assert  False, ('Creating a Polygon with 2 sides:'
                        'Exception expected')
    except ValueError:
        pass
    n = 3
    R = 1
    p = Polygon(n,R)
    print("Testing Polygon")
    assert str(p) == f'Polygon(vertices = 3, circumradius = 1', f'actual: {str(p)}'
    assert p.vertices == n, (f'actual: {p.vertices}, '
                             f'expected: {n}')
    assert p.edges == n
    assert p.circumradius == R
    assert p.interior_angle == 60

    n = 4
    R = 1
    p = Polygon(n, R)
    assert math.isclose(p.interior_angle, 90)
    assert math.isclose(p.area, 2.0,rel_tol=rel_tol,abs_tol=abs_tol),\
                        (f'actual: {p.area}, ' # when you use folats it is not good to use equality because floats are an approximation instead use is_close
                             f'expected: 2.0')
    assert math.isclose(p.apothem, 0.707,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol)

    p1 = Polygon(3, 100)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

test_polygon()
