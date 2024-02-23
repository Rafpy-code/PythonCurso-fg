texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
# del 2 al 6 sin incluir el último
fragmento = texto[2:6]
print(fragmento)

# inicia en 2 hasta el final
fragmento = texto[2:]
print(fragmento)

# inicia en 0 hasta el 6 sin incluir el último
fragmento = texto[:6]
print(fragmento)

# el tercer número indica que saltará en este caso de 2 en 2 caracteres
fragmento = texto[2:6:2]
print(fragmento)

fragmento = texto[::2]
print(fragmento)

# empieza desde el final
fragmento = texto[::-1]
print(fragmento)
