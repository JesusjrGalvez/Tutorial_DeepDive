import numbers as numbers


class Point:
    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            #self.x, self.y = x, y
            self._pt = x, y
        else:
            raise TypeError('Point co-ordinates must be real numbers.')

    def __repr__(self):
        return f"Point({self._pt[0]}, {self._pt[1]})"

    def __str__(self):
        return f"Point(x={self._pt[0]}, y={self._pt[1]})"

    def __getitem__(self, s):
        return self._pt[s]


class Polygon:

    def __init__(self, pts):
        pass



p1 = Point(5, 5)
print(p1)
p2 = Point(x=5, y=5)
print(p2.__repr__())


