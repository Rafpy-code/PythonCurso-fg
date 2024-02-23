
print("for numero in range(5):")
for numero in range(5):
    print(numero)

print("\nfor numero in range(1, 6):")
for numero in range(1, 6):
    print(numero)

print("\nfor numero in range(1, 15, 2):")
for numero in range(1, 15, 2):
    print(numero)

print("\nlista = list(range(1, 101))")
lista = list(range(1, 101))
print(lista)

print("\nsuma_cuadrados, list(range(1, 16))")
suma_cuadrados = 0
numeros = list(range(1, 16))
for numero in numeros:
    numero_cuadrado = numero ** 2
    suma_cuadrados += numero_cuadrado
print(suma_cuadrados)
