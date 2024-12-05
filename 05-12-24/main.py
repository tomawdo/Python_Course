# Chiedi all'utente di inserire tre numeri separati da virgole
input_utente = input("Inserisci tre numeri separati da virgole: ")

# Dividi l'input in una lista di stringhe
numeri_str = input_utente.split(",")

# Crea una lista vuota per i numeri
numeri = []

# Usa un ciclo for con indicizzazione per convertire le stringhe in numeri e aggiungerli alla lista
for i in range(len(numeri_str)):
    try:
        numeri.append(float(numeri_str[i].strip()))
    except ValueError:
        print(f"Errore: '{numeri_str[i]}' non è un numero valido.")

# Stampa la lista risultante
print("I numeri inseriti sono:", numeri)