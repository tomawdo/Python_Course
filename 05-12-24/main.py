- creare una lista vuota
- generare un numero random compreso tra 1 e 20
- tramite ciclo for, aggiungere alla lista una quantità di numeri generati casualmente pari al primo numero casuale generato.

import random

# Crea una lista vuota
lista = []

# Genera un numero casuale compreso tra 1 e 20
n = random.randint(1, 20)

# Usa un ciclo for per aggiungere 'n' numeri casuali alla lista
for _ in range(n):
    lista.append(random.randint(1, 20))

# Stampa la lista generata
print(lista)
