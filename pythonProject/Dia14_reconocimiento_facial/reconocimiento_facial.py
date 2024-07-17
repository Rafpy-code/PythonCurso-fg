'''
# Poner 2 fotos tuyas, 1 de frente foto_A.jpg y 1 un poco de perfil foto_B.jpg, para hacer las pruebas
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

#from cv2 import cv2 #Así no me funciona la importación
import cv2
import face_recognition as fr

# Cargar imágenes
foto_control = fr.load_image_file("pythonProject/Dia14_reconocimiento_facial/foto_B.jpg")
foto_prueba = fr.load_image_file("pythonProject/Dia14_reconocimiento_facial/foto_C.jpg")

# Pasar imágenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

# Mostrar rectangulo en la cara
cv2.rectangle(foto_control, 
                             (lugar_cara_A[3], lugar_cara_A[0]), 
                             (lugar_cara_A[1], lugar_cara_A[2]), 
                             (255, 0, 255), 2)

cv2.rectangle(foto_prueba, 
                             (lugar_cara_B[3], lugar_cara_B[0]), 
                             (lugar_cara_B[1], lugar_cara_B[2]), 
                             (255, 0, 255), 2)

# Realizar comparación, 3er parámetro es la tolerancia ej: 03 si se baja hay menor posibilidad de True
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B)
#print(resultado)

# Medida de distancia
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)
#print(distancia)

# Mostrar resultado
cv2.putText(foto_prueba, 
            f"{resultado}{distancia.round(2)}", 
            (5, 40), 
            cv2.FONT_HERSHEY_COMPLEX, 
            1, 
            (0, 255, 0), 
            2)

# Mostrar imágenes
cv2.imshow("Foto Control", foto_control)
cv2.imshow("Foto Prueba", foto_prueba)

# Mantener el programa abierto
cv2.waitKey(0)

