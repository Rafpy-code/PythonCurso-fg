


def tiene_3_cifras(numero):
    return numero in range(100, 1000)


print("resultado = tiene_3_cifras(59)")
resultado = tiene_3_cifras(59)
print(resultado)


def tiene_3_cifras_lista(lista):
    for n in lista:
        if n in range(100, 1000):
            return True
        else:
            pass
    return False


print()
lista = [23, 456, 18, 145]
print(lista)
print("resultado1 = tiene_3_cifras_lista(lista)")
resultado1 = tiene_3_cifras_lista(lista)
print(resultado1)


def tiene_3_cifras_lista_list(lista):
    tienen_3_cifras = []
    for n in lista:
        if n in range(100, 1000):
            tienen_3_cifras.append(n)
        else:
            pass
    return tienen_3_cifras


print()
lista = [23, 456, 18, -145]
print(lista)
resultado2 = tiene_3_cifras_lista_list(lista)
print("resultado2 = tiene_3_cifras_lista_list(lista)")
print(resultado2)


def todos_positivos(lista_n):
    for n in lista_n:
        if n < 0:
            return False
        else:
            pass
    return True


print()
lista_numeros = [456, 45, -34, 678, 12031]
print(lista_numeros)
resultado3 = todos_positivos(lista_numeros)
print("resultado3 = todos_positivos(lista_numeros)")
print(resultado3)


def suma_menores(lista_n):
    suma = 0
    for n in lista_n:
        if 0 < n < 1000:
            suma += n
        else:
            pass
    return suma


print()
lista_numeros = [456, 45, -34, 678, 12031]
suma_lista = suma_menores(lista_numeros)
print("suma_lista = suma_menores(lista_numeros)")
print(suma_lista)


def cantidad_pares(numeros):
    contador_pares = 0
    for n in numeros:
        if n % 2 == 0:
            contador_pares += 1
        else:
            pass
    return contador_pares


print()
lista_numeros = [456, 45, -34, 678, 12031]
print(lista_numeros)
hay_pares = cantidad_pares(lista_numeros)
print("hay_pares = cantidad_pares(lista_numeros)")
print(hay_pares)


def precio_mayor(lista_cafes):
    nombre_bebida = ''
    mas_caro = 0

    for bebida, precio in lista_cafes:
        if precio > mas_caro:
            mas_caro = precio
            nombre_bebida = bebida
        else:
            pass
    return nombre_bebida, mas_caro


print()
# Precio mayor de una lista
precios_bebidas = [('solo', 1.70), ('cafe_con_leche', 1.85), ('chocolate', 2.10)]
print(precios_bebidas)
print("Tuplas")
for tupla in precios_bebidas:
    print(tupla)
print("precio_mayor(precios_bebidas)")
print(precio_mayor(precios_bebidas))

bebida, precio = precio_mayor(precios_bebidas)
print(f'La bebida más cara es {bebida} y cuesta € {precio}')
