lista_palabras = ["La", "legibilidad", "cuenta."]
print(lista_palabras)

d = " ".join(lista_palabras)
print(d)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase = frase.replace("difícil", "fácil")
frase = frase.replace("mala", "buena")
print(frase)

print("Repetición" * 15)

frase = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""
print("¿Está la palabra 'agua' en la frase?")
print("agua" not in frase)

palabra = "electroencefalografista"
print(f"¿Cuántos caracteres tiene la palabra {palabra}?")
print(len(palabra))
