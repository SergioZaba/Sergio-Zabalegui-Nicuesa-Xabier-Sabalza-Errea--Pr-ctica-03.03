
import pygame
import time


pygame.init()
ventana = pygame.display.set_mode((840,680))
pygame.display.set_caption("ARKANOID")

ball = pygame.image.load("pelota.png")
ballrect = ball.get_rect()
speed = [7,7]
ballrect.move_ip(0,0)

# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("perro.png")
baterect = bate.get_rect()

# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(340,550)

# Al perder la partida nos saldra una goto de game over y se saldra del juego a los 3 segundos
final = pygame.image.load("gameover.png")
finalrect = final.get_rect()
finalrect.move_ip(110,110)


# Empezara a sonar una canción cuando estemos jugando al juego
sonido_fondo = pygame.mixer.Sound("cancion.wav")
pygame.mixer.Sound.play(sonido_fondo)

imagen_ladrillo = "comidaperro1.png"
class Huesitos:
    def __init__(self, pos_x, pos_y, imagen_ladrillo):
        self.__image = pygame.image.load(imagen_ladrillo)
        self.__rect = self.image.get_rect()
        self.__rect.move_ip(pos_x, pos_y)

    @property
    def image(self):
        return self.__image

    @property
    def image_rect(self):
        return self.__rect

lista_ladrillos = []
for posx in range(16):
    for posy in range(7):
        lista_ladrillos.append(Huesitos(60*posx, 55*posy, "comidaperro1.png"))


jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-8,0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(8,0)

    # Compruebo si hay colisión
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]
    ventana.fill((179, 220, 172))
    ventana.blit(ball, ballrect)

    for a in lista_ladrillos:
        if ballrect.colliderect(a.image_rect):
            speed[1] = -speed[1]
            lista_ladrillos.remove(a)

    if ballrect.bottom > ventana.get_height():
        pygame.mixer.Sound.stop(sonido_fondo)
        sonido_final = pygame.mixer.Sound("siuu.wav")
        pygame.mixer.Sound.play(sonido_final)
        jugando = False
        ventana.blit(final, finalrect)

    # Dibujo el bate
    ventana.blit(bate, baterect)


    for ladrillo in lista_ladrillos:
        ventana.blit(ladrillo.image, ladrillo.image_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
    #Crear ladrillos



time.sleep(5)
pygame.quit()