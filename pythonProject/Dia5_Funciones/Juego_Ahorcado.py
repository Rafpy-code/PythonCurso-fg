import time
import random

print('\tJUEGO DEL AHORCADO')

jugador = input('Ingresa tu nombre: ')
jugador = jugador.capitalize()
print(f'Hola, {jugador}')
time.sleep(1)
print('Empecemos!!!\n')

# Declaro la lista de palabras a adivinar.
palabras = ['perro', 'gallina', 'gato', 'raton',
            'pato', 'conejo', 'caballo', 'burro',
            'canguro', 'delfin', 'tortuga']

tuPalabra = ''
intentos = 5
errores = 0


# Creo una función para sacar una palabra aleatoria.
def escogerPalabra(palabras):
    return random.choice(palabras)


palabra = escogerPalabra(palabras)
print(palabra)
while intentos > 0:
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
        print(f'Cuidado, te quedan {intentos} vidas.')
    if intentos == 0:
        print('No lo has logrado')
else:
    print('Gracias por jugar.')
