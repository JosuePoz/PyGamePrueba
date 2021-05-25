import pygame, sys, random
pygame.init()
size = (800, 500)
# Crear ventana
screen = pygame.display.set_mode(size)
#Reloj 
clock = pygame.time.Clock()
#Colores
Black   =       (   0,      0,      0   )
White   =       (   255,    255,    255 )
Red     =       (   255,    0,      0   )
Green   =       (   0,      255,    0   )
Blue    =       (   0,      0,      255 )
Orange  =       (   250,    105,    5   )
cor_list = []
for i in range(80):
        x = random.randint(0,800)
        y = random.randint(0,500)
        cor_list.append([x, y])
while True:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(White)
    #Incio zona de dibujo
    for cord in cor_list:
        
        pygame.draw.circle(screen, Red, cord, 2)
        if cord[1]<=500:
            cord[1]+=1
            cord[0] += random.randint(-1,1)
        else:
            cord[0]=random.randint(0,800)
            cord[1]=0
        
    #Fin hora de dibujo
    #Pintar pantalla
    pygame.display.flip()
    clock.tick(30)