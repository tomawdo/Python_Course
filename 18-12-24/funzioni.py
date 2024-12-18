#crea una lista che prende in input una lista e somma i numeri

def somma_pari(lista):
    somma = 0
    for numero in lista:
        if numero % 2 == 0:
            somma += numero
    return somma
def n_merz(n, rule):
    step = [1, 1]

    for i in range(len(step), n):
        print(i)
        nuovo_num = rule(step[i-1], step[i-2])
        step.append(nuovo_num)
    return step
def regola_somma(x, y):
    return x + y

def crea_dizionario(nomi, stipendi):
    if len(nomi) != len(stipendi):
        print("Le due liste devono avere la stessa lunghezza.")
    dizionario = nomi, stipendi
    return dizionario
