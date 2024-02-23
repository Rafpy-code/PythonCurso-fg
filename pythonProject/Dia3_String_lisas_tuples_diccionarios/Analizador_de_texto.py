texto = input("Ingresa un texto a elección: ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ".lower()))
letras.append(input("Ingresa la segunda letra: ".lower()))
letras.append(input("Ingresa la tercera letra: ".lower()))

print()
print("CANTIDAD DE LETRAS => texto.count(letras[0])")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print()
print("CANTIDAD DE PALABRAS => palabras = texto.split()")
palabras = texto.split()
print(palabras)
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print()
print("LETRAS DE INICIO => texto[0] Y DE FIN => texto[-1]")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print()
print("TEXTO INVERTIDO => palabras.reverse()")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al revés va a decir: '{texto_invertido}'")

print()
print("BUSCANDO LA PALABRA PYTHON EN EL TEXTO INGRESADO => 'python' in texto")
buscar_python = 'python' in texto
dic = {True: "sí", False: "no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")
