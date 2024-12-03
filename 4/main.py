# Ciclo while e condizioni if per richiedere all’utente di inserire tre numeri pari negativi.
# Il programma continua fino a quando l’utente non inserisce correttamente tre numeri che soddisfano il criterio.

numeri = []  # Lista per memorizzare i numeri validi

while len(numeri) < 3:
    numero = input(f"Inserisci tre numeri pari negativi ({len(numeri) + 1}/3): ")

    # Controllo se l'input è un numero
    if numero.lstrip('-').isdigit():
        numero = int(numero)
        # Controllo se il numero è pari e negativo
        if numero < 0 and numero % 2 == 0:
            numeri.append(numero)
            # print(f"Numero valido! Hai inserito: {numeri}")
        else:
            print("Il numero deve essere pari e negativo. Riprova.")
    else:
        print("Inserire un numero valido. Riprova.")

print(f"Hai inserito correttamente i numeri pari negativi: {numeri}")