import pygame, sys
pygame.init()
size = (800, 500)
#Colores
Black   =  (   0,      0,      0   )
White   =  (   255,    255,    255 )
Red     =    (   255,    0,      0   )
Green   =  (   0,      255,    0   )
Blue    =   (   0,      0,      255)
# Crear ventana
screen = pygame.display.set_mode(size)
while True:
    for event  in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
    #Fondo de pantall
    screen.fill(White)
    #Incio zona de dibujo

    pygame.draw.line(screen, Green, [0,100], [100, 100], 5)
    pygame.draw.rect(screen,  Red, (100, 100, 80, 80))
    pygame.draw.circle(screen, Blue, (200, 200), 50)

    #Fin hora de dibujo
    #Pintar pantalla
    pygame.display.flip()