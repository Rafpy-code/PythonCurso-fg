def sumar(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(sumar(4, 6, 56, 23, 4, 678, 234, 1))


# Función ya definida sum()
def suma(*args):
    return sum(args)


print(suma(4, 6, 56, 23, 4, 678, 234, 1))

lista = [4, 6, 56, 23, 4, 678, 234, 1]
print(sum(lista))

print(sum([4, 6, 56, 23, 4, 678, 234, 1]))
