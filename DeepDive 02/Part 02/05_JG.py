import itertools


def main():
    class CyclicIterator:
        def __init__(self, lst):
            # print('calling CyclicIterator__init__ 1')
            self.lst = lst
            self.i = 0

        def __iter__(self):
            # print('calling CyclicIterator__iter__ 2')
            return self

        def __next__(self):
            #print('calling CyclicIterator__next__ 3')
            result = self.lst[self.i % len(self.lst)]
            # 0 % 3 = 0
            # 1 % 3 = 1
            # 2 % 3 = 2
            # 3 % 3 = 0
            # 4 % 3 = 1
            self.i += 1
            return result

    directions = CyclicIterator('NESW')
    lst = []
    for i in range(10):
        direction = next(directions)
        a = f"{i}{direction}"
        lst.append(a)

    print(lst)


def main2():
    n = 10
    iter_cycl = itertools.cycle('NSWE')
    directions = []
    for i in range(1, n+1):
        directions.append(f'{i}{next(iter_cycl)}')
    print([f'{i}{next(iter_cycl)}' for i in range(1, n + 1)])
    print(directions)

    for i,j in zip(range(10), iter_cycl):
        print(i, j)


if __name__ == "__main__":
    main2()
