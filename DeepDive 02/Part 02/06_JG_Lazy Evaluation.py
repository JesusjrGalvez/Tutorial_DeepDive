import math


#
# class Circle:
#     def __init__(self, r):
#         self.radius = r
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, r):
#         self._radius = r
#         self.area = math.pi * r ** 2


### Example of LAZY EVALUATION.

class Circle:
    def __init__(self, r):
        self.radius = r
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None  # If a new radius is set, make area = None, so that it gets calculated again if asked.

    @property
    def area(self):
        if self._area is None:
            print('calculating area... ')
            self._area = math.pi * self.radius ** 2
        return self._area



if __name__ == '__main__':
    print('hello world')
    c1 = Circle(1)
    print(c1.area)
    print(c1.area)
    c1.radius = 2
    print(c1.area)
