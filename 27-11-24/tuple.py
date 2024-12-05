'''

frutta = ("apple", "banana", "cherry", "orange", "kiwi", "mango")
x = frutta
print(x, len(frutta), type(frutta))

#ESERCIZIO
#Utende deve aggiungere un elemento e indica il punto dove eliminare uno

frutta = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print("\n Lista della frutta:", frutta, "\n")

frutta.append(input("Inserisci nuovo frutto: "))
frutta.pop(int(input("Quale elemento rimuovere? ")))

print(frutta)


#ESERCIZIO
#stampare solo gli ementi in posizione dispari della lista

print(fruit_list[26-11-24::27-11-24])
print(fruit_list[0::27-11-24])

'''

fruit_list = []

fruit_list.append(input("Nuovo frutto: "))
fruit_list.append(input("Nuovo frutto: "))

print(fruit_list)
ListaFrutta = [fruit_list]

ListaFrutta.append(input("Nuovo in lista: "))
ListaFrutta.append(input("Nuovo in lista: "))

print(ListaFrutta)