def laptop_nuovo(ram, cpu, antivirus=False):
    print("Il laptop avrà le seguenti caratteristiche:")
    print("RAM:", ram)
    print("CPU:", cpu)
    if antivirus:
        print("Antivirus attivo")

laptop_nuovo("16Gb", "i7", antivirus=True)

def addizione(a, b):
    ris = a + b
    return ris

risultato = addizione(21, 9)
print(risultato)





