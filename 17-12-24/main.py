def sommatoria():
    print(n1 + n2)
sommatoria()

def sottrazione():
    print(n1 - n2)
sottrazione()

def moltiplicazione():
    print(n1 * n2)
moltiplicazione()

def divisione():
    if n2 != 0:
        print(f"{n1 / n2}")
    else:
        print("Errore: divisione per zero.")
divisione()

operatore = input("Inserisci un operatore (+, -, *, /): ")
n1 = int(input("Inserisci il primo numero"))
n2 = int(input("Inserisci il secondo numero"))

if operatore == "+":
        sommatoria(operatore)
    elif operatore == "-":
        sottrazione(operatore)
    elif operatore == "*":
        moltiplicazione(operatore)
    elif operatore == '/':
        if n2 != 0:
            divisione(operatore)
        else:
            print("Errore: divisione per zero.")
    else:
        print("Operazione non valida.")



# chiedi all'utente di inserire una lista di parole (max 5)
# tramite una funzione stampo un elenco di parole che inziano con la "s"
