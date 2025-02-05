# Se il numero è pari, lo si divide per 2.
# Se il numero è dispari: moltiplica per 3 e somma 1.

intero = int(input("Inserisci un numero intero positivo: "))

def congettura(n):
    while n != 1:
        print(n, end=" → ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(n)

if intero > 0:
    congettura(intero)
else:
    print("Errore! Inserisci un intero positivo.")