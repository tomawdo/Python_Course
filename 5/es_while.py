# 1 - Scrivi un programma che chiede all'utente
# di inserire un numero intero. Continua a chiedere all'utente
# di inserire un numero finché non viene inserito un numero pari.
'''
while True:
    numero = int(input("Inserisci un numero: "))
    if numero % 2 == 0:
        break

# 2 - Scrivi un programma che stampi i numeri da 1 a 100

n = 1
while n <= 100:
    print(n)
    n += 1

'''

# 3 - scrivi un programma che chieda all'utente di inserire un
# numero intero. Continua a chiederlo finché non inserisce un multiplo di 3

while True:
    n = int(input("Inserisci un numero: "))
    if n % 3 == 0:
        print("Nr. multiplo di 3, grazie.")
        break
    else:
        print("Nr. non multiplo di 3, riprova.")