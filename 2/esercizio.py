# ESERCIZIO LISTA DELLA SPESA
# METODO 1

utente = input("Come ti chiami? ")
prod1 = input("Inserisci il prodotto: ")
prod2 = input("Inserisci il prodotto: ")
prod3 = input("Inserisci il prodotto: ")

przprod1 = 3.45
przprod2 = 2
przprod3 = 2

print(utente, ",oggi hai speso", (float(przprod1) + przprod2 + przprod3), "euro per comprare: \n", prod1, "-", przprod1, "\n", prod2, "-", przprod2, "\n",prod3, "-", przprod3)


# METODO 2

utente = input("Ciao! Come ti chiami? ")
prodotti = []
prezzi = []

for i in range(2):
    prodotti.append(input("Inserisci il prodotto: "))
    prezzi.append(float(input(f"Inserisci il prezzo di {prodotti[i]}: ")))
    
totale_spesa = sum(prezzi)
print(utente, "oggi hai speso: ", totale_spesa)
