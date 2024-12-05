'''
# if metodo 1
user_input = input("Name: ")

if user_input:
    nome = user_input
else:
    nome = "ND"

print(nome)


# if metodo 2
user_input = input("Name: ")
nome = user_input or "ND"
print(nome)

'''
# Come rimuovere il prefisso o i primi 4 caratteri
# metodo 1

links = [
    "www.google.it",
    "www.youtube.com",
    "www.ansa.it",
    "www.wikipedia.org",
]

for link in links:
    #print(link.lstrip("www.")) #in questo caso elimina anche la w di wikipedia quindi ATTENZIONE!
    print(link.removeprefix("www.")) # .removeprefix è consigliato