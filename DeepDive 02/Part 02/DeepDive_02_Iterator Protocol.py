from collections import namedtuple

class Cities:
    def __init__(self):
        self._cities = ['New York', 'London', 'Madrid', 'Paris']

    def __len__(self): # OJO es __len__ no __length__
        return len(self._cities)

    def __iter__(self):
        print('calling Cities __iter__ 1')
        return self.CityIterator(self)

    class CityIterator:
        def __init__(self, city_obj):
            print('calling CityIterator __init__ 2')
            self.city_obj = city_obj
            self.index = 0
            self.length = len(self.city_obj)

        def __iter__(self):
            print('calling CityIterator __iter__ 0')
            return self

        def __next__(self):
            if self.index >= self.length:
                print('calling CityIterator __next__ 4')

                raise StopIteration
            else:
                print('calling CityIterator __next__ 3')

                result = self.city_obj._cities[self.index]
                self.index += 1
                return result

cities = Cities()

for city in cities:
    print(city)


class Cities:
    def __init__(self):
        self._cities = ['Madrid', 'Barcelona']

    def __len__(self):
        self.length = len(self._cities)

    def __iter__(self):
        return self.CityIterator(self)

    class CityIterator:
        def __init__(self):
            pass

        def __iter__(self):
            return self

        def __next__(self):
            if self.index >= self.length:
                raise StopIteration
            else:
                result = self._cities
                self.index += 1
                return result


color_dict = {'red': 124, 'green': 82, 'blue': 167}
print(color_dict)

Color = namedtuple('Color', ['red', 'green', 'blue'])
print(Color)

colors = []
color = Color(255, 255, 255)
color_02 = Color(123, 125, 193)

colors.append(color)
colors.append(color_02)
print(colors)
color__ = Color[255, 20, 155] # this does not work
print(color)
print(color.green)