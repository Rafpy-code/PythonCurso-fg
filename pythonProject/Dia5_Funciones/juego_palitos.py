# Lista de palitos
from random import shuffle

palitos = ['-', '--', '---', '----']


# Función para mezclar los palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# Función para escoger los palitos
def elegir():
    elegido = ''
    while elegido not in ['1', '2', '3', '4']:
        elegido = input("Elija un número del 1 al 4: ")
    return int(elegido)


# Funcion para realizar el juego
def jugar(lista, eleccion):
    if (lista[eleccion - 1]) == '-':
        print(f"Has perdido, te ha tocado '{lista[eleccion - 1]}' a pagar la apuesta!")
    else:
        print(f"Te has salvado de pagar la apuesta, te ha tocado '{lista[eleccion - 1]}'")


# A jugar
lista_palitos = mezclar(palitos)
probar_suerte = elegir()
jugar(lista_palitos, probar_suerte)
