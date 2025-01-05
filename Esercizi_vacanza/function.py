def sfida1():
    print("Scrivi un programma che permetta a un negoziante di calcolare lo sconto. "
          "Il programma prende in input il prezzo iniziale e lo sconto applicato, restituendo il prezzo finale scontato.")
    try:
        listino_base = float(input("Inserisci il prezzo base (€): "))
        sconto = float(input("Inserisci lo sconto dedicato (senza %): "))
        prezzo_scontato = listino_base - (listino_base * sconto) / 100
        print(f"Il prezzo a te dedicato è: €{prezzo_scontato:.2f}")
    except ValueError:
        print("Controlla che abbia inserito valori numerici. Riprova!")

def sfida2():
    print("Scrivi un programma che permetta di calcolare per quanto tempo deve rimanere acceso il forno "
          "per il pranzo di Natale. Il programma prende in input tutte le pietanze che richiedono di essere"
          "inserite in forno e relativo tempo di cottura e restituisce la somma del tempo necessario per"
          "completare tutte le preparazioni")
    try:
        nr_pietanze = int(input("Quante pietanze cucinerai? ")) # utente indica il numero di pietanze
        tempo_totale = 0

        for i in range(nr_pietanze):
            pietanza = input(f"Inserisci la pietanza {i + 1}: ")
            tempo_cottura = int(input(f"Inserisci i minuti di cottura per {pietanza}: "))
            tempo_totale += tempo_cottura

        if tempo_totale > 60:
            ore, minuti = divmod(tempo_totale, 60)
            print(f"Il tempo necessario per cucinare tutte le pietanze è di {ore} ore e {minuti} minuti.")
        else:
            print(f"Il tempo necessario per cucinare tutte le pietanze è di {tempo_totale} minuti.")

    except ValueError:
        print("Assicurati di inserire numeri validi per il numero di pietanze e i tempi di cottura.")

def sfida3():
    print("Scrivi un programma che calcoli il numero totale di parole presenti in un messaggio di auguri.")




if __name__ == "__main__":
    sfida1(),
    sfida2(),
    sfida3()