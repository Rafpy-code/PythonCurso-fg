numero = 10
while numero >= 0:
    print(numero)
    numero -= 1

print()
numero = 50
while (numero <= 50) and (numero >= 0):
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1

print()
lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]
print(lista_numeros)
for numero in lista_numeros:
    if numero > 0:
        print(numero)
    else:
        break
print(f"Ha introducido el primer valor negativo {numero}, fin del loop_for")

print()
monedas = 5
print(monedas)
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo monedas")

respuesta = 's'
while respuesta == 's':
    respuesta = input("¿Deseas continuar? s/n -> ").lower()
else:
    print("Gracias!")

while respuesta == 'x':
    # Cuando no sabemos que código vamos a poner.
    pass

print()
nombre = input("Escribe tu nombre ").lower()
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)
