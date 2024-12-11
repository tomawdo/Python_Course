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



# ESERCIZIO 1: richiedi all'utente di inserire due numeri a sommare. Uno deve essere pari, l'altro dispari

#ESERCIZIO 2:
# indovina un numero segreto e pensato dal computer
# hai tre tentativi
# dopo ogni tentativo ti sarà indicato quanti te ne restano (es. 2 tentativi rimasti)
# quando esaurisce i tentativi chiediamo se vuole giocare nuovamente


print("Devi inserire un numero pari e uno dispari da sommare.")

# Chiedi un numero pari
numero1 = int(input("Inserisci un numero pari: "))
while numero1 % 2 != 0:  # Controlla se il numero non è pari
    print("Il numero non è pari. Riprova.")
    numero1 = int(input("Inserisci un numero pari: "))

# Chiedi un numero dispari
numero2 = int(input("Inserisci un numero dispari: "))
while numero2 % 2 == 0:  # Controlla se il numero non è dispari
    print("Il numero non è dispari. Riprova.")
    numero2 = int(input("Inserisci un numero dispari: "))

# Somma e stampa il risultato
somma = numero1 + numero2
print(f"La somma dei due numeri è: {somma}")





import random


#ESERCIZIO 2: indovina un numero segreto e pensato dal computer
# max 3 tentativi
# dopo ogni tentativo ti sarà indicato quanti te ne restano (es. 2 tentativi rimasti)
# quando esaurisce i tentativi chiediamo se vuole giocare nuovamente

n_segreto = random.randint(1, 20)
tentativo = 3
inizio = ""
rigioca = ""
ytd = datetime.datetime.now()

nome = input("Come ti chiami? ")
anno_nascita = int(input("Inserisci l'anno di nascita: "))
start = ytd.year - anno_nascita
print(f"Benvenuto {nome}! \nHai {start} anni quindi puoi giocare.")


if inizio == start:
    while tentativo > 0:
        indovina = int(input(f"Indovia il numero (tentativi riasti: {tentativo}): "))
        if indovina == n_segreto:
            print("Numero indovinato")
            break
        elif indovina < n_segreto:
            print("Troppo basso. Riprova!")
        else:
            print("Troppo alto. Riprova!")
        tentativo -= 1
    if tentativo == 0:
        print(f"Hai esaurito tutti i tentativi. Il nr segreto era: {n_segreto}")
        print("Vuoi giocare nuovamente? (sì/no)")
elif rigioca == "sì":
    print("Rigioca script")
else:
    print("Alla prossima!")
