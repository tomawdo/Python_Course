d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))

d = {"name": "Alice", 1: "Python", (1, 2): [1, 2, 4]}

for key in d:
    print(f"Chiave: {key}, Valore: {d[key]}")

# ESERCIZIO - creare un dizionario con chiave - valore (nome - voto universitario) max 10 alunni
# visualizzare a video la media dei voti di tutti gli alunni

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

nomi = ["Anna", "Marco", "Luca", "Sara", "Elena", "Giulia", "Paolo", "Francesca", "Giovanni", "Marta"]
voti = [28, 25, 30, 27, 24, 26, 29, 22, 21, 23]

alunni = {}
for i in range(10):  # Massimo 10 alunni
    alunni[nomi[i]] = voti[i]

media_voti = sum(alunni.values()) / len(alunni)

print("I voti degli alunni sono:")
for nome, voto in alunni.items():
    print(f"{nome}: {voto}")

print(f"\nLa media dei voti è: {media_voti:.2f}")

# chiedere di inserire un nome presente nella lista e
# modificare il voto dello studente (chiedere in input anche il nuovo voto)
# stampare a video i voti di ogni alunno con il voto espresso in decimi anziché in trentesimi
# Lista di nomi predefiniti e voti
# Creazione del dizionario con massimo 10 alunni e i rispettivi voti
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

nome = input("Inserisci il nome dello studente per modificare il voto: ").strip()
cognome = str()

if nome in alunni:
    nuovo_voto = float(input(f"Inserisci il nuovo voto per {nome}: "))
    alunni[nome] = nuovo_voto
else:
    print("Nome non trovato nel dizionario.")

print("\nI voti degli alunni in decimi sono:")
for nome, voto in alunni.items():
    voto_in_decimi = voto / 3  # Conversione in decimi
    print(f"{nome}: {voto_in_decimi:.1f}")

# Creare un dizionario strutturato in cognome, voto, materia. Una classe con cognome voto e materia.
# Se la media dei voti è minore di 6, i voti vengono alzati secondo la seguente regola:
# - i voti minori di 4.5 (incluso) vengono alzati di 0.75 
# - i voti tra 5 e 6.5 (escluso) vengono alzati di 0.5
# - i voti compresi tra 6.5 (incluso) e 7 (escluso) vengono alzati di 0.75
# - gli altri voti non vengono alzati

# 1. Creare il dizionario con i dati della classe
classe = {
    "Rossi": {"voto": 5.0, "materia": "Matematica"},
    "Bianchi": {"voto": 4.5, "materia": "Fisica"},
    "Verdi": {"voto": 6.8, "materia": "Chimica"},
    "Neri": {"voto": 7.2, "materia": "Storia"},
    "Gialli": {"voto": 3.9, "materia": "Inglese"},
}

somma_voti = 0 # media dei voti
numero_studenti = len(classe)

for studente in classe.values():
    somma_voti += studente["voto"]

media_voti = somma_voti / numero_studenti
print(f"Media dei voti iniziale: {media_voti:.2f}")

if media_voti < 6:
    for studente in classe.values():
        voto = studente["voto"]

        if voto <= 4.5: # Applicare le regole di modifica
            studente["voto"] += 0.75
        elif 5 <= voto < 6.5:
            studente["voto"] += 0.5
        elif 6.5 <= voto < 7:
            studente["voto"] += 0.75

print("\nVoti aggiornati:") # 4. stampo i risultati
for cognome, dati in classe.items():
    print(f"{cognome}: {dati['voto']:.2f} ({dati['materia']})")

somma_voti_aggiornati = 0 # Nuova media dei voti
for studente in classe.values():
    somma_voti_aggiornati += studente["voto"]

nuova_media_voti = somma_voti_aggiornati / numero_studenti
print(f"\nNuova media dei voti: {nuova_media_voti:.2f}")


