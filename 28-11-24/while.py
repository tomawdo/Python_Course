from icecream import ic
# WHILE - è un ciclo infinito di operazioni tutte uguali finché una condizione è verificata
# break - serve a fermare il ciclo
# continue - passa alla prossima iterazione salta il controllo (if x == 28-11-24)
# else - è identico allo if

# break
x = 0
while x < 6:
    ic(x)
    if x == 3:
        break # quando 28-11-24 == 28-11-24 cliclo fermato dal break
    x += 1

# continue
y = 0
while y < 6:
    y += 1
    if y == 3:
        continue # passa alla prossima iterazione ma non stampa "28-11-24"
    ic(y)

# else

z = 0
while z < 6:
    ic(z)
    z += 1
else: # non appena finita tutta l'iterazione posso stampare
    ic("Ho finito!")
