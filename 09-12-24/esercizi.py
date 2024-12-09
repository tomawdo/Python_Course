# Scrivi un programma che chieda all'utente che svoga le seguenti operazioni:
# - trova la lunghezza della stringa
# - determina il carattere minimo e massimo in base all'ordine alfabetico
# - ordina i caratteri della stringa in ordine alfabetico
# - usa str per convertire un numero intero come stringa

# Chiedi una stringa all'utente
stringa = input("Inserisci una stringa: ")

# Lunghezza della stringa
print("Lunghezza della stringa:", len(stringa))

# Carattere minimo e massimo
print("Carattere minimo:", min(stringa))
print("Carattere massimo:", max(stringa))

# Ordina i caratteri della stringa
print("Stringa ordinata:", ''.join(sorted(stringa)))

# Conversione di un numero intero in stringa
numero = int(input("Inserisci un numero intero: "))
print("Numero come stringa:", str(numero))

# ESERCIZIO 2: Chiedi all'utente una frase o parola. Fai quanto segue:
# - trova la posizione della prima occorenza della parola nella frase
# - conta quante volte appare la parola nella frase
# - converti la frase in maiuscolo, minuscolo e con la prima lettera maiuscola.

# Chiedi una frase all'utente
frase = input("Inserisci una frase: ")

# Chiedi una parola da cercare nella frase
parola = input("Inserisci una parola da cercare: ")

# Trova la posizione della prima occorrenza della parola
posizione = frase.find(parola)
if posizione != -1:
    print(f"La parola '{parola}' appare per la prima volta alla posizione: {posizione}")
else:
    print(f"La parola '{parola}' non è presente nella frase.")

# Conta quante volte appare la parola nella frase
conteggio = frase.count(parola)
print(f"La parola '{parola}' appare {conteggio} volta/e nella frase.")

# Converti la frase in maiuscolo, minuscolo e con la prima lettera maiuscola
print("Frase in maiuscolo:", frase.upper())
print("Frase in minuscolo:", frase.lower())
print("Frase con la prima lettera maiuscola:", frase.capitalize())
