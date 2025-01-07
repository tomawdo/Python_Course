from function import *

sfide = {
    1: sfida1,
    2: sfida2,
    3: sfida3,
    4: sfida4,
    5: sfida5,
    6: sfida6,
    7: sfida7,
    8: sfida8,
    9: sfida9,
    10: sfida10,
    11: sfida11,
    12: sfida12,
    13: sfida13,
    14: sfida14
}

while True:
    print("\n*** Calendario delle Sfide di Programmazione ***")
    print("Digita il numero del giorno (1-24) per affrontare una sfida, oppure 0 per uscire.")

    scelta = int(input("La tua scelta: "))
    if scelta == 0:
        print("Grazie per aver partecipato! Alla prossima!")
        break
    elif scelta in sfide:
        print(f"\nLanciando la sfida del giorno {scelta}...\n")
        sfide[scelta]()
    else:
        print("Scelta non valida. Inserisci un numero tra 1 e 24.")
    
