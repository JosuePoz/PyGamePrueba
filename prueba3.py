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

# Crear ventana
screen = pygame.display.set_mode(size)
while True:
    for event  in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
    #Fondo de pantall
    screen.fill(White)
    #Incio zona de dibujo

    for x in range(100, 700, 100):
        pygame.draw.rect(screen, Black, (x, 250, 50, 50))
        pygame.draw.line(screen, Green, (x, 0), (x, 100), 10 )
        #pygame.draw.polygon(screen, Red, [(146,0), (291,106), (236,277), (26,277), (0,106)], 60)
        pygame.draw.circle(screen, Blue, (x, 100), 100, 10)
        
    for x in range(0, 600, 100):
        pygame.draw.ellipse(screen, Orange, (x, 200, 200, 50), 10)

    #Fin hora de dibujo
    #Pintar pantalla
    pygame.display.flip()
    clock.tick(20)