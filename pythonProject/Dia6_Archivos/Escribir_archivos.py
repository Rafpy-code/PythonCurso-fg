archivo = open('prueba1.txt', 'w')

lista = ['casa', 'del', 'árbol']

for palabra in lista:
    archivo.writelines(f"{palabra}\n")

archivo.close()

archivo = open('prueba1.txt', 'a')

# Se puede hacer """ comillas, para varias líneas """
archivo.write('Esta es una línea con append\n')

archivo.close()
