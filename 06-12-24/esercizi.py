# chiedete di inserire tre cibi e salvai in una lista

cibi = []
for cibo in range(3):
    domanda = input("Inserisci un cibo: ")
    cibi.append(domanda)
print(cibi)

cibi = [input("Inserisci un cibo: ") for _ in range(3)]
print(cibi)

