# 1 - Scrivi un programma che chiede all'utente
# di inserire un numero intero. Continua a chiedere all'utente
# di inserire un numero finché non viene inserito un numero pari.

while True:
    numero = int(input("Inserisci un numero: "))
    if numero % 2 == 0:
        break

# 2 - Scrivi un programma che stampi i numeri da 1 a 100

n = 1
while n <= 100:
    print(n)
    n += 1



# 3 - scrivi un programma che chieda all'utente di inserire un
# numero intero. Continua a chiederlo finché non inserisce un multiplo di 3

while True:
    n = int(input("Inserisci un numero: "))
    if n % 3 == 0:
        print("Nr. multiplo di 3, grazie.")
        break
    else:
        print("Nr. non multiplo di 3, riprova.")


# 4 - Scrivi un programma che chiede all'utente di inserire una parola.
# Continua a chiedere all'utente di inserire una parola finché la parola
# inserita non è "ciao".

while True:
    parola = str(input("Inserisci una parola: "))
    if parola != "ciao":
        print("Parola sbagliata, riprova.")
    else:
        print("Parola corretta!")
        break


# 5 - Scrivi un programma che stampa i numeri pari da 1 a 100.
n = 1
while n <= 100:
    if n % 2 == 0:
        print(n)
    n += 1


# 6 - Scrivi un programma che chiede all'utente di inserire una lettera.
# Continua a chiedere all'utente di inserire una lettera finché la lettera
# inserita non è una vocale.

while True:
    lettera = str(input("Inserisci una lettera: "))
    if lettera in "aioue":
        break
    else:
        print("Non è una vocale, riprova! ")
        continue


# 7: Scrivi un programma che stampa i numeri multipli di 3 e 25 compresi tra 1 e 1000.

n = 1
while n <= 1000:
    if n % 3 == 0 and n % 25 == 0:
        print(n)
    n += 1


# 8 - Scrivi un programma che chiede all'utente di inserire un numero intero.
# Continua a chiedere all'utente di inserire un numero finché
# non viene inserito un numero intero compreso tra 1 e 100.

while True:
    n = int(input("Inserisci un nr. intero: "))
    if 1 <= n <= 100:
        break


# 9 - Scrivi un programma che chiede all'utente di inserire una parola.
# Continua a chiedere all'utente di inserire una parola finché
# la parola inserita non è lunga almeno 8 caratteri.

while True:
    parola = str(input("Inserisci parola (8 caratteri): "))
    if len(parola) >= 8:
        print("Ottimo!")
        break
    else:
        print("Riprova!")










