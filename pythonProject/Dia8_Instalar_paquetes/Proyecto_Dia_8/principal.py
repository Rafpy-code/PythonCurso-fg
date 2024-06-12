import numeros


def preguntar():
    print("Bienvenido a Farmacia Python")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmética")
        try:
            mi_rubro = input("\tElija su rubro: ").upper()
            ["P", "F", "C"].index(mi_rubro)  # Devuelve un error si la letra no está en la lista
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    numeros.decorador(mi_rubro)  # Llama al decorador importado de numeros.py


def inicio():
    continuar = False
    while not continuar:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                continuar = True


inicio()
