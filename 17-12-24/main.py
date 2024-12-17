# Esercizio 1: 


# Esercizio 2: chiedi all'utente di inserire una lista di parole (max 5) tramite una funzione stampo un elenco di parole che inziano con la "s"


# Esercizio 3 - scrivi una funzione (separat dal codice main) che richieda una serie di numeri (lista) e stampi il valore max


# Esercizio 4 - scrivi la versione della funzione len() senza usare len()
# inizializzo la variabile contatore a 0
# definisco una variabile con un argomento
# creo un ciclo for che analizzi tutti gli elementi presenti nell'argomento della variabile
# per ogni elemento presente nell'argoomento della variabile aggiungo 1 e riassegno contatore
# uso return per restituire il valore di contatore
# test funzione su una stringa inserita dall'utente

# Definizione della funzione per calcolare la lunghezza
def lunghezza(elemento):
    contatore = 0  # Inizializzo il contatore a 0
    for _ in elemento:  # Scorro ogni elemento dell'argomento passato
        contatore += 1  # Incremento il contatore di 1 per ogni elemento
    return contatore  # Restituisco il valore del contatore

# Test della funzione su una stringa inserita dall'utente
stringa = input("Inserisci una stringa: ")
print(f"La lunghezza della stringa è: {lunghezza(stringa)}")


