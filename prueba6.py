import pygame, sys, random
pygame.init()
size = (800, 500)
# Crear ventana
screen = pygame.display.set_mode(size)
#Reloj 
clock = pygame.time.Clock()
x= 400
y= 250
#pygame.mouse.set_visible(False)
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
    mause_pos= pygame.mouse.get_pos()
    screen.fill(White)
    #Incio zona de dibujo
    if (mause_pos[0]>x):
        x +=2
    elif(mause_pos[0]==x):
        pass
    else:
        x-=2
    if (mause_pos[1]>y):
        y +=2
    elif(mause_pos[1]==y):
        pass
    else:
        y-=2
    pygame.draw.rect(screen, Red, (x,y, 100, 100))
    #Fin hora de dibujo
    #Pintar pantalla
    pygame.display.flip()
    clock.tick(30)