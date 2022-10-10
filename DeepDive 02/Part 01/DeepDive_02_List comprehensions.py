import math
from math import factorial
from itertools import permutations
import itertools as itertools

squares = []

for i in range(10):
    squares.append(i**2)

print(squares)

print("================")
l = [i for i in range(100) if i%2 and i%3 and i%5]
print(l)

print("================")

l = [i for i in range(100) if i%2==0 and i%3==0 and i%5==0]
print(l)

print("================")
#Multiplication table

l = [[i * j for i in range(0, 11)]
     for j in range(0, 11)]

for row in l:
    print(row)

l = []
for j in range(0, 11):
    row = []
    for i in range(0, 11):
        row.append(i*j)
    l.append(row)

print(l)

print("================")

def combo(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

size = 10

pascal = [ [combo(n, k) for k in range(n+1)] for n in range(size+1)]
print(pascal)
for row in pascal:
    print(row)

print("================")

from math import factorial

def combo(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

size = 10  # global variable
pascal = [ [combo(n, k) for k in range(n+1)] for n in range(size+1) ]

for row in pascal:
    print(row)


print("================")

l1 = ['a', 'b', 'c']
l2 = ['1', '2', '3']

l3 = itertools.product(l1, l2)
for i in l3: print(''.join(i))

l3 = list(zip(l1, l2))
print(l3)

l4 = []
for index1, item1 in enumerate(l1):
    for index2, item2 in enumerate(l2):
        if index1==index2:
            l4.append((item1, item2))
        else:
            pass

print("l4")
print(l4)

l5 = [(item1, item2) for index1, item1 in enumerate(l1) for index2, item2 in enumerate(l2) if index1==index2]
print('l5')
print(l5)

print("================")



