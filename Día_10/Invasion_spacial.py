import pygame
import random
import math
from pygame import mixer
import io


# INICIALIZAR PYGAME
pygame.init()

# CREAR LA PANTALLA
pantalla = pygame.display.set_mode((800, 600))

# TTF A BYTES
def fuente_bytes(fuente):
    #abre el archivo ttf en modo lectura binaria
    with open(fuente, 'rb')as f:
        #lee todos los bytes del archivo y los almacena en una variable
        ttf_bytes = f.read()
    #crea un obj BytesIO a partir de los bites del archivo
    return io.BytesIO(ttf_bytes)



# TITULO E ICONO
pygame.display.set_caption("Spacial Invasion")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load('7756635.png')

# AGREGANDO SONIDOS
mixer.music.load('MusicaFondo.mp3')
mixer.music.play(-1)

# VARIABLES DEL JUGADOR
img_jugador = pygame.image.load('protagonista.png')
jugador_x = 360
jugador_y = 520
jugador_x_cambio = 0

# VARIABLES DEL ENEMIGO
img_enemigo = pygame.image.load('enemigo.png')
enemigo_x = random.randint(0, 734)
enemigo_y = random.randint(34, 250)
enemigo_x_cambio = 0.75
enemigo_y_cambio = 50


class Enemigo():
    img_enemigo = pygame.image.load('enemigo.png')

    def __init__(self):
        self.enemigo_x = random.randint(0, 734)
        self.enemigo_y = random.randint(34, 250)
        self.enemigo_x_cambio = 0.75
        self.enemigo_y_cambio = 50

    def enemigo(self):
        pantalla.blit(img_enemigo, (self.enemigo_x, self.enemigo_y))


# VARIABLES DE LA BALA
img_bala = pygame.image.load('misil.png')
bala_x = 0
bala_y = 520
bala_y_cambio = 3
bala_visible = False

# PUNTAJE
score = 0
fuente_como_bytes = fuente_bytes('FreeSansBold.ttf')
fuente = pygame.font.Font(fuente_como_bytes, 32)
texto_x = 10
texto_y = 10


# FUNCION MOSTRAR PUNTAJE
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {score}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# TEXTO FINAL DEL JUEGO
texto_final_x = 25
texto_final_y = 300


def texto_final(x, y):
    otro_texto= f'HAZ PERDIDO! LOS INVASORES HAN LLEGADO'
    texto_lose = fuente.render(f'{otro_texto}', True, (255, 255, 255))
    pantalla.blit(texto_lose, (x, y))


# FUNCION DEL ENEMIGO
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))


# FUNCION PRUEBA CON EL OBJETO ENEMIGO

def creacion_enemigos():
    list = [1, 2, 3, 4, 5, 6, 7, 8,9,10]
    enemigos_listos = []

    for i in list:
        i = Enemigo()
        enemigos_listos.append(i)
    return enemigos_listos


creando = creacion_enemigos()


# FUNCION DEL JUGADOR
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# FUNCION DISPARAR BALA
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 20, y + 10))


# FUNCION DETECTAR COLISIONES
def hay_colision(x_1, y_1, x_2, y_2):
    operacion = x_2 - x_1
    operacion2 = y_2 - y_1
    distancia = math.sqrt(math.pow(operacion, 2) + math.pow(operacion2, 2))
    if distancia < 27:
        return True
    else:
        return False


# DETECTAR COLISION DEL JUGADOR Y EL ENEMIGO
def hay_colision_enemigo(x_1, y_1, x_2, y_2):
    operacion = x_2 - x_1
    operacion2 = y_2 - y_1
    distancia = math.sqrt(math.pow(operacion, 2) + math.pow(operacion2, 2))
    if distancia < 27:
        return True
    else:
        return False


# LOOP DEL JUEGO
se_ejecuta = True

while se_ejecuta:
    # fondo de pantalla
    pantalla.blit(fondo, (0, 0))

    # ITERAR EVENTOS
    for evento in pygame.event.get():
        # EVENTO CERRAR
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        # EVENTO PRESIONAR TECLAS
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1.8

            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1.8

            if evento.key == pygame.K_SPACE:
                sonido_misil = mixer.Sound('disparo.mp3')
                sonido_misil.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # EVENTO SOLTAR FLECHAS
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # MODIFICAR UBICACION
    jugador_x += jugador_x_cambio

    # MANTENER DENTRO DE LOS BORDES al JUGADOR
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 725:
        jugador_x = 725

    # MODIFICAR UBICACION
    # enemigo_x += enemigo_x_cambio

    for i in creando:

        if i.enemigo_y > 520 or hay_colision_enemigo(i.enemigo_x, i.enemigo_y, jugador_x, jugador_y):

            for k in creando:
                k.enemigo_y=1000
                texto_final(texto_final_x, texto_final_y)
            break


        i.enemigo()
        i.enemigo_x += i.enemigo_x_cambio
        # MANTENER DENTRO DE LOS BORDES AL ENEMIGO

        if i.enemigo_x <= 0:
            i.enemigo_x_cambio = 2
            i.enemigo_y += i.enemigo_y_cambio
        elif i.enemigo_x >= 725:
            i.enemigo_x_cambio = -2
            i.enemigo_y += i.enemigo_y_cambio

        # colision
        colision = hay_colision(i.enemigo_x, i.enemigo_y, bala_x, bala_y)

        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            bala_y = 520
            bala_visible = False
            score += 1
            i.enemigo_x = random.randint(0, 734)
            i.enemigo_y = random.randint(34, 250)
            creando.remove(i)
            print(score)

    # enemigo(enemigo_x,enemigo_y)
    jugador(jugador_x, jugador_y)

    # MOSTRAR PUNTAJE
    mostrar_puntaje(texto_x, texto_y)

    # MOVIMIENTO BALA

    if bala_y <= -16:
        bala_y = 520
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # ACTUALIZAR
    pygame.display.update()
