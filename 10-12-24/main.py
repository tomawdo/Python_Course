# LISTE
'''
# Esempio di list comprehension
city_names = ["Torino", "Milano", "Roma", "Napoli", "Messina"]

# espressione for elemento in lista_elementi if condizione == vera
[print(city) for city in city_names if city != "Roma"]

city_names.sort(reverse=True)
print(city_names)

# Copiare una lista con .copy()
x = ["Torino", "Milano", "Roma", "Napoli", "Messina"]
y = x.copy()
y[0] = "New York"
# print(y)

# unire più liste insieme con +, append(), extend()
x = ["Peugeot", "Fiat", "Renault"]
y = ["Audi", "Volvo"]

for brand in y: x.append(brand) # metodo con ciclo for
x.extend(y) # metodo con extend()

print(x)
'''

# TUPLE: sono ordinate, indicizzate, non modificabili e permettono duplicati

x = ("Milano", "Roma", "Napoli")
y = tuple(("Milano", "Roma", "Napoli"))
z = ("Milano")

print(len(x))
print(y)
print(type(z))

