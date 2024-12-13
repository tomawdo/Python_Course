# Esercizio 1
# chiedi all'utente di inserire una parola e stampa le posizioni delle vocali presenti nella stringa

# Chiedi all'utente di inserire una parola
parola = input("Inserisci una parola: ")

# Definisci le vocali
vocali = "aeiouAEIOU"

# Trova le posizioni delle vocali nella parola
posizioni_vocali = [indice for indice, carattere in enumerate(parola) if carattere in vocali]

# Stampa le posizioni delle vocali
if posizioni_vocali:
    print("Le vocali si trovano alle seguenti posizioni:", posizioni_vocali)
else:
    print("Non ci sono vocali nella parola inserita.")