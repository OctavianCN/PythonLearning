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
        return f'Polygon(vertices = {self._n}, circumradius = {self._R})'

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

class Polygons:

    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [ Polygon(i,R) for i in range(3, m+1)]

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f'Polygons(m = {self._m}, R={self._R})'

    def __getitem__(self, item):
        return self._polygons[item]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons,
                                 key= lambda p: p.area / p.perimeter,
                                 reverse=True)
        return sorted_polygons[0]




polygons = Polygons(8, 1)

print(len(polygons))
print(polygons)

for p in polygons:
    print(p)

for p in polygons[2:5]:
    print(p)

print(polygons.max_efficiency_polygon)