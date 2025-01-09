# creiamo una matrice quadrata 3 x 3
matrix = [
    [4, 5, 2],
    [6, 8, 11],
    [1, 7, 9]
]
somma = 0
for x in matrix:
    for y in x:
        somma += y
        print(y)