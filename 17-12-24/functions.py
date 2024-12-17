# Esercizio 1
def somma(arg1, arg2):
    result = arg1 + arg2
    print(f"Risultato somma: {result}")
def sottrazione(arg1, arg2):
    result = arg1 - arg2
    print(f"Risultato sottrazione: {result}")
def moltiplicazione(arg1, arg2):
    result = arg1 * arg2
    print(f"Risultato moltiplicazione: {result}")
def divisione(arg1, arg2):
    if arg2 != 0:
        result = arg1 / arg2
    else:
        print("Errore: divisione per zero.")
    print(print(f"Risultato divisione: {result}"))

# Esercizio 2
def filtra_parole_con_esse(parole):
    return [parola for parola in parole if parola.startswith('s')]

# Esercizio 3
def numeri_max(lista_numeri):
    if len(lista_numeri) == 0:
        print("La lista è vuota. Riprova!")
    else:
        val_max = max(lista_numeri)
        print(f"Il valore massimo è: {val_max}")

# Esercizio 4
def lunghezza(elemento):
    contatore = 0
    for i in elemento:
        contatore += 1
    return contatore






















