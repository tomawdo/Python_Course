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
          "\nper il pranzo di Natale. Il programma prende in input tutte le pietanze che richiedono di essere"
          "\ninserite in forno e relativo tempo di cottura e restituisce la somma del tempo necessario per"
          "\ncompletare tutte le preparazioni"
          "\n")
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
    messaggio = "Tanti auguri! La multi ani! Happy New Year!"
    lunghezza = len(messaggio.split())
    print(f"Il messaggio ({messaggio}) è composto da {lunghezza} parole.")

def sfida4():
    print("Crea un programma che generi automaticamente i nomi degli elfi che aiutano Babbo Natale."
          "Il programma chiederà due input, uno che selezioni il nome e l'altro il cognome")

    lista_nomi = ["Neve", "Fiocco", "Ghirlanda", "Albero", "Strenna", "Gingerbread",
                  "Agrifoglio", "Cannella", "Biscotto", "Vischio", "Candela"]
    lista_cognomi = ["Allegro", "scintillante", "minuscolo", "gioioso", "vivace", "gelido", "soffice",
                     "ridacchiante", "lucido", "scintillante", "piccante", "carino", "cattivo", "volante",
                     "frizzante", "sfacciato", "luminoso", "splendente", "rimbalzante", "coccolante"]

    domanda_nome = input("Vuoi scegliere un nome dalla lista? (sì/no) ")
    if domanda_nome == "sì":
        for nome in lista_nomi:
            print(nome.capitalize())
        nome = input("Scegli il nome che ti piace: ")
        print(f"Ok, hai scelto {nome}.")

        domanda_cognome = input("Procediamo con il cognome? (sì/no) ")
        if domanda_cognome == "sì":
            for cognome in lista_cognomi:
                print(cognome.capitalize())
            cognome = input(f"Scegli il cognome che più si abbina al nome: ")
            print(f"Molto bene, hai scelto {cognome}.")

            print(f"\nL'elfo, che aiuterà Babbo Natale, si chiamerà {nome} {cognome}.")





if __name__ == "__main__":
    sfida1(),
    sfida2(),
    sfida3(),
    sfida4()