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


# ESERCIZIO 3: usa i metodi strip, replace, startswith, endswith, join, insieme a slicing e indexing.
# Chiedi all'utente una stringa e fai quanto segue:
# - rimuovi gli spazi iniziali
# - sostituisci tutte le vocali con un simbolo (*)
# - Verfica se la stringa inizia con una determinata parola e finsice con un'altra
# - stampa la stringa inversa usando slicing
# - unisci i caratteri della stringa con un separatore

# Chiedi all'utente una stringa
stringa = input("Inserisci una stringa: ")

# Rimuovi gli spazi iniziali
stringa_senza_spazi = stringa.lstrip()
print("Stringa senza spazi iniziali:", stringa_senza_spazi)

# Sostituisci tutte le vocali con il simbolo '*'


# Definizione delle vocali
vocali = "aeiouAEIOU"

# Chiedi all'utente una stringa
stringa = input("Inserisci una stringa: ")

# Sostituisci tutte le vocali con il simbolo '*'
for vocale in vocali:
    stringa = stringa.replace(vocale, '*')

print("Stringa con vocali sostituite:", stringa)



# Verifica se la stringa inizia con una determinata parola e finisce con un'altra
inizio = input("Inserisci la parola con cui dovrebbe iniziare la stringa: ")
fine = input("Inserisci la parola con cui dovrebbe finire la stringa: ")
if stringa_senza_spazi.startswith(inizio):
    print(f"La stringa inizia con '{inizio}'.")
else:
    print(f"La stringa non inizia con '{inizio}'.")

if stringa_senza_spazi.endswith(fine):
    print(f"La stringa finisce con '{fine}'.")
else:
    print(f"La stringa non finisce con '{fine}'.")

# Stampa la stringa inversa usando slicing
stringa_inversa = stringa_senza_spazi[::-1]
print("Stringa inversa:", stringa_inversa)

# Unisci i caratteri della stringa con un separatore
separatore = input("Inserisci un separatore: ")
stringa_unita = separatore.join(stringa_senza_spazi)
print("Stringa con caratteri uniti dal separatore:", stringa_unita)


# Dizionario per sostituire le vocali con '*'
mappa_vocali = {'a': '*', 'e': '*', 'i': '*', 'o': '*', 'u': '*',
                'A': '*', 'E': '*', 'I': '*', 'O': '*', 'U': '*'}

# Chiedi all'utente una stringa
stringa = input("Inserisci una stringa: ")

# Costruisci una nuova stringa
stringa_sostituita = ""
for char in stringa:
    if char in mappa_vocali:  # Se il carattere è una vocale
        stringa_sostituita += mappa_vocali[char]  # Sostituiscilo con '*'
    else:
        stringa_sostituita += char  # Altrimenti, mantienilo invariato

print("Stringa con vocali sostituite:", stringa_sostituita)

