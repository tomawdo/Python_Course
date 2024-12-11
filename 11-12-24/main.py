print("")

import random

# Genera un numero casuale tra 1 e 100
numero_segreto = random.randint(1, 100)
tentativo = None

print("Benvenuto! Ho scelto un numero tra 1 e 100. Riuscirai a indovinarlo?")

# Continua finché l'utente non indovina
while tentativo != numero_segreto:
    try:
        # Chiede all'utente di inserire un numero
        tentativo = int(input("Inserisci il tuo tentativo: "))
        
        # Fornisce feedback
        if tentativo < numero_segreto:
            print("Troppo basso! Riprova.")
        elif tentativo > numero_segreto:
            print("Troppo alto! Riprova.")
        else:
            print("Congratulazioni! Hai indovinato il numero!")
    except ValueError:
        print("Per favore, inserisci un numero valido.")

print("Grazie per aver giocato!")



# chiedi all'utente di inserire una parola
#stampa solo le consonanti con il ciclo while

# Chiedi all'utente di inserire una parola
parola = input("Inserisci una parola: ")

# Inizializza un indice per il ciclo
indice = 0

# Ciclo while per scorrere ogni carattere della parola
while indice < len(parola):
    carattere = parola[indice]
    # Controlla se il carattere è una consonante
    if carattere.lower() not in 'aeiou':
        print(carattere, end="")
    indice += 1









