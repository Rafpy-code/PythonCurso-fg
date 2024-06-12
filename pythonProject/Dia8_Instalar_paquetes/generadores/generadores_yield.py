def mi_funcion():
    lista = []
    for n in range(1, 5):
        lista.append(n)
    return lista


def mi_generador():
    for n in range(1, 5):
        yield n * 10  # yield (producir) en lugar de return


print(mi_funcion())  # [1, 2, 3, 4]
print(mi_generador())  # <generator object mi_generador at 0x00000197F95936B0>

generado = mi_generador()  # por cada next() va generando
print(next(generado))
print(next(generado))
print(next(generado))
print(next(generado))
#  print(next(generado))  StopIteration

print(generado)  # <generator object mi_generador at 0x000001BB576436B0>
