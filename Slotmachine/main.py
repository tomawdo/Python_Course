NR_MAX_RIGHE = 30

def deposito(): # scrivo la funzione deposito
    while True: # ciclo l'operazione
        importo = input("Quanto vuoi caricare? €") # chiedo all'utente di inserire una somma
        if importo.isdigit(): # controllo che l'importo sia un numero
            importo = int(importo) # converto l'importo in intero
            if importo > 0: # controllo che l'importo sia maggiore di zero
                break # proseguo con l'operazione
            else:
                print("L'importo deve essere maggiore di 0 (zero).") # informo l'utente che l'importo deve essere maggiore di zero.
        else:
            print("Attenzione! Inserisci un numero corretto.") # poiché non è un numero, chiedo di inserire un numero.
    return importo

def ottenere_nr_righe():
    while True: # ciclo l'operazione
        righe = input("Quante righe vuoi scommettere (1 - " + str(NR_MAX_RIGHE) + ")? ")
        if righe.isdigit(): # controllo righe -> numero
            righe = int(righe) # converto righe -> intero
            if 1 <= righe <= NR_MAX_RIGHE: # controllo righe siano tra 1 e 3 (nr_max_righe)
                break # proseguo con l'operazione
            else:
                print("Inserisci un numero valido di righe.") # informo l'utente che l'importo deve essere maggiore di zero.
        else:
            print("Attenzione! Inserisci un numero.") # poiché non è un numero, chiedo di inserire un numero.
    return righe

def main():
    saldo = deposito()
    righe = ottenere_nr_righe()
    print(saldo, righe)

main()