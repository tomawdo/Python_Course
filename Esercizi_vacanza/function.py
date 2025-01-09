from datetime import datetime
import matplotlib.pyplot as plt

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

def sfida5():
    print("Scrivi un programma che calcoli il tempo necessario per calcolare quanto tempo che ci vuole per"
          "\nprodurre un determinato tipo di giocattolo (es. bambola, trenino, lego...). Il programma prende in"
          "\ninput: la tipologia di giocattolo (a cui avrai associato un tempo di realizzazione per elfo es. 1 elfo"
          "\nproduce 1 bambola in 1 ora), e il numero di pezzi da realizzare e quanti elfi sono disponibili a"
          "\nlavorare su quell'ordine. Restituisce come risultato il numero delle ore necessarie per soddisfare"
          "\nquell'ordine")

    dati_lego = {
        "LEGO Millennium Falcon": {"elfi_operativi": 5, "ore_necessarie": 10},
        "LEGO Technic Bugatti Chiron": {"elfi_operativi": 4, "ore_necessarie": 9},
        "LEGO Hogwarts Castle": {"elfi_operativi": 6, "ore_necessarie": 12},
        "LEGO Titanic": {"elfi_operativi": 8, "ore_necessarie": 15},
        "LEGO Star Wars AT-AT": {"elfi_operativi": 7, "ore_necessarie": 13}
    }

    nomi_lego = list(dati_lego.keys()) # associo i numeri ai giochi

    while True:
        domanda = input(
            "Vuoi calcolare il tempo di assemblaggio di uno dei più famosi LEGO? (sì/no o 0 per uscire): ").lower()

        if domanda == "0" or domanda == "no":
            print("Alla prossima!")
            break
        elif domanda == "sì":
            print("\nEcco i LEGO disponibili:")
            for i, gioco in enumerate(nomi_lego, 1):
                print(f"{i}. {gioco}")

            scelta = int(input("\nScegli il tuo LEGO preferito (1-5): "))
            if 1 <= scelta <= len(nomi_lego):
                lego_scelto = nomi_lego[scelta - 1]
                elfi = dati_lego[lego_scelto]["elfi_operativi"]
                ore = dati_lego[lego_scelto]["ore_necessarie"]

                nr_assemblaggi = int(input(f"\nOttimo! Quanti esemplari vuoi assemblare di {lego_scelto}? "))
                nr_ore_assemblaggio = nr_assemblaggi * ore

                print(
                    f"\nPer assemblare {nr_assemblaggi} esemplari di {lego_scelto}, servono {elfi} Elfi e {nr_ore_assemblaggio} ore di assemblaggio.\n")
            else:
                print("\nScelta non valida. Riprova.\n")
        else:
            print("\nInput non valido. Inserisci 'sì', 'no' o '0' per uscire.\n")

def sfida6():
    print("Scegli una canzone di Natale di tuo gusto e scrivi un programma "
          "che stampi una riga sì e una riga no di quella canzone")

    canzone = """Jingle bells jingle bells
oh che bello andar
bello andare col cavallo
sulla neve bianca.
Jingle bells jingle bells
oh che bello andar
scivolando con la slitta
nel silenzio andiam."""

    print(f"\n{canzone}")

    righe = canzone.splitlines()
    for i, riga in enumerate(righe):
        if i % 2 == 0:
            print(f"\n{riga}")

def sfida7():
    print(
        "Scrivi un programma che ti permetta di inserire data e ora corrente e calcoli quanto tempo manca al Natale.\n")
    data_corrente_str = input("Inserisci la data di oggi (formato: YYYY-MM-DD): ")

    try:
        data_corrente = datetime.strptime(data_corrente_str, "%Y-%m-%d")
    except ValueError:
        print("Formato della data non valido. Usa il formato YYYY-MM-DD.")
        return

    natale = datetime(data_corrente.year, 12, 25)
    if data_corrente > natale:
        natale = datetime(data_corrente.year + 1, 12, 25)
    tempo_rimanente = natale - data_corrente
    print(f"Tempo rimanente fino a Natale: {tempo_rimanente}")

def sfida8():
    print("Scrivi un programma che calcoli il volume di una casa di zenzero, l'utente deve inserire base, altezza e profondità")

    base = int(input("Base in mm: "))
    altezza = int(input("Altezza in mm: "))
    profondo = int(input("Profondità in mm: "))

    result = base * altezza * profondo
    print(f"Il volume è {result} mm")

