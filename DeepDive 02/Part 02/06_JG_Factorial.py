import math


def main():
    class Factorial:
        def __init__(self, length):
            self.length = length

        def __iter__(self):
            return self.FactorialIterator(self.length)

        class FactorialIterator:
            def __init__(self, length):
                self.length = length
                self.index = 0

            def __iter__(self):
                return self

            def __next__(self):
                if self.index >= self.length:
                    raise StopIteration
                else:
                    result = math.factorial(self.index)
                    self.index += 1
                    return result

    f1 = Factorial(10)
    for index, value in enumerate(f1):
        print(f"{index+1}, {value}")
    print(f1)

def main2():
    class Factorial:
        def __iter__(self):
            return self.FactorialIterator()

        class FactorialIterator:
            def __init__(self):
                self.index = 0

            def __iter__(self):
                return self

            def __next__(self):
                result = math.factorial(self.index)
                self.index += 1
                return result

    f1 = Factorial(10)
    for index, value in enumerate(f1):
        print(f"{index+1}, {value}")
    print(f1)





if __name__ == '__main__':
    main()