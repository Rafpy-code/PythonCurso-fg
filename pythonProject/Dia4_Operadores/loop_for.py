# Debe ser un objeto iterable
nombres = ['Juan', 'Perico', 'Dulce', 'Jeydan']

print("Nombres que empiezan con 'D' o 'J'")
for nombre in nombres:
    indice = nombres.index(nombre) + 1
    if nombre.startswith('D') or nombre.startswith('J'):
        print(f"{indice}.- Hola {nombre}")

numeros = [1, 4, 45, 23, 34]
mi_valor = 0
print(numeros)

for numero in numeros:
    print(f"mi_valor ahora vale: {mi_valor}")
    mi_valor += numero

palabra = 'python'
print(palabra)
for letra in palabra:
    print(letra)

lista_de_listas = [[5, 7], [3, 9], ['rana', 'salta']]
print(lista_de_listas)
print("Listas de las listas")
for lista in lista_de_listas:
    print(lista)
print("Elemento de cada lista")
for a, b in lista_de_listas:
    print(a)
    print(b)

diccionario = {'clave1': 15, 'clave2': "ratón", 'clave3': [4, 8]}
print(diccionario)

print("Claves")
for clave in diccionario:
    print(clave)

print("Clave, valor")
for item in diccionario.items():
    print(item)

print("Valores del diccionario")
for valor in diccionario.values():
    print(valor)

print("Otra manera de clave, valor")
print(diccionario)
for a, b in diccionario.items():
    print(a, b)
