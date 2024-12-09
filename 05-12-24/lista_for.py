# Esercizi ciclo for

righe = range(1, 9)
colonne = "abcdefgh"

for colonna in colonne:
    for riga in righe:
        print(colonna, str(riga))


lista = ["Rossi", "Luca", "Edoardo", "Marco", "Isabel"]
for nome in lista:
    if len(nome) % 2 == 0:
        print(nome)
        for vocale in nome:
            if vocale in "aeiou":
                print(vocale)


lista_uno = [1,2,3,4,5]
lista_due = [10,2,9,8,5]

for valore in lista_uno:
    if valore in lista_due:
        print(valore)
