d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))

d = {"name": "Alice", 1: "Python", (1, 2): [1, 2, 4]}

# Iterare sulle chiavi e stampare chiave e valore
for key in d:
    print(f"Chiave: {key}, Valore: {d[key]}")


# ESERCIZIO in PyTHON - creare un dizionario con chiave - valore (nome - voto universitario) max 10 alunni
# visualizzare a video la media dei voti di tutti gli alunni

# Creazione di un dizionario predefinito con massimo 10 alunni
alunni = {
    "Anna": 28,
    "Marco": 25,
    "Luca": 30,
    "Sara": 27,
    "Elena": 24,
    "Giulia": 26,
    "Paolo": 29,
    "Francesca": 22,
    "Giovanni": 21,
    "Marta": 23
}

# Calcolo della media dei voti
media_voti = sum(alunni.values()) / len(alunni)

# Stampa del dizionario e della media dei voti
print("I voti degli alunni sono:")
for nome, voto in alunni.items():
    print(f"{nome}: {voto}")

print(f"\nLa media dei voti è: {media_voti:.2f}")


# Lista di nomi predefiniti e voti
nomi = ["Anna", "Marco", "Luca", "Sara", "Elena", "Giulia", "Paolo", "Francesca", "Giovanni", "Marta"]
voti = [28, 25, 30, 27, 24, 26, 29, 22, 21, 23]

# Creazione del dizionario con un ciclo for
alunni = {}
for i in range(10):  # Massimo 10 alunni
    alunni[nomi[i]] = voti[i]

# Calcolo della media dei voti
media_voti = sum(alunni.values()) / len(alunni)

# Stampa del dizionario e della media
print("I voti degli alunni sono:")
for nome, voto in alunni.items():
    print(f"{nome}: {voto}")

print(f"\nLa media dei voti è: {media_voti:.2f}")


# chiedere in input un nome presente nella lista e modificare il voto dello studente (chiedere in input anche il nuovo voto)

# stampare a video i voti di ogni alunno con il voto espresso in decimi anziché in trentesimi

# Lista di nomi predefiniti e voti
nomi = ["Anna", "Marco", "Luca", "Sara", "Elena", "Giulia", "Paolo", "Francesca", "Giovanni", "Marta"]
voti = [28, 25, 30, 27, 24, 26, 29, 22, 21, 23]

# Creazione del dizionario con un ciclo for
alunni = {}
for i in range(10):  # Massimo 10 alunni
    alunni[nomi[i]] = voti[i]

# Chiedere all'utente di modificare il voto di uno studente
nome = input("Inserisci il nome dello studente per modificare il voto: ").strip()

if nome in alunni:
    nuovo_voto = float(input(f"Inserisci il nuovo voto per {nome}: "))
    alunni[nome] = nuovo_voto
else:
    print("Nome non trovato nella lista.")

# Stampare i voti in decimi anziché in trentesimi
print("\nI voti degli alunni in decimi sono:")
for nome, voto in alunni.items():
    voto_in_decimi = voto / 3  # Conversione in decimi
    print(f"{nome}: {voto_in_decimi:.1f}")
