'''
# BITWISE
a = 15
b = 8
'''

#a = 3
#b = 2
#print(bin(a), bin(b))
#print(a & b) # AND BIT a BIT
#print(a | b) # OR BIT a BIT

# SHIFT
# a = 8
#n = 1
#print(a << n)

def my_function(country = "Italy"):
    print(f"I' from {country}")

my_function("Canada")


# Funzione Fattoriale n!

def factorial(n):
    if n < 2:
        return n
    else:
        return n * factorial(n - 1)

print(factorial(5))