
# frutta = ["mela", "pera", "uva", "anguria", "melone", "arancia"]
numeri = []

#for i in range(3):
#    input_utente = float(input("Inserisci un numero decimale: ")) # Chiedo di inserire un numero
#    numeri.append(input_utente)
# print(numeri)

# esempio accodamento liste
list1 = 5 *  [0]
list2 = [12,43,26,22,98,46,54]
liste = list1 + list2

list1 = list(range(5,1,-1))

vocali = "aeiou"
listavocali = list(vocali)
# print(listavocali)

listavocali.insert(len(listavocali), "w")
# print(listavocali)

print(listavocali.pop())
print(listavocali)
'''
- creare una lista vuota
- generare un numero random compreso tra 1 e 20
- tramite ciclo for, aggiungere alla lista una quantità di numeri generati casualmente pari al primo numero casuale generato.
'''
import random

lista = []

n = random.randint(1, 20) # Genero un numero casuale compreso tra 1 e 20

for _ in range(n): # Usa un ciclo for per aggiungere 'n' numeri casuali alla lista
    lista.append(random.randint(1, 20))
    if n < 20:
        print(lista)
