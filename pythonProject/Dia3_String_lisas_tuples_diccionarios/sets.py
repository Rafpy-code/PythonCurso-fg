# No acepta valores repetidos, los elimina si existen(no los imprime)
# No admite diccionarios, ni listas, pero si tuples
mi_set = set((1, 2, 4))  # mi_set = set([1, 2, 4]) o mi_set = {1, 2, 3}
print(f"mi_set => {mi_set}")
print(type(mi_set))

otro_set = {4, 6, 7, 9, 4, 9, }
print(f"otro_set => {otro_set}")
print(type(otro_set))
print(len(otro_set))

# El 3 repetido no lo une
s1 = {1, 2, 3}
print(s1)
s2 = {3, 4, 5}
print(s2)
print("Uniendo dos sets => s3 = s1.union(s2)\nSi hay elementos repetidos los elimina")
s3 = s1.union(s2)
print(s3)

print("Añadiendo un elemento")
s3.add(6)
print(s3)

print("Removiendoun elemento")
s3.remove(3)
print(s3)

# Si se pone un valor que no existe no da la excepcion que con remove
print("Descartando un elemto, si no existe no da error")
s3.discard(5)
print(s3)

# pop() elimina un valor aleatorio
print("Elimina un elemento aleatorio, peligro!!")
sorteo = s3.pop()
print(sorteo)

# clear() vacía el set
print("Vaciar el set => s3.clear()")
s3.clear()
print(s3)

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
print(sorteo)
sorteo.pop()
print(sorteo)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
print(sorteo)
