numeri = [3, 15, 8, 23, 7, 12, 19, 5, 17]

def maggiori_di_10(lista):
    count = 0
    for numero in lista:
        if numero > 10:
            count += 1
    return count

result = maggiori_di_10(numeri)
print(f"Numeri maggiori di 10: {result}")