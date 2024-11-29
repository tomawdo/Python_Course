NR_MAX_QUOTE = 5
MAX_SCOMMESSA = 100
MIN_SCOMMESSA = 10

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

def ottengo_nr_quote():
    while True: # ciclo l'operazione
        quote = input("Quante quote vuoi scommettere (1 - " + str(NR_MAX_QUOTE) + ")? ")
        if quote.isdigit(): # controllo quote -> numero
            quote = int(quote) # converto quote -> intero
            if 1 <= quote <= NR_MAX_QUOTE: # controllo quote siano tra 1 e 3 (nr_max_righe)
                break # proseguo con l'operazione
            else:
                print("Inserisci un numero valido di quote.") # informo l'utente che l'importo deve essere maggiore di zero.
        else:
            print("Attenzione! Inserisci un numero.") # poiché non è un numero, chiedo di inserire un numero.
    return quote

def ottengo_scommessa():
    while True:
        importo = input("Quanto vuoi scommettere per ogni riga? €")
        if importo.isdigit():
            importo = int(importo)
            if MIN_SCOMMESSA <= importo <= MAX_SCOMMESSA:
                break
            else:
                print(f"L'importo per ogni riga dev'essere tra €{MIN_SCOMMESSA} - €{MAX_SCOMMESSA}.")
        else:
            print("Inserisci un importo.")
    return importo

def main():
    saldo = float(deposito())
    quote = ottengo_nr_quote()
    scommessa = float(ottengo_scommessa())
    tot_scommessa = float(scommessa * quote)

    if tot_scommessa > saldo:
        print(f"Non hai sufficiente credito. Il tuo saldo è: €{saldo}")
    else:
        print(f"Hai scommesso €{scommessa} su {quote} quote. Totale: €{tot_scommessa}.")
        # Altra logica per la conclusione del gioco

    # print(f"Hai scommesso €{scommessa} su {quote} quote. Totale: €{tot_scommessa}.")
main()