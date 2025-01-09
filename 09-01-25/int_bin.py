while True:
    numero = int(input("Inserisci un numero: "))
    conversione = bin(numero)[2:]
    print(f"Il numero {numero} convertito in binario {conversione}")
    
    
    # Chiedi all'utente di inserire un numero intero
numero = int(input("Inserisci un numero intero: "))

# Inizializza una stringa vuota per il risultato
binario = ""

# Esegui la conversione
while numero > 0:
    resto = numero % 2      # Trova il resto della divisione per 2
    binario = str(resto) + binario  # Aggiungi il resto all'inizio della stringa
    numero = numero // 2    # Aggiorna il numero dividendo interamente per 2

# Stampa il risultato
print(f"Il numero in binario è: {binario}")



# Chiedi all'utente di inserire un numero binario
binario = input("Inserisci un numero binario: ")

# Inizializza il risultato
decimale = 0

# Esegui la conversione
for i in range(len(binario)):
    bit = int(binario[-(i + 1)])  # Prendi il bit da destra a sinistra
    decimale += bit * (2 ** i)   # Somma il valore del bit moltiplicato per 2^posizione

# Stampa il risultato
print(f"Il numero binario {binario} in decimale è: {decimale}")
