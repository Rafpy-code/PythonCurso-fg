print("Uso de zip()")
nombres = ['Ramón', 'Dulce', 'Jeydan']
print(nombres)
edades = [49, 8, 2]
print(edades)
paises = ['Ecuador', 'España', 'Honduras']
print(paises)

print("\nSiempre hacer el cast de list(zip(nombres, edades, paises))")
combinados = list(zip(nombres, edades, paises))
print(combinados)

print("\nfor nombre, edad, pais in combinados:")
for nombre, edad, pais in combinados:
    print(f"{nombre} tiene {edad} y vive en {pais}")

print()
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
print(capitales)
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
print(paises)

print("\nlist(zip(paises, capitales)")
pais_capital = list(zip(paises, capitales))
for pais, capital in pais_capital:
    print(f"La capital de {pais} es {capital}")

print()
marcas = ['adidas', 'nike', 'levis']
print(marcas)
productos =['zapatillas', 'camiseta', 'pantalón 501']
print(productos)

print("\nprint(mi_zip)")
mi_zip = zip(marcas, productos)
print(mi_zip)
print("Imprime el espacio de memoria")

print("\nlist(zip(spanish, portugues, ingles))")
spanish = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
print(spanish)
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
print(portugues)
ingles = ['one', 'two', 'three', 'four', 'five']
print(ingles)
traduccion = list(zip(spanish, portugues, ingles))
print(traduccion)
