"""
Escribe una función (puedes ponerle cualquier nombre quequieras)
que reciba cualquier palabra como parámetro, y quedevuelva todas sus letras únicas
(sin repetir) pero en ordenalfabético.
Por ejemplo si al invocar esta función pasamos la palabra"entretenido",
debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
def letras_unicas(palabra):
    set_letras = set()
    for letra in palabra:
        set_letras.add(letra)
    unicas = list(set_letras)
    unicas.sort()
    return unicas
"""


def letras_unicas(palabra):
    set_letras = set(palabra)
    unicas = list(set_letras)
    unicas.sort()
    return unicas


print(letras_unicas('ramomocittooncito'))


def l_unicas(word):
    set_unicas = set(w for w in word)
    list_unicas = list(set_unicas)
    list_unicas.sort()
    return list_unicas


print(l_unicas("psdfjhdpython"))


# Crear un conjunto
mi_conjunto = {4, 2, 7, 1, 5}

# Ordenar el conjunto y convertirlo a una lista
lista_ordenada = sorted(mi_conjunto)

# Imprimir la lista ordenada
print(lista_ordenada)


# Crear un conjunto
mi_conjunto = {41, 72, 17, 1, 95}

# Convertir el conjunto a una lista y ordenarla
lista_ordenada = sorted(list(mi_conjunto))

# Imprimir la lista ordenada
print(lista_ordenada)

