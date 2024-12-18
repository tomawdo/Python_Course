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
    
    
def numeri_volanti_di_merz(n, regola):
    """
    Calcola i numeri volanti di Merz secondo una regola data.
    
    Args:
        n (int): Numero di termini da generare.
        regola (function): Funzione che definisce la regola della sequenza.
    
    Returns:
        list: Sequenza dei numeri volanti di Merz.
    """
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