def sfida9():
    print("Scrivi un programma che permetta di dividere automaticamente il costo di una cena"
          "tra un gruppo di amici. Il programma prende in input il costo totale della cena e "
          "il numero di partecipanti e restituisce la quota procapite")
    
    costo = int(input("Inserisci il costo totale della cena: "))
    amici = int(input("In quanti eravate? "))
    print(f"La quota per ciascuno è di {costo / amici:.2f}")

def sfida10():
    filastrocca = input("Inserisci filastrocca: ")
    lettera = input("Inserisci la lettera da contare: ")

    result = filastrocca.lower().count(lettera.lower())
    print(f"La lettera '{lettera}' si ripete {result} volte nella filastrocca.")

def sfida11():
    print("Scrivi un programma che ti permetta di registrarti come aiutante di Babbo Natale. Se l'utente ha meno di 18 anni non può essere accettato")
    anno_nascita = int(input("Inserisci l'anno di nascita: "))

    anno = datetime.now().year
    result = anno - anno_nascita
    if result > 18:
        print(f"Ottimo, poiché hai {result}, sei un lil Babbo.")
    else:
        print("Purtroppo sei minorenne.")

def sfida12():
    print("Calcola lo stipendio di un elfo. Prendi in input le ore lavorate "
          "mensilmente dall'elfo e la retribuzione oraria e restituisce lo stipendio mensile.")
    ore_lavorate = int(input("Quante ore ha lavorato? "))
    retribuzione_oraria = int(input("Quale è la paga oraria? "))
    stipendio = ore_lavorate * retribuzione_oraria

    print(f"Stipendio elfico: {stipendio:.2f}EUR")

def sfida13():
    print("Dato il peso massimo trasportabile dalla slitta di Babbo Natale, crea un programma che"
          " permetta di inserire i pesi dei regali finché non si raggiunge il limite consentito.")

    peso_massimo = int(input("Qual è il peso massimo trasportabile dalla slitta? "))
    regali = []
    peso_totale = 0

    print("\nInizia ad aggiungere i pesi dei regali (uno alla volta).")
    while peso_totale < peso_massimo:
        peso_regalo = int(input("Inserisci il peso del regalo: "))
        if peso_totale + peso_regalo > peso_massimo:
            print(f"\nNon puoi aggiungere un regalo di peso {peso_regalo}. Supererebbe il limite di {peso_massimo}.")
            continue
        regali.append(peso_regalo)
        peso_totale += peso_regalo

        print(f"Regalo aggiunto! Peso totale: {peso_totale}/{peso_massimo}.")
    print("\nLa slitta è piena! Ecco i pesi dei regali caricati:")
    print(regali)

def sfida14():
    print("Calcolo della distanza percorsa da una palla di neve e verifica della barriera del suono.")
    print("La barriera del suono è fissata a 343 m/s (velocità del suono a livello del mare).\n")

    try:
        ms = float(input("Inserisci la velocità della palla di neve (m/s): "))
        s = float(input("Inserisci il tempo di viaggio (s): "))

        if ms <= 0 or s <= 0:
            print("La velocità e il tempo devono essere numeri positivi. Riprova.")
            return

        distanza = ms * s
        if ms > 343:
            print(f"\nLa palla di neve ha infranto la barriera del suono! (Velocità: {ms:.2f} m/s)")
            tempo_per_1km = 1000 / ms
            print(f"A questa velocità, percorrere 1 km richiederebbe {tempo_per_1km:.2f} secondi.")
        else:
            differenza = 343 - ms
            print(f"\nLa palla di neve NON ha infranto la barriera del suono.")
            print(f"Manca una velocità aggiuntiva di {differenza:.2f} m/s per superarla.")

        if distanza > 1000:
            km = distanza / 1000
            print(f"\nDistanza percorsa: {km:.2f} km")
        else:
            print(f"\nDistanza percorsa: {distanza:.2f} metri")

    except ValueError:
        print("Errore: Inserisci numeri validi per la velocità e il tempo.")






if __name__ == "__main__":
    sfida1(),
    sfida2(),
    sfida3(),
    sfida4(),
    sfida5(),
    sfida6(),
    sfida7(),
    sfida8(),
    sfida9(),
    sfida10(),
    sfida11(),
    sfida12(),
    sfida13(),
    sfida14()
