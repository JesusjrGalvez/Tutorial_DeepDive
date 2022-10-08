import math


class Polygon:

    def __init__(self, n, r):
        self.n = n
        self.radius = r
        self.edges = self.n
        self.vertices = self.n
        self.interior_angle = (self.n-2) * (180/self.n)
        self.edge_length = 2 * r * math.sin(math.pi/self.n)
        self.apothem = self.radius * math.cos(math.pi/self.n)
        self.area = 0.5 * self.n * self.edge_length * self.apothem
        self.perimeter = self.n * self.edge_length

    def __repr__(self):
        return f"Polygon({self.n}, {self.radius})"

    #def __str__(self):
    #    return f"Polygon(Number of edges={self.n}, Circumradius={self.radius})"

    def __eq__(self, other):
        if isinstance(other, Polygon):
            if self.n == other.n and self.radius==other.radius:
                return True
            else:
                return False
        else:
            raise TypeError(f"{other} is not a Polygon")

    def __gt__(self, other):
        if isinstance(other, Polygon):
            if self.n > other.n:
                return True
            else:
                return False
        else:
            raise TypeError(f"{other} is not a Polygon")



p1 = Polygon(4, 10)
print(p1.area)
print(p1.edge_length)
print(p1.interior_angle)
print(p1.perimeter)
print(p1)
print(str(p1))

p2 = Polygon(3, 10)
print(p2.radius)

#p3 = (5, 10)
#print(p1 == p3)

if p1 > p2:
    print("p1 is larger than p2")
else:
    print("p1 is smaller than p2")

