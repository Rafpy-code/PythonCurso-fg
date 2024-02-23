def suma(**kwargs):
    print(type(kwargs))
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total


print(f"la suma da: {suma(x=3, y=7, z=6)}")


def mix(num1, num2, *args, **kwargs):
    print("\ndef mix(num1, num2, *args, **kwargs):")
    print(f"El primer valor num1 es: {num1}")
    print(f"El segundo valor num2 es: {num2}")

    for arg in args:
        print(f"Arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


mix(15, 73, 0.2, 45, 87, 5, 25, a=1, b=243, c=698)

args = [16, 34, -13, -45]
kwargs = {'1': 'Nombre', '2': 'Apellido', '3': 'DNI'}
mix(50, 2023, *args, **kwargs)


def cantidad_atributos(**kwargs):
    contador = 0
    for clave, valor in kwargs.items():
        contador += 1
    return f"Hay {contador} argumentos"


print(cantidad_atributos(R="Ramón", a=13, b=67, c='F'))


def lista_atributos(**kwargs):
    lista_kwargs = []
    for clave, valor in kwargs.items():
        lista_kwargs.append(valor)
    return lista_kwargs


print(lista_atributos(R="Ramón", a=13, b=67, c='F'))


def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


describir_persona("María", color_ojos="azules", color_pelo="rubio")
