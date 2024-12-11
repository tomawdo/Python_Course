import datetime
import random
import time

'''
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

'''
#ESERCIZIO 2: indovina un numero segreto e pensato dal computer
# max 3 tentativi
# dopo ogni tentativo ti sarà indicato quanti te ne restano (es. 2 tentativi rimasti)
# quando esaurisce i tentativi chiediamo se vuole giocare nuovamente



nome = input("Inserisci il tuo nome: ")

while True:  # Ciclo principale per il riavvio del gioco
    print(f"Benvenuto {nome}! \nPer giocare devi prima inserire il tuo anno di nascita.")

    anno_nascita = input("Inserisci il tuo anno di nascita: ")
    if not anno_nascita.isdigit():
        print("Devi inserire un numero valido.")
        continue

    anno_nascita = int(anno_nascita)
    anno_corrente = datetime.datetime.now()
    eta = anno_corrente.year - anno_nascita

    if eta < 0 or anno_nascita < 1900:
        print("Anno non valido. Riprova.")
        continue

    if eta < 18:
        print("Mi dispiace, sei minorenne. Il gioco d'azzardo non è permesso ai minori di 18 anni.")
        break

    print("Ho generato un numero tra 1 e 10. Hai 3 tentativi per indovinarlo.")
    numero_segreto = random.randint(1, 10)
    tentativi = 3

    while tentativi > 0:
        guess = input(f"Indovina il numero (tentativi rimasti: {tentativi}): ")
        if not guess.isdigit():
            print("Devi inserire un numero valido.")
            continue

        guess = int(guess)
        if guess == numero_segreto:
            print("Complimenti! Hai indovinato il numero segreto.")
            break
        elif guess < numero_segreto:
            print("Troppo basso!")
        else:
            print("Troppo alto!")
        tentativi -= 1

    if tentativi == 0:
        print(f"Hai esaurito i tentativi! Il numero segreto era: {numero_segreto}")

    # Chiedi se vuole giocare di nuovo
    gioca_ancora = input("Vuoi giocare di nuovo? (sì/no): ").strip().lower()
    if gioca_ancora != "sì":
        print("Grazie per aver giocato! Alla prossima!")
        break


