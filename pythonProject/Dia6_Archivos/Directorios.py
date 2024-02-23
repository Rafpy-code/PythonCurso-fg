import os
from pathlib import Path

# Objeto Path


ruta0 = os.getcwd()
print(ruta0)

# Para leer archivos que están en otra ubicación
ruta = os.chdir('D:\\PROGRAMACION\\PythonCursoFedericoGaray\\pythonProject\\Dia6_Archivos\\ruta_archivos')
print(ruta)  # Imprime none
archivo = open('nueva_ruta.txt')

print(archivo.read())

# Para crear nuevos directorios
ruta0 = os.makedirs('D:\\PROGRAMACION\\PythonCursoFedericoGaray\\pythonProject\\Dia6_Archivos\\carpeta_a_borrar')

# Devuelve el nombre del archivo
ruta1 = 'D:\\PROGRAMACION\\PythonCursoFedericoGaray\\pythonProject\\Dia6_Archivos\\archivo1.txt'
elemento0 = os.path.basename(ruta1)
print(elemento0)

# Devuelve el directorio en donde se aloja el archivo
elemento1 = os.path.dirname(ruta1)
print(elemento1)

# Devuelve el directorio y el nombre del archivo en una tupla
elemento2 = os.path.split(ruta1)
print(elemento2)

# Para eliminar directorios
mi_ruta = os.rmdir('D:\\PROGRAMACION\\PythonCursoFedericoGaray\\pythonProject\\Dia6_Archivos\\carpeta_a_borrar')
print(mi_ruta)

# Con el objeto Path: para que cualquier sistema operativo pueda leer la ruta
carpeta = Path('D:/PROGRAMACION/PythonCursoFedericoGaray/pythonProject/Dia6_Archivos/ruta_archivos')
# Dejar espacios entre la /
archivo1 = carpeta / 'nueva_ruta.txt'
mi_archivo = open(archivo1)

carpeta1 = Path('Dia6_Archivos/ruta_archivos') / 'nueva_ruta.txt'

mi_archivo = open(carpeta1)
print(mi_archivo.read())
