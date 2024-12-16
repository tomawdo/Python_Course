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
