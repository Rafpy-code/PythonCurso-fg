import pygame
import random
import math
from pygame import mixer

# Inicializar el juego
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800,600))

# Titulo de la pantalla
pygame.display.set_caption("Castor-Ardilla Invaders")
# Icono de la pantalla "autor: <a target="_blank" href="https://icons8.com/icon/21712/space-fighter">Space Fighter</a> icono de <a target="_blank" href="https://icons8.com">Icons8</a>"
icono = pygame.image.load('D:\PROGRAMACION\PythonCurso-fg\pythonProject\Dia10_pygame\imagenes\icons8-castor-40.png')
pygame.display.set_icon(icono)
# Fondo de pantalla
fondo = pygame.image.load('D:\PROGRAMACION\PythonCurso-fg\pythonProject\Dia10_pygame\imagenes/fondo_verde.jpg')

# Agregar música
mixer.music.load('D:\PROGRAMACION\PythonCurso-fg\pythonProject\Dia10_pygame\sonidos\MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Variables del jugador
jugador_img = pygame.image.load('D:\PROGRAMACION\PythonCurso-fg\pythonProject\Dia10_pygame\imagenes\icons8-castor-80.png')
jugador_x = 360
jugador_y = 510
jugador_x_cambio = 0
#jugador_y_cambio = 0

# Variables de los enemigos
enemigo_img = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for i in range(cantidad_enemigos):
    enemigo_img.append(pygame.image.load('D:\PROGRAMACION\PythonCurso-fg\pythonProject\Dia10_pygame\imagenes\icons8-ardilla-64.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(0, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

# Variables de la bala
# Ready - no se ve la bala
bala_visible = False
# Fire - la bala se mueve
bala_img = pygame.image.load('D:\PROGRAMACION\PythonCurso-fg\pythonProject\Dia10_pygame\imagenes\icons8-nuez-48.png')
bala_x = 0
bala_y = 480
bala_x_cambio = 0
bala_y_cambio = 3

# Puntaje
puntaje = 0
fuente = pygame.font.Font('D:\PROGRAMACION\PythonCurso-fg\pythonProject\Dia10_pygame/fuentes\PlaywriteMX-VariableFont_wght.ttf', 32)
texto_x = 10
texto_y = 10

# texto final de juego
fuente_final = pygame.font.Font('D:\PROGRAMACION\PythonCurso-fg\pythonProject\Dia10_pygame/fuentes\PlaywriteMX-VariableFont_wght.ttf', 40)

# =========== Funciones ===========
# Posicion del jugador
def jugador(x, y):
    pantalla.blit(jugador_img, (x, y))

# Posicion enemigos
def enemigo(x, y, enemigo):
    pantalla.blit(enemigo_img[enemigo], (x, y))

# Disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(bala_img, (x + 16, y + 10))

# Detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distancia < 27:
        return True
    else:
        return False

def texto_final():
    mi_fuente_final = fuente_final.render("Haz sido capturado... FIN", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))

# funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # Fondo de pantalla
    # pantalla.fill((205, 144, 228))       
    pantalla.blit(fondo, (0, 0))
    
    # Iterar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            se_ejecuta = False
        
        # Evento de presionar teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if event.key == pygame.K_UP:
                jugador_y_cambio = -0.3
            if event.key == pygame.K_DOWN:
                jugador_y_cambio = 0.3
            if event.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('D:\PROGRAMACION\PythonCurso-fg\pythonProject\Dia10_pygame\sonidos\disparo.mp3')
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)
        
        # Evento de soltar teclas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
            #if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                #jugador_y_cambio = 0

    # Modificar ubicaciones de jugador
    jugador_x += jugador_x_cambio
    #jugador_y += jugador_y_cambio
    
    # Evitar que el jugador se salga de la pantalla
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 720:
        jugador_x = 720       
    # if jugador_y <= 0:
    #     jugador_y = 0       
    # elif jugador_y >= 520:
    #     jugador_y = 520

    # Modificar ubicaciones del enemigo
    for i in range(cantidad_enemigos):
        
        # fin del juego
        if enemigo_y[i] > 510:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        # Movimiento
        enemigo_x[i] += enemigo_x_cambio[i]
        #enemigo_y[i] += enemigo_y_cambio[i]
        
        # Evitar que el enemigo se salga de la pantalla
        if enemigo_x[i] <= 0:
            enemigo_x_cambio[i] = 0.3
            enemigo_y[i] += enemigo_y_cambio[i]
        elif enemigo_x[i] >= 736:
            enemigo_x_cambio[i] = -0.3
            enemigo_y[i] += enemigo_y_cambio[i]
        
        # Colision
        colision = hay_colision(enemigo_x[i], enemigo_y[i], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('D:\PROGRAMACION\PythonCurso-fg\pythonProject\Dia10_pygame\sonidos\Golpe.mp3')
            sonido_colision.play()
            bala_visible = False
            bala_y = 480
            puntaje += 1
            #print(puntaje)
            enemigo_x[i] = random.randint(0, 736)
            enemigo_y[i] = random.randint(0, 200)
            
        # Llamar a la funcion enemigo
        enemigo(enemigo_x[i], enemigo_y[i], i)

    # Variables para el cambio de ubicacion de la bala
    if bala_y <= 0:
        bala_visible = False
        bala_y = 480 
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # Llamar a la funcion jugador
    jugador(jugador_x, jugador_y)

    # Mostrar puntaje
    mostrar_puntaje(texto_x, texto_y)

    # Actualizar la pantalla
    pygame.display.update()