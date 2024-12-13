# Esercizio 1
# chiedi all'utente di inserire una parola e stampa le posizioni delle vocali presenti nella stringa

# Chiedi all'utente di inserire una parola
parola = input("Inserisci una parola: ")

# Definisci le vocali
vocali = "aeiouAEIOU"

# Trova le posizioni delle vocali nella parola
posizioni_vocali = [indice for indice, carattere in enumerate(parola) if carattere in vocali]

# Stampa le posizioni delle vocali
if posizioni_vocali:
    print("Le vocali si trovano alle seguenti posizioni:", posizioni_vocali)
else:
    print("Non ci sono vocali nella parola inserita.")
    
    
    
Quando utilizzate uno sportello bancario automatico (ATM, automatic teller machine) con la vostra
carta, dovete usare un numero identificativo personale (PIN, personal identification number) per
poter accedere al vostro conto. Se un utente sbaglia tre volte l’inserimento del PIN, la macchina
trattiene la carta e la blocca. Nell’ipotesi che il PIN dell’utente sia “1234”, scrivete un programma
che chieda all’utente di digitare il PIN, consentendo al massimo tre tentativi e agendo in questo
modo:
- se l’utente inserisce il numero corretto, visualizzate il messaggio “Il tuo PIN è corretto” e
terminate il programma;
- se l’utente inserisce un numero sbagliato, visualizzate il messaggio “Il tuo PIN non è corretto”
e, se avete chiesto il PIN meno di tre volte, chiedetelo di nuovo;
- se l’utente inserisce un numero sbagliato per tre volte, visualizzate il messaggio “La banca ha
bloccato la tua carta” e terminate il programma