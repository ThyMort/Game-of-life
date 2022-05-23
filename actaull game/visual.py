from datetime import datetime
import pygame
import time

import numpy as np
import logic 

GRID = (80, 80, 80)
DEAD = (10, 10, 10)
ALIVE = (255, 255, 255) 

delay = 0.5
size = 10
screen = pygame.display.set_mode((80 * size, 60* size))

setting_img = pygame.image.load('red.png').convert_alpha()
width = setting_img.get_width()
height = setting_img.get_height()

setting_button = pygame.transform.scale(setting_img, (int(width), int(height))) 
setting_rect = setting_button.get_rect(center = (770, 30))


def main():

    pygame.init()
    pygame.display.set_caption('Mårts Game of Life')
    last_update = time.time()

    screen.fill(GRID) #rita background
    
    running = False #starta pausad
    
    while True: #game loop
        # ibland när det är lämligt kör update
        # dvs: 

        for event in pygame.event.get(): #quit
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN: # start
                if event.key == pygame.K_SPACE:
                    if running == False: 
                        running = True
                    else:
                        running = False
                        
            
        if pygame.mouse.get_pressed()[0]: #click
            print ('click')
            pos = pygame.mouse.get_pos()

            if setting_rect.collidepoint(pos): #open settings
                running = False
                options()
                print ('option')

            else: 
                logic.place_cell(pos)
                print ('places cell')

        cell_list = logic.update(active=False)

        if time.time() - last_update > 1:
            last_update = time.time()
        
            if running:
                cell_list = logic.update(active=True)
            
    
        for rad, col in np.ndindex(cell_list.shape): #rita celler
            if [rad, col] == 1:
                cell_color = ALIVE
            else:
                cell_color = DEAD 
            
            pygame.draw.rect(screen, cell_color, (col * size, rad * size, size -1, size -1))       


        screen.blit(setting_button, setting_rect) 
        pygame.display.flip()
        print ('updating')
            


def options():

    running_options = True
    settings_color = (155, 185, 208)
    
    pygame.draw.rect(screen, settings_color, ((400, 0),(40* size, 30 *size)))
    
    pygame.display.flip()

    while running_options:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running_options = False
                    print('escape from options')          

    screen.fill(GRID)
         
if __name__ == '__main__':
    main()

