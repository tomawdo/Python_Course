def calcolatrice():
    operazione = input("Inserisci l'operazione (+, -, *, /): ")
    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))

    if operazione == '+':
        print(f"Risultato: {num1 + num2}")
    elif operazione == '-':
        print(f"Risultato: {num1 - num2}")
    elif operazione == '*':
        print(f"Risultato: {num1 * num2}")
    elif operazione == '/':
        if num2 != 0:
            print(f"Risultato: {num1 / num2}")
        else:
            print("Errore: divisione per zero.")
    else:
        print("Operazione non valida.")

calcolatrice()
        
