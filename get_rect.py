import pygame
import sys

pygame.init()
surface = pygame.display.set_mode( (200, 200) )
last_color = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill( (0,0,255) )
    pygame.draw.rect( surface, (255,0,0), (0, 0, 100, 100) )
    pygame.draw.rect( surface, (0,255,0), (100, 100, 100, 100) )


    color = surface.get_at(pygame.mouse.get_pos()) 
    if last_color != color:
        print(color)
        last_color = color

    pygame.display.update()

