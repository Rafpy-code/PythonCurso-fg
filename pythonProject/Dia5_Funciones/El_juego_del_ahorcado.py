import time
import random

print("\t***** JUEGO DEL AHORCADO *****")

# Declaro la lista de palabras a adivinar.
palabras = ['perro', 'gallina', 'gato', 'raton',
            'pato', 'conejo', 'caballo', 'burro',
            'canguro', 'delfin', 'tortuga']

jugador = input('Ingresa tu nombre: ')
jugador = jugador.capitalize()
print(f'Hola, {jugador}')
time.sleep(1)
print('Empecemos!!!')


# Creo una función para sacar una palabra aleatoria.
def escogerPalabra(lista):
    return random.choice(lista)


# print(escogerPalabra())
letras = "abcdefghijklmnñopqrstuvwxyzáéíóú"
letras_erroneas = []
vidas = 6


def jugar(palabra, vidas):
    tu_palabra = ''
    while vidas > 0:
        errores = False

        for letra in palabra:
            if letra in tu_palabra:
                print(letra, end='')
            else:
                print('-', end='')
                errores = True
                # print (errores,end='')
        if not errores:
            print('\n\tPalabra encontrada!!!')
            break

        letra = input('\tIntroduce una letra: ')
        tu_palabra += letra
        # print(f'Letras introducidas {tu_palabra}')

        if letra not in palabra:
            letras_erroneas.append(letra)
            vidas -= 1
            if vidas == 0:
                print(f'\tNo lo has logrado. La palabra buscada era {palabra}')
            else:
                print(f'\tCuidado, te quedan {vidas} vidas.')
                print(f'\tHas fallado {letras_erroneas}')
    print('Gracias por jugar.')


palabra = escogerPalabra(palabras)
print(palabra)
jugar(palabra, vidas)
