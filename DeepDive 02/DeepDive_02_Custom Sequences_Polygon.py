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
    def __init__(self, *pts):
        self._pts = []
        if pts:
            #self._pts = [Point(*pt) for pt in pts]
            for pt in pts:
                self._pts.append(Point(*pt))
        else:
            self._pts = []

    def __repr__(self):
        pts_str = str(self._pts)
        #return "Polygon(" + pts_str.replace("[", "").replace("]", "")+")"
        #return "Polygon("+ pts_str[1:(len(pts_str)-1)] + ")"
        #", ".join([self._pts])
        return "Polygon(" + ", ".join((map(str, self._pts))) + ")"

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, item):
        return self._pts[item]

    def __add__(self, other):
        #self._pts.append(*Polygon(other))
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            #print("new_pts", new_pts)
            #print("*new_pts", *new_pts)
            return Polygon(*new_pts)
            #return Polygon(new_pts[0]) #This doesnt work.
        else:
            raise TypeError(f"{other} is not a Polygon")

    def __iadd__(self, other):
        # This method adds functionality to += operator.
        if isinstance(other, Polygon):
            self._pts = self._pts + other._pts
            return self
        else:
            raise TypeError(f"{other} is not a Polygon")

    def __iadd__(self, other):
        if isinstance(other, Polygon):
            self._pts = self._pts + other._pts
            return self
        else:
            # We assume we are passing an iterable
            points
            self._pts = self._pts + Polygon(other)


p1 = Point(5, 5)
p2 = Point(x=6, y=6)
#print("Test", *p2)
p3 = (3, 3)
#print("Test", *p3)
#pol1 = Polygon(p1, p2)
#print(pol1)

p = Polygon((0,0), (1, 1))

p4 = Polygon(Point(0, 0), Point(1, 1), (2, 2))

p4.__add__(Polygon((4, 4)))


p1 = Polygon((0,0), (1,1))
p2 = Polygon((2,2), (3,3))
print(id(p1), p1)
print(id(p2), p2)
result = p1 + p2
print(id(result), result)
#result2 = p1 + Point(2, 3)
print("===========")
p1 = Polygon((0,0), (1,1))
p2 = Polygon((2,2), (3,3))
print(id(p1), p1)
print(id(p2), p2)
p1 += p2
print(id(p1), p1)

p1 += Point(6, 6)
print(p1)


