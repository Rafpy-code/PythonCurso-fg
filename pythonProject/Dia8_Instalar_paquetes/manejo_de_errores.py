def pedir_numero():
    while True:
        try:
            numero = int(input("Ingresa un número: "))
        except ValueError:
            print("No has ingresado un número")
        else:
            print(f"Ingresaste el número {numero}")
            break
    print("Gracias")


pedir_numero()


def suma():
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    print(f"{n1} + {n2} = {n1 + n2}")


try:
    suma()
except TypeError:
    print("TypeError! string + integer")
except ValueError:
    print("No has ingresado un número")
else:
    print("Ejecución correcta")
finally:
    print("Adios desde finally")
