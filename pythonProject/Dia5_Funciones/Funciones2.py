lista_numeros = [2, 56, 23, 89, 56, 1, 23]


def reducir_lista(lista):
    unicos = set(lista)
    unicos = list(unicos)
    unicos.pop()
    return unicos


def promedio(lista):
    avg = sum(lista) / len(lista)
    return avg

print(reducir_lista(lista_numeros))
print(promedio(reducir_lista(lista_numeros)))
