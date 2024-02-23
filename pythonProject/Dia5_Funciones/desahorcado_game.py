import random


def obtener_palabra():
    palabras = ['perro', 'gato', 'elefante', 'leon', 'jirafa', 'vaca', 'raton', 'murcielago', 'ballena', 'delfin',
                'mono', 'oso', 'tigre', 'caballo', 'cerdo', 'conejo', 'koala', 'hipopotamo', 'ardilla', 'canguro']
    return random.choice(palabras)


def inicializar_juego():
    palabra_secreta = obtener_palabra()
    print(palabra_secreta)
    palabra_oculta = ["_" for _ in palabra_secreta]
    vidas = 6
    letras_intentadas = set()
    return palabra_secreta, palabra_oculta, vidas, letras_intentadas


def mostrar_tablero(palabra_oculta, vidas, letras_intentadas):
    print("\nVidas restantes: {} \tLetras intentadas => {}".format(vidas, (", ".join(letras_intentadas))))
    print("Palabra actual: " + " ".join(palabra_oculta))


def ingresar_letra():
    while True:
        letra = input("Ingresa una letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("\tPor favor, ingresa una letra.")


def actualizar_palabra_oculta(palabra_secreta, palabra_oculta, letra):
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_oculta[i] = letra


def jugar_ahorcado():
    print('*' * 50)
    print("\tBienvenido al juego del desahorcado_game!")

    palabra_secreta, palabra_oculta, vidas, letras_intentadas = inicializar_juego()

    while vidas > 0 and "_" in palabra_oculta:
        mostrar_tablero(palabra_oculta, vidas, letras_intentadas)

        letra = ingresar_letra()

        if letra in letras_intentadas:
            print("\tLetra ya introducida, prueba con otra letra!")
            continue

        letras_intentadas.add(letra)

        if letra in palabra_secreta:
            actualizar_palabra_oculta(palabra_secreta, palabra_oculta, letra)
            print("\t¡Correcto!")
        else:
            vidas -= 1
            if vidas == 0:
                print("\tTe has quedado sin vidas :(")
            else:
                print("\tIncorrecto. Pierdes una vida.")

    if "_" not in palabra_oculta:
        print("\t¡Felicidades! Has adivinado la palabra: {}".format("".join(palabra_oculta)))
    else:
        print("\tHas perdido. La palabra era: {}".format(palabra_secreta))


if __name__ == "__main__":
    jugar_ahorcado()
