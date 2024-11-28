user = "Admin"
checkUser = input("Inseisci nome utente: ")

if checkUser == user:
    print("corretto")
else:
    print("sbagliato")

num1 = input("Inserisci un dividendo: ")
num2 = input("Inserisci un divisore: ")
result = int(num1) / int(num2)

if result == 0:
    print("dispari")
else:
    print("pari")