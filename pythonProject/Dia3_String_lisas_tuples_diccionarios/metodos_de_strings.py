linea_de_texto = "Esta es una línea de texto para la práctica"

resultado = linea_de_texto.upper()
print(resultado)

resultado = linea_de_texto.split()
print(resultado)

resultado = linea_de_texto.split("a")
print(resultado)

resultado = "".join(linea_de_texto)
print(resultado)

a = "Estoy"
b = "aprendiendo"
c = "Python"
resultado = " ".join([a, b, c])
print(resultado)

resultado = resultado.find("Py")
print(resultado)

resultado = linea_de_texto.find("to")
print(resultado)

resultado = linea_de_texto.replace("e", "E")
print(resultado)
