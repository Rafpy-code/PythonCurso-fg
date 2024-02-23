from random import *


lista_numeros = [25, 67, 108, 12]


def lanzar_moneda():
    cara_cruz = ['Cara', 'Cruz']
    return choice(cara_cruz)


def probar_suerte(lanzar, lista):
    suerte = lanzar

    if suerte == 'Cara':
        lista = []
        print(f"{suerte}, La lista se autodestruirá")
        return lista
    else:
        print(f"{suerte}, La lista fue salvada")
        return lista


print(probar_suerte(lanzar_moneda(), lista_numeros))