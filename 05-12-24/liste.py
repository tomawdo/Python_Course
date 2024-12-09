# Le liste sono collezioni ordinate e modificabili. Permettono duplicati
# Le tuple sono collezioni ordinate ma immutabili. Permettono duplicati

# I set sono collezioni non ordinate e perciò non indicizzate. Non permettono duplicati
# I dictionary sono collezioni ordinate* e modificabili (dalla versione 3.7). Non permettono duplicati

# Liste + len() + type() + list()
x = ["Milano", "Roma", "Napoli", "Palermo"]
y = ["Ciao!", 24, False]
z = list(("Milano", "Roma", "Napoli", "Palermo")) # lista di array

print(len(x)) # len() conta gli elementi in lista
print(type(x)) # type() identifica il tipo di lista
print(type(z)) # type() identifica il tipo di lista

print(x[-2])
print(x[2:4])

























