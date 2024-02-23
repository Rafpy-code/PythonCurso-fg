# -*- coding: utf-8 -*-
import random


def seleccionar_palabra(lista):
    palabra_choice = random.choice(lista)
    # Quitar esta línea cuando funcione todo
    print(palabra_choice)
    return palabra_choice


def ocultar_palabra(palabra_visible):
    oculta = ['-' for letra in palabra_visible]
    return oculta


def lista_a_string(palabra_oculta):
    palabra_oculta = ''.join(palabra_usuario)
    return palabra_oculta


def pedir_letra():
    while True:
        letra = input("Por favor, ingresa una letra: ")
        # Verificar si la entrada es una única letra y es alfabética
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("\tPor favor, ingresa solo una letra.")


def comprobar_letra(letra_ingresada, intentos):
    if letra_ingresada in palabra_buscada:
        for index, letra in enumerate(palabra_buscada):
            if letra == letra_ingresada:
                palabra_usuario[index] = letra
    else:
        intentos -= 1
        if intentos == 0:
            print(f'\tHas perdido, la palabra era => {palabra_buscada}')
        else:
            print(f"\tFallo, te quedan => {intentos} vidas.")

    return intentos


def comprobar_ganador(x, y):
    if x == y:
        print(f'***** Has ganado, has descubierto la palabra => {x} *****')
        exit(1)


# Desarrollo del juego
lista_palabras = ['raton', 'burro', 'delfin', 'ardilla', 'castor']
vidas = 6
ganador = False
palabra_usuario = []
palabra_buscada = seleccionar_palabra(lista_palabras)
palabra_usuario = ocultar_palabra(palabra_buscada)

while vidas > 0 and not ganador:
    # imprimo la palabra oculta
    palabra = lista_a_string(palabra_usuario)
    print(palabra)

    # LLamo al método que comprueba las 2 palabras
    comprobar_ganador(palabra_buscada, palabra)

    # LLamo al método para que el usuario ingrese una letra
    letra_usuario = pedir_letra()

    # LLamo al método para comprobar que la letra ingresada está o no en la palabra buscada
    vidas = comprobar_letra(letra_usuario, vidas)
