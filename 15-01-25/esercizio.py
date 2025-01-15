import re
# Prof. Luciana: luciana.trubian@gmail.com

def is_valid_email(email): # Controlla se l'email contiene almeno una @ seguita da un punto
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def lunghezza_pwd_ok(password):
    return 8 <= len(password) <= 15 # Controlla se la password è lunga tra 8 e 15 caratteri

def main():
    nome = input("Inserisci il tuo nome: ")
    cognome = input("Inserisci il tuo cognome: ")
    email = input("Inserisci la tua email: ")
    password = input("Inserisci la tua password: ")
    conferma_password = input("Conferma la tua password: ")

    if not is_valid_email(email):
        print("Email non valida. Assicurati che contenga una '@' e un punto dopo.")
        return
    
    if not lunghezza_pwd_ok(password):
        print("La password deve essere lunga tra 8 e 15 caratteri.")
        return

    if password != conferma_password:
        print("Le password non sono identiche. Riprova.")
        return

    user_data = {
        "nome": nome,
        "cognome": cognome,
        "email": email,
        "password": password
    }

    print("Dati inseriti correttamente!")
    print("Dati utente salvati nel dizionario:", user_data)

if __name__ == "__main__":
    main()