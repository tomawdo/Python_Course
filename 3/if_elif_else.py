# Scrivi un programma che chieda all’utente il prezzo di un prodotto e la categoria dello sconto da applicare.
# Il programma deve calcolare il prezzo finale dopo aver applicato lo sconto.

# Dichiarazione delle categorie di sconto

sconto_a = 0.20  # 20% di sconto
sconto_b = 0.10  # 10% di sconto
sconto_c = 0.05  # 5% di sconto
sconto_nessuno = 0.00  # Nessuno sconto

prezzo = float(input("Inserisci il prezzo di un prodotto: "))
categoria_sconto = input("Inserisci la categoria di sconto (A, B, C o Z): ")

if categoria_sconto.upper() == "A":
    prezzo_finale = prezzo - (prezzo * sconto_a)
elif categoria_sconto.upper() == "B":
    prezzo_finale = prezzo - (prezzo * sconto_b)
elif categoria_sconto.upper() == "C":
    prezzo_finale = prezzo - (prezzo * sconto_c)
elif categoria_sconto.upper() == "Z":
    prezzo_finale = prezzo - (prezzo * sconto_nessuno)
else:
    prezzo_finale = None
    print("Categoria non valida!")

if prezzo_finale is not None:
    print(f"Il prezzo finale è: {prezzo_finale:.2f}")
