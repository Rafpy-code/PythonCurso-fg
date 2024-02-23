def suma_cuadrados(*args):
    total = 0
    for n in args:
        total += n ** 2
    return total


print(suma_cuadrados(1, 2, 3))


def suma_absolutos(*args):
    total = 0
    for n in args:
        total += abs(n)
    return total


print(suma_absolutos(-15, 15, -15))


def numeros_persona(tu_nombre, *args):
    nombre = tu_nombre
    suma_numeros = 0
    for n in args:
        suma_numeros += n
    return f"{nombre}, la suma de tus números es {suma_numeros}"


print(numeros_persona('Ramón', 23, 56, 87, 14))
