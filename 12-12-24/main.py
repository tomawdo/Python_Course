# DEFINIZIONE: Le funzioni sono un blocco di informazioni al cui interno
# sono delle istruzioni che verranno eseguite ogni volta che chiameremo la funzione

# - parametri in funzione
# - differenza tra argomenti e parametri
# - parametri di default
# - return dei valori


# il parametro è in fase di definizione e possiamo avere più parametri in linea
# l'argomento è il valore effettivo che mettiamo in fase di esecuzione

'''
def fai_la_pasta(tipo_pasta = "spaghetti"):
    print("metti l'acqua")
    print("falla bollire")
    print("metti " + tipo_pasta)
    print("Apparecchia il tavolo!")
    return True

pasta_pronta = fai_la_pasta()

if pasta_pronta:
    print("Venite a tavola!")
'''

def fai_somma(num1, num2):
    somma = num1 + num2
    return somma

x = fai_somma(2, 2)
print(x)


# chiedere all'utente quanti esami ha dato
# chiedere all'utente i voti degli esami ed inserirli in una lista
# calcolare la media ponderata degli esami dati sia in trentesimi e sia in 110

numero_esami = int(input("Quanti esami hai dato? "))

voti = []
crediti = []

# Raccogli i voti e i crediti per ogni esame
for i in range(numero_esami):
    voto = int(input(f"Inserisci il voto dell'esame {i + 1} (in trentesimi): "))
    credito = int(input(f"Inserisci i crediti dell'esame {i + 1}: "))
    voti.append(voto)
    crediti.append(credito)

# Calcola la somma pesata e il totale dei crediti con un for esplicito
somma_pesata = 0
totale_crediti = 0

for i in range(numero_esami):
    somma_pesata += voti[i] * crediti[i]
    totale_crediti += crediti[i]

# Calcola la media ponderata in trentesimi
media_ponderata_trentesimi = somma_pesata / totale_crediti

# Converti la media in 110
media_ponderata_110 = (media_ponderata_trentesimi / 30) * 110

# Mostra i risultati
print(f"\nMedia ponderata in trentesimi: {media_ponderata_trentesimi:.2f}")
print(f"Media ponderata in 110: {media_ponderata_110:.2f}")


