from random import *

print("randint(1, 50)")
aleatorio = randint(1, 50)
print(aleatorio)

print("\nround(uniform(1, 50), 1)")
aleatorio = round(uniform(1, 50), 1)
print(aleatorio)

print("\nrandom()")
aleatorio = random()
print(aleatorio)

print()
colores = ['azul', 'rojo', 'verde', 'morado']
print(colores)
print("choice(colores)")
aleatorio = choice(colores)
print(aleatorio)

print()
numeros = list(range(5, 51, 2))
print(numeros)
print("La lista con shuffle(numeros)")
shuffle(numeros)
print(numeros)

print("\nrandint(1, 10)")
aleatorio = randint(1, 10)
print(aleatorio)

print()
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
print(nombres)
print("choice(nombres)")
sorteo = choice(nombres)
print(sorteo)

print()
frase = "cabaña del monte"
print(frase)
letra = choice(frase)
print(f"letra elegida {letra}")
