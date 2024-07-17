'''
# Poner tu foto en la carpeta de empleados para que se reconozca
requirements.txt
instalar visual studio comunity y elegir desarrollo de escritorio C++ durante la instalación
cmake
dlib    # Si da problemas la instalación de dlib: 
        #git clone https://github.com/davisking/dlib.git
        #cd dlib
        #python setup.py install
face-recognition
numpy
opencv-python
'''

import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# crear base de datos
ruta = 'pythonProject/Dia14_reconocimiento_facial/Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])
print(nombres_empleados)

# codificar imagenes
def codificar(imagenes):
    # crear una lista nueva
    lista_codificada = []

    # pasar todas las imagenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # codificar
        codificado = fr.face_encodings(imagen)[0]

        # agregar a la lista
        lista_codificada.append(codificado)

    # devolver lista codificada
    return lista_codificada


# registrar los ingresos
def registrar_ingresos(persona):
    f = open('pythonProject/Dia14_reconocimiento_facial/Registros_csv/registro.csv', 'r+')
    lista_datos = f.readlines()
    nombres_registro = []

    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%d-%m-%Y %H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')


lista_empleados_codificada = codificar(mis_imagenes)

# tomar una imagen de camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# leer imagen de la camara
exito, imagen = captura.read()

if not exito:
    print("No se ha podido tomar la captura")
else:
    # reconocer cara en captura
    cara_captura = fr.face_locations(imagen)
    
    # codificar cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # buscar coincidencias
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        print(distancias)

        indice_coincidencia = numpy.argmin(distancias)

        # mostrar coincidencias si las hay
        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ninguno de nuestros empleados")
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.rectangle(imagen, (x1, y2 + 20), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, 'Peligro!', (x1 + 6, y2 + 18), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 2555, 255), 2)
           
            # mostrar la imagen obtenida
            cv2.imshow('Imagen web', imagen)

            # mantener ventana abierta
            cv2.waitKey(0)
        else:
            # buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]
            print(f'Nombre: {nombre}, buena jornada de trabajo.')
            solo_nombre = nombre.split(' ')
            
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.rectangle(imagen, (x1, y2 + 20), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, solo_nombre[0] , (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 2555, 255), 2)
            cv2.putText(imagen, 'Bienvenido', (x1 + 6, y2 + 18), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 2555, 255), 2)

            registrar_ingresos(nombre)
            
            # mostrar la imagen obtenida
            cv2.imshow('Imagen web', imagen)

            # mantener ventana abierta
            cv2.waitKey(0)
