from random import *

"""
# Lanzamiento de dados
def lanzar_dados():
    suma = randint(1, 6) + randint(1, 6)
    return suma


# Evaluar la jugada
def evaluar(x):
    suma_dados = x
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados <= 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


print(evaluar(lanzar_dados()))
"""


# Lanzamiento de dados
def lanzar_dados():
    r = randint(1, 6)
    s = randint(1, 6)
    return r, s


# Evaluar la jugada
def evaluar_jugada(x, y):
    suma_dados = x + y
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


jugada = list(lanzar_dados())
print(evaluar_jugada(jugada[0], jugada[1]))
