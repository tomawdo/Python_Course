'''
dati = ["Angela", 51, "Maria", 12, "Dario", 34, "Marco", 34]
print(dati[0], dati[1])

targhe = ["AB345CV", "FR678AM", "ER772GD"]
print(targhe)

numeri = [10, 20, 30 ,40]
print(numeri[3])

a = 1
b = 5
c = 3

VarBool = a > b
print(VarBool)
'''

#dati = [37, 52.5, "camicia"]
#anni = [2024, 2025, 2209, 1988, 2007]
paniere_frutta = ["mela", "pera", "uva", "anguria", "melone", "arancia"]

#for frutto in paniere_frutta:
#    print(frutto)

for i in range(len(paniere_frutta)-1, -1, -1):
    print(paniere_frutta[i])
