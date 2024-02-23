texto = "Este es un texto de prueba"
# Si coincide un espacio no se verá el resultado y negativo empieza desde el final
resultado = texto[-8]
print(resultado)
resultado = texto.index("x")
print(resultado)
resultado = texto.index("e", 6)
print(resultado)
resultado = texto.index("t", 5, 13)
print(resultado)

# rindex("b") busca de derecha a izquierda
resultado = texto.rindex("b")
print(resultado)
resultado = texto.rindex("texto")
print(resultado)
