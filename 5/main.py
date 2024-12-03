i = 0
while i < 6:
    print(i)
    i += 1


# 1. stampa 6 volte la frase "Ciao carissim" (3 errori)

# for i in range < 6 #sintassi corretta è range(x) e non range < x (sintassi di while)
# print "ciao carissimi" #identazione del print + le parentesi ()


for i in range(6):
    print ("Ciao carissimi")


# 2. chiedi all'utente di inserire 3 numeri e stampa il numero di asterischi corrispondenti

# nuovalista = () #sintassi sbagliata
nuovalista = []

# for i in range (3): #spazio tra range e valore
for i in range(3):
#   domanda = input("Inserisci un numero ") # cast input -> intero
    domanda = int(input("Inserisci un numero"))
    nuovalista.append(domanda)
    for elemento in nuovalista:
#       print("*" * elemento
        print("*" * elemento) #chiudo ) la funzione print


# 3. stampa tutti i numeri pari fino a 1000 compresi

# for i in range(1000):
for i in range(1001): # 1001 include il valore 1000
#   if i % 2 != 0:
    if i % 2 == 0: # controllo se il numero è pari
        print(i)


# 4. chiedo all'utente di inserire numeri positivi e nagtivi, ferma l'inserimento quando hai almeno 3 numeri positivi

contatore = 0

while contatore < 3:
    n = int(input("Inserisci il numero: "))
    if n < 0:
        continue # identazione
#   contatore += # errore di sintassi 
    contatore += 1
