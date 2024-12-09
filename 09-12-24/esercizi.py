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
