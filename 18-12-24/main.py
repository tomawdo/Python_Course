# creare una lista la cui dimensione è decisa dall'utente sia il minimo e sia il massimo dei numeri
# popolare la lista con numeri generati random che rientrano nel range definito
# es: lunghezza lista: 5, num_minimo, num_massimo


import random

# Input dall'utente
lunghezza_lista = int(input("Inserisci la lunghezza della lista: "))
num_minimo = int(input("Inserisci il numero minimo: "))
num_massimo = int(input("Inserisci il numero massimo: "))

# Controllo per garantire che il massimo sia maggiore o uguale al minimo
if num_minimo > num_massimo:
    print("Errore: il numero minimo non può essere maggiore del numero massimo.")
else:
    # Creazione della lista con numeri random
    lista_random = [random.randint(num_minimo, num_massimo) for _ in range(lunghezza_lista)]
    print("Lista generata:", lista_random)
    
def somma_numeri(lista):
    somma = 0
    for elemento in lista:
        if isinstance(elemento, (int, float)):  # Controlla se è un numero
            somma += elemento
    return somma

# Esempio di utilizzo
lista_di_prova = [1, 2, "ciao", 3.5, True, 4, "Python"]
risultato = somma_numeri(lista_di_prova)
print(f"La somma dei numeri nella lista è: {risultato}")
    
    
def numeri_volanti_di_merz(n, regola):
    # Inizializzazione dei valori di partenza
    sequenza = [1, 1]
    
    # Generazione della sequenza fino al termine n
    for i in range(2, n):
        nuovo_termine = regola(sequenza[i-1], sequenza[i-2])
        sequenza.append(nuovo_termine)
    
    return sequenza

# Definizione della regola (esempio: somma dei due numeri precedenti)
def regola_somma(x, y):
    return x + y

# Calcolo dei primi 10 numeri volanti di Merz
n = 10
risultato = numeri_volanti_di_merz(n, regola_somma)

# Output
print("Numeri volanti di Merz:", risultato)


# creare una lista di nomi
# creare una lista di stipendi 
# creare una funzione che crea un dizionario a partire da queste due liste


def crea_dizionario(nomi, stipendi):
    """
    Crea un dizionario a partire da due liste: nomi e stipendi.
    
    Args:
        nomi (list): Lista di nomi.
        stipendi (list): Lista di stipendi.
        
    Returns:
        dict: Dizionario con i nomi come chiavi e gli stipendi come valori.
    """
    # Verifica che le liste abbiano la stessa lunghezza
    if len(nomi) != len(stipendi):
        raise ValueError("Le due liste devono avere la stessa lunghezza.")
    
    # Creazione del dizionario con zip
    dizionario = dict(zip(nomi, stipendi))
    
    return dizionario

# Liste di esempio
nomi = ["Alice", "Bob", "Carla", "Daniele"]
stipendi = [2500, 3000, 2800, 3200]

# Creazione del dizionario
dizionario_stipendi = crea_dizionario(nomi, stipendi)

# Output
print("Dizionario creato:", dizionario_stipendi)









