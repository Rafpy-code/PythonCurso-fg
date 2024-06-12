def mayusculas(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())


# se puede asignar una función a una variable
mi_funcion = mayusculas
mi_funcion('python a mayúsculas')


# Una función recibe una función y retorna la función
def una_funcion(funcion):
    return funcion


una_funcion(minusculas('PYTHON A MINÚSCULAS'))


def mayuscula_minuscula(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula


cambiar_texto = mayuscula_minuscula('may')
cambiar_texto('todo a mayúsculas')


def decorar_saludo(la_funcion):
    def hola_adios(palabra):
        print('Hola')
        la_funcion(palabra)
        print('Adios')

    return hola_adios


# Usando decoradores
@decorar_saludo
def mayusc(texto):
    print(texto.upper())


@decorar_saludo
def minusc(texto):
    print(texto.lower())


mayusc('hey')
minusc('YOU')

# Usando la funcición decorar saludo
mayuscula_decorada = decorar_saludo(mayusculas)
mayuscula_decorada('mayuscula_decorada = decorar_saludo(mayusculas)')

minuscula_decorada = decorar_saludo(minusculas)
minuscula_decorada('AHORA TODO A MINUSCULA_DECORADA')
