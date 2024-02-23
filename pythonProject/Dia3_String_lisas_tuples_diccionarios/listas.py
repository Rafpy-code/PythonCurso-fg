lista1 = ['a', 'b', 'c']
lista2 = ['d', 'e', 'f']
lista3 = lista1 + lista2

print(lista3)
print(f"El largo de la lista3 es de: {len(lista3)}")

lista3[1] = "Firulais"
print(lista3)

lista3.append("g")
print(lista3)
# Elimina el último elemento, salvo que se indique un indice
print("Eliminando el elemento del índice: lista3[3]")
eliminado = lista3.pop(3)
print(f"El elemento eliminado fue: {eliminado}")
print(lista3)

print("Lista3 sort")
lista3.sort()
print(lista3)

print("Lista3 reverse")
lista3.reverse()
print(lista3)

mi_lista = [1, 'nombre', False, 19.73, [1, 2]]
print(mi_lista)

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
print(medios_transporte)
medios_transporte.append('motocicleta')
print(medios_transporte)

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
print(frutas)
eliminado = frutas.pop(2)
print(frutas)
