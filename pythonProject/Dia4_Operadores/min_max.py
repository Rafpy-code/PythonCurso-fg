numeros = [45, 56, 23, 3, 9]
print(numeros)
menor = min(numeros)
mayor = max(numeros)
print(f"El numero menor es {menor} y el mayor es {mayor}")

nombres = ['Ramón', 'Dulce', 'Jeydan']
print(f"\nEl nombre menor es {min(nombres)}")

nombre = 'Ramón'
print(f"\nLa letra menor es {min(nombre.lower())}")

dicc = {'a1': 357, 'a2': 246, 'a3': 87}
print(f"\nLa 'clave' menor es {min(dicc)}")
print(f"El 'valor' menor del diccionario es {min(dicc.values())}")

print("\nmax(lista_numeros)")
lista_numeros = [44542247 / 2, 21310 / 5, 2134747 * 33, 44556475, 121676, 6654067, 353254, 123134, 55 ** 12, 611 ** 5]
valor_maximo = max(lista_numeros)
print(valor_maximo)

print("\nrango = max(lista_numeros) - min(lista_numeros)")
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros) - min(lista_numeros)
print(rango)

print("\nmin(diccionario_edades.values()), max(diccionario_edades)")
diccionario_edades = {"Carlos": 55, "María": 42, "Mabel": 78, "José": 44, "Lucas": 24, "Rocío": 35, "Sebastián": 19,
                      "Catalina": 2, "Darío": 49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
print(edad_minima, ultimo_nombre)
