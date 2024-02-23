mi_archivo = open('prueba.txt')
# Imprime los datos relativos al archivo, no imprime el contenido
print(mi_archivo)
mi_archivo.close()
print('-----------------------------------------')

mi_archivo = open('prueba.txt')
# Lee todo el archivo
print(mi_archivo.read())
mi_archivo.close()
print('-----------------------------------------')

mi_archivo = open('prueba.txt')
# Lee una línea
una_linea = mi_archivo.readline()
print(una_linea)
mi_archivo.close()
print('-----------------------------------------')

mi_archivo = open('prueba.txt')
# Lee todas las líneas y las mete en una lista
todas = mi_archivo.readlines()
print(todas)
mi_archivo.close()
print('-----------------------------------------')

print("Archivo leido con for:")
mi_archivo = open('prueba.txt')
for linea in mi_archivo:
    print(linea)
mi_archivo.close()
