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

class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area is None:
            print('Calculating area...')
            self._area = math.pi * self.radius ** 2
        return self._area



if __name__=='__main__':
    print('hello world')
    c1 = Circle(1)
    print(c1.area)