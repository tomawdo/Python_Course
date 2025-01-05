def sfida1():
    print("Scrivi un programma che permetta a un negoziante di calcolare lo sconto. "
          "Il programma prende in input il prezzo iniziale e lo sconto applicato, restituendo il prezzo finale scontato.")
    try:
        listino_base = float(input("Inserisci il prezzo base (€): "))
        sconto = float(input("Inserisci lo sconto dedicato (%): "))
        prezzo_scontato = listino_base - (listino_base * sconto) / 100

        print(f"Il prezzo a te dedicato è: €{prezzo_scontato:.2f}")
    except ValueError:
        print("Controlla che abbia inserito valori numerici. Riprova!")






if __name__ == "__main__":
    sfida1()