while True:
    numero = int(input("Inserisci un numero: "))
    conversione = bin(numero)[2:]
    print(f"Il numero {numero} convertito in binario {conversione}")