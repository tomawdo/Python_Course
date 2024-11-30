import random

NR_MAX_QUOTE = 5
MAX_SCOMMESSA = 100
MIN_SCOMMESSA = 10

# struttura ruota slotmachine 3 righe * 3 colonne
RIGHE = 3
COLONNE = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(reels, lines, bet_amount, pay_values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = reels[0][line]  # Cambia 'lines' in 'line'
        for reel in reels:
            symbol_to_check = reel[line]  # Cambia 'lines' in 'line'
            if symbol != symbol_to_check:
                break
        else:
            winnings += pay_values[symbol] * bet_amount
            winning_lines.append(line + 1)
    return winnings, winning_lines

def girare_slotmachine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_counts in symbols.items(): #es il simbolo A comparirà 2 volte
        for _ in range(symbol_counts):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposito(): # scrivo la funzione deposito
    while True: # ciclo l'operazione
        importo = input("Quanto vuoi caricare? €") # chiedo all'utente di inserire una somma
        if importo.isdigit(): # controllo che l'importo sia un numero
            importo = int(importo) # converto l'importo in intero
            if importo > 0: # controllo che l'importo sia maggiore di zero
                break # proseguo con l'operazione
            else:
                print("L'importo deve essere maggiore di 0 (zero).") # informo l'utente che l'importo deve essere maggiore di zero.
        else:
            print("Attenzione! Inserisci un numero corretto.") # poiché non è un numero, chiedo di inserire un numero.
    return importo

def ottengo_nr_quote():
    while True: # ciclo l'operazione
        quote = input("Quante quote vuoi scommettere (1 - " + str(NR_MAX_QUOTE) + ")? ")
        if quote.isdigit(): # controllo quote -> numero
            quote = int(quote) # converto quote -> intero
            if 1 <= quote <= NR_MAX_QUOTE: # controllo quote siano tra 1 e 3 (nr_max_righe)
                break # proseguo con l'operazione
            else:
                print("Inserisci un numero valido di quote.") # informo l'utente che l'importo deve essere maggiore di zero.
        else:
            print("Attenzione! Inserisci un numero.") # poiché non è un numero, chiedo di inserire un numero.
    return quote

def ottengo_scommessa():
    while True:
        importo = input("Quanto vuoi scommettere per ogni riga? €")
        if importo.isdigit():
            importo = int(importo)
            if MIN_SCOMMESSA <= importo <= MAX_SCOMMESSA:
                break
            else:
                print(f"L'importo per ogni riga dev'essere tra €{MIN_SCOMMESSA} - €{MAX_SCOMMESSA}.")
        else:
            print("Inserisci un importo.")
    return importo

def game():
    quote = ottengo_nr_quote()
    scommessa = float(ottengo_scommessa())
    tot_scommessa = float(scommessa * quote)
    saldo = float(deposito())

    if tot_scommessa > saldo:
        print(f"Non hai sufficiente credito. Il tuo saldo è: €{saldo}")
    else:
        print(f"Hai scommesso €{scommessa} su {quote} quote. Totale: €{tot_scommessa}.")
        # Altra logica per la conclusione del gioco

    slots = girare_slotmachine(RIGHE, COLONNE, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, quote, scommessa, symbol_value)
    print(f"Hai vinto €{check_winnings}!")
    print(f"Hai vinto sulle quote: ", *winning_lines)

def main():
    saldo = float(deposito())

main()