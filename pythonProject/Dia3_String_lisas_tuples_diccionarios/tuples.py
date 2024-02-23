mi_tuple = (3, 6, 1, 4)
print(mi_tuple)
print(type(mi_tuple))

print("tuples dentro de tuples")
mi_tuple = (3, 6, (1, 3, 8), 4, 3)
print(mi_tuple)
print(f"Tipo de mi_tuple => {type(mi_tuple)}")
print(f"mi_tuple.count(3) cuenta las veces que se repite el 3 en la tupla, no en las subtuplas")
print(mi_tuple.count(3))
print(f"mi_tple[2] => {mi_tuple[2]}")

mi_tuple = list(mi_tuple)
print(mi_tuple)
print(type(mi_tuple))

# Debe tener la misma cantidad de elementos que las variables.
print("Asignando valores de un tuple a variables")
mi_tuple = (3, 6, 1, 4)
print(mi_tuple)
print("a, b, c, d = mi_tuple")
a, b, c, d = mi_tuple
print(f"a={a}, b={b}, c={c}, d={d}")

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)
print(mi_lista)
print("mi_tupla.index(3)")
print(mi_tupla.index(3))

mi_tupla = (1, 2, 3, 4)
a, b, c, d = mi_tupla
print(a, b, c, d)
