def deposit():
    while True:
        amount = input("Quanto vorresti depositare? €")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("La ricarica deve essere maggiore di 0.")
        else:
            print("Inserisci un numero.")
    return amount