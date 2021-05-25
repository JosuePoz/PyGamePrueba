import pygame, sys, random
pygame.init()
size = (800, 500)
# Crear ventana
screen = pygame.display.set_mode(size)
#Reloj 
clock = pygame.time.Clock()
x = 0
y = 400
speed_x = 0
speed_y = 0
#Colores
Black   =       (   0,      0,      0   )
White   =       (   255,    255,    255 )
Red     =       (   255,    0,      0   )
Green   =       (   0,      255,    0   )
Blue    =       (   0,      0,      255 )
Orange  =       (   250,    105,    5   )

while True:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -4
            if event.key == pygame.K_RIGHT:
                speed_x = 4
            if event.key == pygame.K_z:
                speed_x *= 2
            if event.key == pygame.K_LEFT:
                speed_x = -4
            if event.key == pygame.K_RIGHT:
                speed_x = 4
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_z:
                speed_x *= 0.5
    
    screen.fill(White)
    #Incio zona de dibujo
    x += speed_x
    pygame.draw.rect(screen, Red, (x,y, 100, 100))
    #Fin hora de dibujo
    #Pintar pantalla
    pygame.display.flip()
    clock.tick(30)