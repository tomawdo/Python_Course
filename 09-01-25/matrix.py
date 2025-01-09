# creiamo una matrice quadrata 3 x 3
import random

matrix = [
    [4, 5, 2],
    [6, 8, 11],
    [1, 7, 9]
]
somma = 0
for x in matrix:
    for y in x:
        somma += y
        somma = somma + y
        print(y)

matrix_1 = [[random.randint(0, 10) for x in range(3)] for y in range(3)]
print(matrix_1)

