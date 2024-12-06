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
