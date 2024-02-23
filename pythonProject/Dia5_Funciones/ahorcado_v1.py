# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:41:27 2022
@author: Ramón
Juego del ahorcado
"""
import time
import random

# Declaro las variables.
interruptor = True

print('JUEGO DEL AHORCADO')
jugador = (input('Ingresa tu nombre: ')).upper()
print(f'Hola, {jugador}')
time.sleep(1)
print('Empecemos!!!')

# Declaro la lista de palabras a adivinar.
palabras = ['perro', 'gallina', 'gato', 'raton',
            'pato', 'conejo', 'caballo', 'burro',
            'canguro', 'delfin', 'tortuga']


# Creo una función para sacar una palabra aleatoria.
def escogerPalabra():
    return random.choice(palabras)


# print(escogerPalabra())

palabra = escogerPalabra()
print(palabra)
tuPalabra = ''
intentos = 5

while intentos > 0:
    errores = 0
    for letra in palabra:
        if letra in tuPalabra:
            print(letra, end='')
        else:
            print('-', end='')
            errores = +1
            # print (errores,end='')
    if errores == 0:
        print('\nPalabra encontrada!!!')
        break
    letra = input('\tIntroduce una letra: ')
    tuPalabra += letra

    if letra not in palabra:
        intentos -= 1
        print(f'Intentos => {intentos}')
    if intentos == 0:
        print(f'No lo has logrado, la palabra era: {palabra}')
else:
    print('Gracias por jugar.')
