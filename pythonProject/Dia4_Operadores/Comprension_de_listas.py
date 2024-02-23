palabra = 'Python'
print(palabra)
lista = []

print("\nlista.append(letra)")
for letra in palabra:
    lista.append(letra)
print(lista)

print("\n[letra for letra in 'Python']")
lista1 = [letra for letra in 'Python']
print(lista1)

print("\n[numero for numero in range(0, 21, 2)]")
lista2 = [numero for numero in range(0, 21, 2)]
print(lista2)

print("\n[numero/2 for numero in range(0, 21, 2)]")
lista3 = [numero / 2 for numero in range(0, 21, 2)]
print(lista3)

print("\n[numero for numero in range(0, 21, 2) if numero * 2 > 10]")
lista4 = [numero for numero in range(0, 21, 2) if numero * 2 > 10]
print(lista4)

print("\n[numero if numero * 2 > 10 else 'Es menor que 10' for numero in range(0, 21, 2)]")
lista5 = [numero if numero * 2 > 10 else 'Es menor que 10' for numero in range(0, 21, 2)]
print(lista5)

print("\n[(pie * 3.281) for pie in pies]")
pies = [10, 20, 30, 40]
# metros = [round((pie * 3.281), 2) for pie in pies]
metros = [(pie * 3.281) for pie in pies]
print(pies)
print(metros)

print("\n[valor ** 2 for valor in valores]")
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [valor ** 2 for valor in valores]
print(valores)
print(valores_cuadrado)

print("\n[valor for valor in valores if valor % 2 == 0]")
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [valor for valor in valores if valor % 2 == 0]
print(valores_pares)

print("\n[(grados_fahrenheit - 32)*(5/9) for grados_fahrenheit in temperatura_fahrenheit]")
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(grados_fahrenheit - 32) * (5 / 9) for grados_fahrenheit in temperatura_fahrenheit]
print(temperatura_fahrenheit)
print(grados_celsius)

print("\n[n for n in range(0, 21, 2) if n * 2 > 10]")
lis = [n for n in range(0, 21, 2) if n * 2 > 10]
print(lis)

print("\n[n if n * 2 > 10 else 'no' for n in range(0, 21, 2)]")
lista = [n if n * 2 > 10 else 'menor que 10' for n in range(0, 21, 2)]
print(lista)
