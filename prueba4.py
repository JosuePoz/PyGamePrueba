import pygame, sys
pygame.init()
size = (800, 500)
#Colores
Black   =       (   0,      0,      0   )
White   =       (   255,    255,    255 )
Red     =       (   255,    0,      0   )
Green   =       (   0,      255,    0   )
Blue    =       (   0,      0,      255 )
Orange  =       (   250,    105,    5   )
#Cordenadas
cord_x = 400
cord_y = 200
#Velocidad
speed_x= 3
speed_y= 2
#Reloj 
clock = pygame.time.Clock()
# Crear ventana
screen = pygame.display.set_mode(size)
while True:
    for event  in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
    if(cord_x >=730 or cord_x<=-10):
        speed_x*=-1 


    cord_x += speed_x
    #Fondo de pantall
    screen.fill(White)
    #Incio zona de dibujo

    pygame.draw.rect(screen, Orange, (cord_x, cord_y, 80, 80))

    #Fin hora de dibujo
    #Pintar pantalla
    pygame.display.flip()
    clock.tick(40)