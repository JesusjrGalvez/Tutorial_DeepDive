import math


class Polygon:

    def __init__(self, N, R):
        if N < 3:
            raise ValueError("Number of edges must be greater or equal to 3")
        else:
            self.n = N
            self.radius = R
            self.edges = self.n
            self.vertices = self.n
            self.interior_angle = (self.n-2) * (180/self.n)
            self.edge_length = 2 * self.radius * math.sin(math.pi / self.n)
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


class Polygons:

    def __init__(self, n, r):
        self.polygons = []
        for index in range(3, n):
            self.polygons.append(Polygon(index, r))

    def __getitem__(self, item):
        return self.polygons[item]

    def max_efficiency(self):
        efficiency_dict = {}
        for polygon in self.polygons:
            efficiency = polygon.area//polygon.perimeter
            efficiency_dict[polygon.n] = efficiency
        _max_efficiency = max(efficiency_dict.values())
        max_key = max(efficiency_dict, key=efficiency_dict.get)
        return efficiency_dict, _max_efficiency, max_key


if __name__ == "__main__":
    print("Hello World")
    polygons = Polygons(6, 10)
    print(polygons)
    print(polygons[1])
    a, b, c = polygons.max_efficiency()
    print("hi")



p1 = Polygon(2, 10)
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

