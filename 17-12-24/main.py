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



def filtra_parole_con_s(parole):
    """
    Filtra e restituisce le parole che iniziano con la lettera 's' (o 'S') da una lista.
    """
    return [parola for parola in parole if parola.lower().startswith('s')]

# Codice principale
def main():
    # Chiedo all'utente di inserire una lista di parole (max 5)
    parole = input("Inserisci fino a 5 parole separate da uno spazio: ").split()[:5]
    
    # Chiamo la funzione per filtrare le parole con 's'
    parole_con_s = filtra_parole_con_s(parole)
    
    # Stampo l'elenco delle parole che iniziano con 's'
    print("\nLe parole che iniziano con la lettera 's' sono:")
    for parola in parole_con_s:
        print(parola)

# Eseguo il codice principale
if __name__ == "__main__":
    main()

