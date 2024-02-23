from random import randint

vidas = 8
intentos = 1
adivina = randint(1, 100)
print(adivina)

nombre = input("Dime tu nombre: ")
print(f"Bueno {nombre}, he pensado un número entre 1 y 100\nTienes 8 intentos para adivinar")

while vidas > 0:
    numero = int(input("¿Cuál es tu numero de la suerte? "))
    if (numero < 0) or (numero > 100):
        vidas -= 1
        intentos += 1
        print("Ha elegido un número que no está permitido.")
    elif numero < adivina:
        vidas -= 1
        intentos += 1
        print("Ha elegido un número menor al número secreto.")
    elif numero > adivina:
        vidas -= 1
        intentos += 1
        print("Ha elegido un número mayor al número secreto.")
    elif numero == adivina:
        print(f"\tHas acertado, con {intentos} intentos")
        vidas = -1
if vidas == 0:
    print("\tTe has quedado sin intentos")
