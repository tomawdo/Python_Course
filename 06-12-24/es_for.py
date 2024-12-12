import random

# chiedete di inserire tre cibi e salvai in una lista

# metodo 1
cibi = []
for cibo in range(3):
    domanda = input("Inserisci un cibo: ")
    cibi.append(domanda)
print(cibi)

# metodo 2
cibi = [input("Inserisci un cibo: ") for _ in range(3)]
print(cibi)


for n in range(3):
    x = random.randint(1, 100)
    print(x)

# stampa tutti i numeri compresi tra 1 e 20
# per ogni numero nel range
for n in range(1, 21):
    print(n)

# inserire una frase e stampare tutte le lettere della frase

frase = input("Inserisci una frase")
for f in frase:
    print(f)


# chiedi all'utente di inserire 3 elementi in una lista e stampa ogni lettera di ogni elemento della lista
# listaElementi = []

for elemento in range(3):
    richiesta = input("Inserisci elemento: ")
#   listaElementi.append(richiesta)
    for se in richiesta:
        print(se)


listaElementi = []

for i in range(3):
    richiesta = input("Inserisci elemento: ")
    listaElementi.append(richiesta)

for elemento in listaElementi:
    print(f"\nParola: {elemento}")
    for lettera in elemento:
        print(lettera, end=" | ")


# Chiediamo all'utente di inserire due numeri la cui funzione sia definire il range
numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))

n_min = min(numero1, numero2)
n_max = max(numero1, numero2)

print(f"I numeri compresi {n_min} e {n_max} sono: ")

for numero in range(n_min, n_max + 1):
    print(f"{numero}")



# if metodo 1
user_input = input("Name: ")

if user_input:
    nome = user_input
else:
    nome = "ND"

print(nome)


# if metodo 2
user_input = input("Name: ")
nome = user_input or "ND"
print(nome)

# Come rimuovere il prefisso o i primi 4 caratteri
# metodo 1

links = [
    "www.google.it",
    "www.youtube.com",
    "www.ansa.it",
    "www.wikipedia.org",
]

for link in links:
    #print(link.lstrip("www.")) #in questo caso elimina anche la w di wikipedia quindi ATTENZIONE!
    print(link.removeprefix("www.")) # .remove_prefix è consigliato