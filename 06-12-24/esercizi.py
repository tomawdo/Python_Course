# chiedete di inserire tre cibi e salvai in una lista

cibi = []
for cibo in range(3):
    domanda = input("Inserisci un cibo: ")
    cibi.append(domanda)
print(cibi)

cibi = [input("Inserisci un cibo: ") for _ in range(3)]
print(cibi)

# chiedi all'utente di inserire 3 elementi in una lista e stampa ogni lettera di ogni elemento della lista
listaElementi = []
for elemento in range(3):
    richiesta = input("Inserisci elemento: ")
    for se in richiesta:
        print(se)
        
        
        
listaElementi = []

# Chiedi all'utente di inserire 3 elementi nella lista
for i in range(3):
    richiesta = input("Inserisci elemento: ")
    listaElementi.append(richiesta)

# Stampa ogni parola in spelling
for elemento in listaElementi:
    print(f"\nParola: {elemento}")  # Introduce la parola
    for lettera in elemento:
        print(lettera)

# chiediamo di inserire due numeri
# stampiamo tutti i numeri compresi nel range indicato dall'utente

# Chiediamo all'utente di inserire due numeri
numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))

# Determiniamo l'intervallo corretto (minimo e massimo)
minimo = min(numero1, numero2)
massimo = max(numero1, numero2)

# Stampiamo tutti i numeri compresi nel range
print("I numeri compresi tra", minimo, "e", massimo, "sono:")
for numero in range(minimo, massimo + 1):
    print(numero)
