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