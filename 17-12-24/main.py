# Esercizio 1: 


# Esercizio 2: chiedi all'utente di inserire una lista di parole (max 5) tramite una funzione stampo un elenco di parole che inziano con la "s"


# Esercizio 3 - scrivi una funzione (separat dal codice main) che richieda una serie di numeri (lista) e stampi il valore max

# Definizione della funzione
def stampa_valore_massimo(lista_numeri):
    if len(lista_numeri) == 0:
        print("La lista è vuota. Non è possibile determinare il valore massimo.")
    else:
        valore_massimo = max(lista_numeri)
        print(f"Il valore massimo è: {valore_massimo}")

# Codice principale
if __name__ == "__main__":
    # Input dell'utente
    numeri = input("Inserisci una serie di numeri separati da spazi: ").split()
    numeri = [float(numero) for numero in numeri]  # Converte gli input in numeri
    stampa_valore_massimo(numeri)


