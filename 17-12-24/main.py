from funzioni import *

'''
# Esercizio 1
operatore = input("Inserisci un operatore (+, -, *, /): ")
n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))

if operatore == "+":
    somma(n1, n2)
elif operatore == "-":
    sottrazione(n1, n2)
elif operatore == "*":
    moltiplicazione(n1, n2)
elif operatore == '/':
    if n2 != 0:
        divisione(n1, n2)
    else:
        print("Errore: divisione per zero.")
else:
    print("Operazione non valida.")


# Eserzio 2
parole = input("Inserisci 5 parole separate da uno spazio: ").split()[:5]
parole_con_esse = filtra_parole_con_esse(parole)

print("Le parole che iniziano con la lettera 's' sono:")
for parola in parole_con_esse:
    print(parola)


# Esercizio 3 - scrivi una funzione che richieda una serie di numeri (lista) e stampi il valore max
numeri = input("Inserisci 5 numeri separati da spazi: ").split()[:5]
numeri = [float(numero) for numero in numeri]
numeri_max(numeri)
'''


# Esercizio 4 - scrivi la versione della funzione len() senza usare len()
# inizializzo la variabile contatore a 0
# definisco una variabile con un argomento
# creo un ciclo for che analizzi tutti gli elementi presenti nell'argomento della variabile
# per ogni elemento presente nell'argoomento della variabile aggiungo 1 e riassegno contatore
# uso return per restituire il valore di contatore
# test funzione su una stringa inserita dall'utente
stringa = input("Inserisci una stringa: ")
print(f"Lunghezza: {lunghezza(stringa)}")
