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


PIN_CORRETTO = "1234"  # PIN corretto
MAX_TENTATIVI = 3  # Numero massimo di tentativi
tentativi = 0  # Numero di tentativi effettuati

while tentativi < MAX_TENTATIVI:
    pin_inserito = input("Inserisci il PIN: ")
    
    if pin_inserito == PIN_CORRETTO:
        print("Il tuo PIN è corretto.")
        break
    else:
        tentativi += 1
        tentativi_rimasti = MAX_TENTATIVI - tentativi
        print("Il tuo PIN non è corretto.")
        
        if tentativi_rimasti > 0:
            print(f"Hai ancora {tentativi_rimasti} tentativi.")
        else:
            print("La banca ha bloccato la tua carta.")


# scrivete un programma che legga una sequenza di numeri interi che visualizzino quanto segue:
# - valore minimo e valore massimo tra quelli acquisiti
# - i pari ed i dispari
# - le somme parziali di tutti i numeri acqusiti, calcolate e visualizzate dopo ogni 
# nuova acquisizione (es. i valori in ingresso sono 1729, il programma visualizzerà 1 8 10 19)
