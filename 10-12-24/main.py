dmi# LISTE
'''
# Esempio di list comprehension
city_names = ["Torino", "Milano", "Roma", "Napoli", "Messina"]

# espressione for elemento in lista_elementi if condizione == vera
[print(city) for city in city_names if city != "Roma"]

city_names.sort(reverse=True)
print(city_names)

# Copiare una lista con .copy()
x = ["Torino", "Milano", "Roma", "Napoli", "Messina"]
y = x.copy()
y[0] = "New York"
# print(y)

# unire più liste insieme con +, append(), extend()
x = ["Peugeot", "Fiat", "Renault"]
y = ["Audi", "Volvo"]

for brand in y: x.append(brand) # metodo con ciclo for
x.extend(y) # metodo con extend()

print(x)
'''

# TUPLE: sono ordinate, indicizzate, non modificabili e permettono duplicati

x = ("Milano", "Roma", "Napoli")
y = tuple(("Milano", "Roma", "Napoli"))
z = ("Milano")

print(len(x))
print(y)
print(type(z))






# Esercizio: Scrivete programmi che legano una riga di dati in ingresso sotto forma di stringa e visualizzino quanto segue:
# - le sole lettere maiuscole della stringa
# - partire della seconda lettera della stringa, una lettera viene visualizzata e l'altra no alternativamente
# - la stringa con tutte le vocali sostituita da un carattere a scelta (_)
# - il numero in cifre presenti nella stringa


# Input: leggere una stringa
stringa = input("Inserisci una stringa: ")

# 1. Lettere maiuscole
maiuscole = ""
for carattere in stringa:
    if carattere.isupper():
        maiuscole += carattere
print("Lettere maiuscole:", maiuscole)

# 2. Lettere alternate (dalla seconda lettera)
alternate = ""
for i in range(1, len(stringa), 2):
    alternate += stringa[i]
print("Lettere alternate (da seconda posizione):", alternate)

# 3. Stringa con vocali sostituite da "_"
vocali = "aeiouAEIOU"
sostituita = ""
for carattere in stringa:
    if carattere in vocali:
        sostituita += "_"
    else:
        sostituita += carattere
print("Stringa con vocali sostituite:", sostituita)

# 4. Contare i numeri presenti nella stringa
numeri_totali = 0
for numero in "0123456789":
    numeri_totali += stringa.count(numero)
print("Numeri presenti nella stringa:", numeri_totali)



# chiedi al computer di generare un numero casuale
# utente deve indovinare il numero
# se il numero inserito è troppo alto "troppo alto"
# se il numero nserito è troppo basso "troppo basso"
# se il numero inserito è corretto "corretto"
# max tre tentativi



import random

# Genera un numero casuale tra 1 e 10
numero_casuale = random.randint(1, 10)

print("Indovina il numero tra 1 e 10. Hai 3 tentativi!")

for tentativo in range(1, 4):
    # Chiede all'utente di inserire un numero
    numero_utente = int(input(f"Tentativo {tentativo}: "))

    if numero_utente == numero_casuale:
        print("Corretto! Hai indovinato il numero.")
        break
    elif numero_utente < numero_casuale:
        print("Troppo basso.")
    else:
        print("Troppo alto.")

    if tentativo == 3:
        print(f"Hai finito i tentativi. Il numero corretto era {numero_casuale}.")



# Chiedi all'utene di inserire 3 numeri.
# stampa il numero più alto
# stabilisci se il carattere inserito dall'utente è una voale


# Chiedere all'utente di inserire 3 numeri
num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))
num3 = float(input("Inserisci il terzo numero: "))

# Trovare e stampare il numero più alto
massimo = max(num1, num2, num3)
print("Il numero più alto è:", massimo)

# Chiedere all'utente di inserire un carattere
carattere = input("Inserisci un carattere: ").lower()

# Stabilire se il carattere è una vocale
if carattere in "aeiou":
    print(f"Il carattere '{carattere}' è una vocale.")
else:
    print(f"Il carattere '{carattere}' non è una vocale.")



