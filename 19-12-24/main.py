# Definizione delle funzioni
def aggiungi_altezza(altezze):
    altezza = float(input("Inserisci l'altezza in centimetri: "))
    altezze.append(altezza)
    print("Altezza aggiunta con successo.")

def elimina_altezza(altezze):
    altezza = float(input("Inserisci l'altezza da eliminare in centimetri: "))
    if altezza in altezze:
        altezze.remove(altezza)
        print("Altezza eliminata con successo.")
    else:
        print("Altezza non trovata nella lista.")

def suddividi_in_gruppi(altezze):
    soglia = float(input("Inserisci la soglia per suddividere le altezze in gruppi: "))
    gruppo1 = [a for a in altezze if a <= soglia]
    gruppo2 = [a for a in altezze if a > soglia]
    print(f"Gruppo 1 (<= {soglia} cm): {gruppo1}")
    print(f"Gruppo 2 (> {soglia} cm): {gruppo2}")

def calcola_media(altezze):
    if not altezze:
        print("La lista delle altezze è vuota. Impossibile calcolare la media.")
    else:
        media = sum(altezze) / len(altezze)
        print(f"La media delle altezze è: {media:.2f} cm")

def menu():
    altezze = []
    while True:
        print("\n--- Menu ---")
        print("1. Aggiungi altezza")
        print("2. Elimina altezza")
        print("3. Suddividi in gruppi")
        print("4. Calcola la media")
        print("5. Esci")
        
        scelta = input("Seleziona un'opzione: ")
        
        if scelta == '1':
            aggiungi_altezza(altezze)
        elif scelta == '2':
            elimina_altezza(altezze)
        elif scelta == '3':
            suddividi_in_gruppi(altezze)
        elif scelta == '4':
            calcola_media(altezze)
        elif scelta == '5':
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")

# Funzione principale che avvia il menu
if __name__ == "__main__":
    menu()
