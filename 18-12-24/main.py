# creare una lista la cui dimensione è decisa dall'utente sia il minimo e sia il massimo dei numeri
# popolare la lista con numeri generati random che rientrano nel range definito
# es: lunghezza lista: 5, num_minimo, num_massimo


import random

# Input dall'utente
lunghezza_lista = int(input("Inserisci la lunghezza della lista: "))
num_minimo = int(input("Inserisci il numero minimo: "))
num_massimo = int(input("Inserisci il numero massimo: "))

# Controllo per garantire che il massimo sia maggiore o uguale al minimo
if num_minimo > num_massimo:
    print("Errore: il numero minimo non può essere maggiore del numero massimo.")
else:
    # Creazione della lista con numeri random
    lista_random = [random.randint(num_minimo, num_massimo) for _ in range(lunghezza_lista)]
    print("Lista generata:", lista_random)