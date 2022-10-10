import math


class Polygon:

    def __init__(self, N, R):
        assert N >= 3, "N is not greater or equal to 3"
        self._n = N
        self._radius = R

    def __repr__(self):
        return f"Polygon({self._n}, {self._radius})"

    @property
    def count_vertices(self):
        return self._n

    @property
    def count_edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._radius

    @property
    def interior_angle(self):
        return (self._n - 2) * (180 / self._n)

    @property
    def edge_length(self):
        return 2 * self._radius * math.sin(math.pi / self._n)

    @property
    def apothem(self):
        return self._radius * math.cos(math.pi / self._n)

    @property
    def area(self):
        return 0.5 * self._n * self.edge_length * self.apothem

    @property
    def perimeter(self):
        return self._n * self.edge_length

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self._n == other._n and self._radius == other._radius:
                return True
            else:
                return False
        else:
            # what this does is that it checks if self == other, but if it can't do it, it will reverse
            # and check if other == self.
            return NotImplemented
            #raise TypeError(f"{other} is not a Polygon")

    def __gt__(self, other):
        if isinstance(other, Polygon):
            if self._n > other._n:
                return True
            else:
                return False
        else:
            return NotImplemented
            #raise TypeError(f"{other} is not a Polygon")


p1 = Polygon(3, 10)
print(p1.area)
print(p1.edge_length)
print(p1.interior_angle)
print(p1.perimeter)
print(p1)
print(str(p1))

p2 = Polygon(4, 10)
print(p2.circumradius)
# print(p2.radius)
