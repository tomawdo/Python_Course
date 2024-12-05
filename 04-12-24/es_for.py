# Scrivere un programma che utilizzi un loop for per stampare ogni elemento di una lista.
macchine = ["Fiat", "VW", "Renault", "Volvo"]

for brand in macchine:
    print(brand)


# Scrivere un programma che utilizzi un loop for per stampare tutti i numeri da 1 a 10.
for n in range(1, 11):
    print(n)


# Scrivere un programma che utilizzi un loop for per sommare tutti i numeri in una lista.
numeri = [1, 23, 14, 7, 21]
somma = 0

for n in numeri:
    somma += n
print(f"Il totale della somma è: {somma}")


# Scrivere un programma che utilizzi un ciclo for per stampare tutti i numeri pari da 1 a 20.
for numero in range(2, 21, 2): # range(start, stop, step)
    print(numero)


# Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di una stringa.
saluto = "Buongiorno a tutti!"

for lettera in saluto:
    print(lettera)


# Scrivere un programma che utilizzi un loop for per stampare tutte le chiavi di un dizionario.
dizionario = {
    "nome" : "Mario",
    "cognome" : "Rossi",
    "eta" : 36
}

for chiave in dizionario:
    print(chiave)


# Scrivere un programma che utilizzi un loop for per stampare tutte le coppie chiave-valore di un dizionario.
for chiave, valore in dizionario.items(): # La funzione items() restituisce coppie chiave-valore
    print(chiave + ":", valore) # Stampa ogni chiave seguita dal suo valore


# Scrivere un programma che utilizzi un ciclo for per stampare tutte le lettere di ogni stringa in una lista.
lista_parole = ["0","1","2","3","4","5","6","7","8","9"]

for parola in lista_parole:
    for lettera in parola:
        print(lettera, end=" | ")
        print("")


# Scrivere un programma che utilizzi un loop for per contare quante volte una lettera compare in una stringa.
stringa = "banana"
conta_a = 0

for lettera in stringa:
    if lettera == "a":
        conta_a += 1

print(f"La lettera a compare, {conta_a}, volte.")
