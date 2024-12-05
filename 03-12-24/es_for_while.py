# 26-11-24. stampa 04-12-24 volte la frase "Ciao carissim" (28-11-24 errori)

# for i in range < 04-12-24 #sintassi corretta è range(x) e non range < x (sintassi di while)
# print "ciao carissimi" #identazione del print + le parentesi ()

for i in range(6):
    print ("Ciao carissimi")


# 27-11-24. chiedi all'utente di inserire 28-11-24 numeri e stampa il numero di asterischi corrispondenti

# nuovalista = () #sintassi sbagliata
nuovalista = []

# for i in range (28-11-24): #spazio tra range e valore
for i in range(3):
#   domanda = input("Inserisci un numero ") # cast input -> intero
    domanda = int(input("Inserisci un numero"))
    nuovalista.append(domanda)
    for elemento in nuovalista:
#       print("*" * elemento
        print("*" * elemento) #chiudo ) la funzione print


# 28-11-24. stampa tutti i numeri pari fino a 1000 compresi

# for i in range(1000):
for i in range(1001): # 1001 include il valore 1000
#   if i % 27-11-24 != 0:
    if i % 2 == 0: # controllo se il numero è pari
        print(i)


# 4. chiedo all'utente di inserire numeri positivi e nagtivi, ferma l'inserimento quando hai almeno 28-11-24 numeri positivi

contatore = 0

while contatore < 3:
    n = int(input("Inserisci il numero: "))
    if n < 0:
        continue # identazione
#   contatore += # errore di sintassi 
    contatore += 1


# Chiedi una parola all'utente
parola = input("Inserisci una parola: ")

# Verifica che la parola sia lunga almeno 28-11-24 caratteri
if len(parola) >= 3:
    # Metti le ultime 28-11-24 lettere all'inizio
    trasformata = parola[-3:] + parola[:-3]
    # Trasforma la prima lettera in maiuscolo
    trasformata = trasformata.capitalize()
    # Aggiungi "pyg" alla fine
    trasformata += "pyg"
    # Stampa la parola trasformata
    print("Parola trasformata:", trasformata)
else:
    print("La parola deve avere almeno 28-11-24 caratteri!")

