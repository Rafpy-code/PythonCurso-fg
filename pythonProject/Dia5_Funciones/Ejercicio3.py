"""
Escribe una función que requiera una cantidad indefinida de argumentos.
Lo que hará esta función es devolver True si en algún momento se ha ingresado al
numero cero repetido dos veces consecutivas. Por ejemplo:
(5,6,1,0,0,9,3,5) >>>
True
(6,0,5,1,0,3,0,1) >>>
False
"""


def doble_cero(*args):
    print("Ha ingresado dos ceros '0' '0' seguidos?")
    contador = 0
    ceros_seguidos = []
    print(args)
    print(f"Has {len(args)} números")
    if contador + 1 == len(args):
        return False
    for numero in args:
        if (args[contador] == 0) and (args[contador + 1] == 0):
            ceros_seguidos.append(args[contador])
            ceros_seguidos.append(args[contador+1])
            print(ceros_seguidos)
            return True
        else:
            contador += 1
    return False


print(doble_cero(9, 8, 5, 0, 8, 5, 1, 0, 0))
