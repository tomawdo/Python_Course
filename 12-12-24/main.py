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