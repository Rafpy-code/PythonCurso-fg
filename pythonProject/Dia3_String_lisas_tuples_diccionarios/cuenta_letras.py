frase = input("Ingresa tus palabras o frases o textos. ").lower()
letras = [input("Ingresa la primera letra a buscar: ").lower(),
          input("Ingresa la segunda letra a buscar: ").lower(),
          input("Ingresa la tercera letra a buscar: ").lower()]

contador_palabras = frase.count(" ")
frase_lista = list(frase)
contador_palabras1 = frase.split()
contador_letra0 = frase.count(letras[0])
contador_letra1 = frase.count(letras[1])
contador_letra2 = frase.count(letras[2])
primera_letra = frase_lista[0]
ultima_letra = frase_lista[-1]
palaba_buscada = "Python"
print("\t^^^RESULTADOS^^^")
print(frase)
print(f"La frase tiene {contador_palabras} palabras")
print(f"La frase tiene {len(contador_palabras1)} palabras")
print(f"La letra {letras[0]} se encuentra {contador_letra0} veces")
print(f"La letra {letras[1]} se encuentra {contador_letra1} veces")
print(f"La letra {letras[2]} se encuentra {contador_letra2} veces")
print(f"La frase empieza con la letra '{primera_letra}'")
print(f"La frase termina con la letra '{ultima_letra}'")
print(f"¿La palabra 'Phyton' se encuentra en la frase? -> {palaba_buscada.lower() in frase_lista}")
contador_palabras1.reverse()
palabras_invertidas = " ".join(contador_palabras1)
print(f"La frase invertida:\n{palabras_invertidas}")
