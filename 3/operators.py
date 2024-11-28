# Operatori aritmetici
# -------------------
a = 10
b = 3

# Addizione
somma = a + b  # 10 + 3 = 13

# Sottrazione
differenza = a - b  # 10 - 3 = 7

# Moltiplicazione
prodotto = a * b  # 10 * 3 = 30

# Divisione
divisione = a / b  # 10 / 3 = 3.333...

# Divisione intera
divisione_intera = a // b  # 10 // 3 = 3

# Modulo (resto della divisione)
resto = a % b  # 10 % 3 = 1

# Esponenziale
potenza = a ** b  # 10 ** 3 = 1000


# Operatori di confronto
# ----------------------
x = 5
y = 8

# Uguale
uguale = x == y  # False

# Diverso
diverso = x != y  # True

# Maggiore
maggiore = x > y  # False

# Minore
minore = x < y  # True

# Maggiore o uguale
maggiore_uguale = x >= y  # False

# Minore o uguale
minore_uguale = x <= y  # True


# Operatori logici
# ----------------
p = True
q = False

# AND logico
and_logico = p and q  # False

# OR logico
or_logico = p or q  # True

# NOT logico
not_logico = not p  # False


# Operatori di assegnazione
# -------------------------
z = 7

# Assegnazione semplice
z = 7  # z è 7

# Assegnazione con somma
z += 3  # z = z + 3 -> z è 10

# Assegnazione con sottrazione
z -= 2  # z = z - 2 -> z è 8

# Assegnazione con moltiplicazione
z *= 2  # z = z * 2 -> z è 16

# Assegnazione con divisione
z /= 4  # z = z / 4 -> z è 4.0

# Assegnazione con modulo
z %= 3  # z = z % 3 -> z è 1.0

# Assegnazione con divisione intera
z //= 2  # z = z // 2 -> z è 0.0

# Assegnazione con esponenziale
z **= 3  # z = z ** 3 -> z è 0.0


# Operatori di appartenenza
# -------------------------
lista = [1, 2, 3, 4]

# Appartiene
appartiene = 2 in lista  # True

# Non appartiene
non_appartiene = 5 not in lista  # True


# Operatori di identità
# ---------------------
a = [1, 2, 3]
b = a
c = [1, 2, 3]

# È lo stesso oggetto
stesso_oggetto = a is b  # True

# Non è lo stesso oggetto
diverso_oggetto = a is not c  # True


# Operatori bitwise (lavorano a livello di bit)
# ---------------------------------------------
m = 5  # In binario: 0101
n = 3  # In binario: 0011

# AND bitwise
and_bitwise = m & n  # 0101 & 0011 = 0001 (1 in decimale)

# OR bitwise
or_bitwise = m | n  # 0101 | 0011 = 0111 (7 in decimale)

# XOR bitwise
xor_bitwise = m ^ n  # 0101 ^ 0011 = 0110 (6 in decimale)

# Complemento bitwise (NOT)
complemento = ~m  # ~0101 = 1010 (in complemento a due)

# Shift a sinistra
shift_sinistra = m << 1  # 0101 << 1 = 1010 (10 in decimale)

# Shift a destra
shift_destra = m >> 1  # 0101 >> 1 = 0010 (2 in decimale)