def multiplicar(num1, num2):
    total = num1 * num2
    print(total)
    return total


resultado = multiplicar(4, 5)


# No se está cpntrolando la entrada de datos
# resultado = multiplicar('4', '5')

def potencia(num1, num2):
    return num1 ** num2


def usd_a_eur(valor):
    return valor * 0.90


dolares = usd_a_eur(55)
print(dolares)


def invertir_palabra(palabra):
    p = list(palabra.upper())
    p.reverse()
    return ''.join(p)


palabra = invertir_palabra('python')
print(palabra)
