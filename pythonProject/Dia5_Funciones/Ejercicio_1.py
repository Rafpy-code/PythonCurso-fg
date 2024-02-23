"""
Crea una función llamada devolver_distintos() que reciba 3 integers
como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a
devolver el número de valor intermedio .
"""


def devolver_distintos(a, b, c):
    lista = [a, b, c]
    print(lista)
    suma = 0

    for n in lista:
        suma += n
    print(f"La suma da {suma}")

    if suma > 15:
        return f"El número mayor es {max(lista)}"
    elif suma < 10:
        return f"El número menor es {min(lista)}"
    else:
        #lista.remove(max(lista))
        #lista.remove(min(lista))
        lista.sort()
        return f"El número intermedio es {lista[1]}"


print(devolver_distintos(1, 4, 3))
