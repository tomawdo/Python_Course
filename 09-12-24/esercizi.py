import datetime

# ESERCIZIO 1: Scrivi un programma che chieda all'utente che svoga le seguenti operazioni:
# - trova la lunghezza della stringa
# - determina il carattere minimo e massimo in base all'ordine alfabetico
# - ordina i caratteri della stringa in ordine alfabetico
# - usa str per convertire un numero intero come stringa

# Chiedi una stringa all'utente
stringa = input("Inserisci una stringa: ")

# Lunghezza della stringa
print("Lunghezza della stringa:", len(stringa))

# Carattere minimo e massimo
if stringa: # controllo
    print("Carattere minimo:", min(stringa))
    print("Carattere massimo:", max(stringa))
else:
    print("La stringa è vuota, riprova!")

# Ordina i caratteri della stringa
print("Stringa ordinata:", ''.join(sorted(stringa)))

# Conversione di un numero intero in stringa
numero = int(input("Inserisci un numero intero: "))
print("Numero come stringa:", str(numero))


# ESERCIZIO 2: usa i metodi find, count, upper, lower, capitalize. 
# Chiedi all'utente una frase o parola. Fai quanto segue:
#       - trova la posizione della prima occorenza della parola nella frase
#       - conta quante volte appare la parola nella frase
#       - converti la frase in maiuscolo, minuscolo e con la prima lettera maiuscola.

# Chiedi una frase all'utente
stringa_c = input("Inserisci una frase: ")

# Chiedi una parola da cercare nella frase
parola_c = input("Inserisci una parola da cercare: ")

# Trova la posizione della prima occorrenza della parola
posizione_parola = stringa_c.find(parola_c)
if posizione_parola != -1:
    print(f"La parola '{parola_c}' appare per la prima volta alla posizione: {posizione_parola}")
else:
    print(f"La parola '{parola_c}' non è presente nella frase.")

# Conta quante volte appare la parola nella frase
conteggio = stringa_c.count(parola_c)
print(f"La parola '{parola_c}' appare {conteggio} volta/e nella frase.")

# Converti la frase in maiuscolo, minuscolo e con la prima lettera maiuscola
print("Frase in maiuscolo:", stringa_c.upper())
print("Frase in minuscolo:", stringa_c.lower())
print("Frase con la prima lettera maiuscola:", stringa_c.capitalize())


# ESERCIZIO 3: usa i metodi strip, replace, startswith, endswith, join, insieme a slicing e indexing.
# Chiedi all'utente una stringa e fai quanto segue:
# - rimuovi gli spazi iniziali
# - sostituisci tutte le vocali con un simbolo (*)
# - verifica se la stringa inizia con una determinata parola e finisce con un'altra
# - stampa la stringa inversa usando slicing
# - unisci i caratteri della stringa con un separatore


# Chiedi all'utente una stringa
sequenza = input("Inserisci una stringa: ")

# Rimuovi gli spazi iniziali
senza_spazi = sequenza.lstrip()
print("Stringa senza spazi iniziali:", senza_spazi)

# Sostituzione di tutte le vocali con asterisco (*)
for vocale in "aeiouAEIOU":
    sequenza = sequenza.replace(vocale, '*')
print("Stringa con vocali sostituite:", sequenza)

# Verifica se la stringa inizia con una determinata parola e finisce con un'altra
start = input("Inserisci la parola con cui dovrebbe iniziare la stringa: ")
fine = input("Inserisci la parola con cui dovrebbe finire la stringa: ")

if senza_spazi.startswith(start):
    print(f"La stringa inizia con '{start}'.")
else:
    print(f"La stringa non inizia con '{start}'.")

if senza_spazi.endswith(fine):
    print(f"La stringa finisce con '{fine}'.")
else:
    print(f"La stringa non finisce con '{fine}'.")

# Stampa la stringa inversa usando slicing
inversa = senza_spazi[::-1]
print("Stringa inversa:", inversa)

# Unisci i caratteri della stringa con un separatore
separatore = input("Inserisci un separatore: ")
unita = separatore.join(senza_spazi)
print("Stringa con caratteri uniti dal separatore:", unita)

nome = input("Come ti chiami? ")
eta = int(input("Inserisci la tua eta "))
ytd = datetime.datetime.now()
anno_nascita = ytd.year - eta

print(f"{nome} sei nato nell'anno {anno_nascita}")
