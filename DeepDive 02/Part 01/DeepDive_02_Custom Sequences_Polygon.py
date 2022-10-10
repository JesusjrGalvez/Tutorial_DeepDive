import numbers as numbers


class Point:
    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            #self.x, self.y = x, y
            self._pt = x, y
        else:
            raise TypeError(f'Coordinates {x, y} must be real numbers.')

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
            #self._pts = [Point(*pt) for pt in pts] # This is another way of doing it.
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

    # This allows pol1 + pol2 functionality.
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
            print("HI")
            print(other)
            points = [Points(*pt) for pt in other]
            print(points)
            self._pts = self._pts + points
            return self

p1 = Point(1, 1)
p2 = Point(2, 2)
pol1 = Polygon(p1, p2)
print(pol1)
pol2 = Polygon((3, 3))
print(pol2)


def foo(a, *b):
    print(a)
    print(b)

foo(5, 6, 7)
# # pol3 = pol1 + pol2
# # print(pol3)
# # pol4 = Polygon(4, 4)
#
# l = [i for i in range(10) if i%2 and i%3]
# print(l)

l = [ [i*j for j in range(5)] for i in range(5)]
print(l)