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
    """
    Questa funzione prende una lista come input e restituisce 
    la somma di tutti i numeri presenti nella lista.
    
    Args:
        lista (list): Una lista contenente elementi di vario tipo.
    
    Returns:
        float: La somma dei numeri nella lista.
    """
    somma = 0
    for elemento in lista:
        if isinstance(elemento, (int, float)):  # Controlla se è un numero
            somma += elemento
    return somma

# Esempio di utilizzo
lista_di_prova = [1, 2, "ciao", 3.5, True, 4, "Python"]
risultato = somma_numeri(lista_di_prova)
print(f"La somma dei numeri nella lista è: {risultato}")
    