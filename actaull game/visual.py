import pygame
from threading import Timer

import numpy as np
import logic 


numba = 0

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
    
    numba_1 = 0

    pygame.init()
    pygame.display.set_caption('Mårts Game of Life')

    cell_list = logic.update()

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
                        running = logic.status(True)
    
                    else:
                        running = logic.status(False)
            
        if pygame.mouse.get_pressed()[0]: #click
            print ('id does')
            pos = pygame.mouse.get_pos()

            if setting_rect.collidepoint(pos): #open settings
                running = False
                options()
                print ('option')

            else: 
                logic.place_cell(pos)
            
        for rad, col in np.ndindex(cell_list.shape): #rita celler
            if [rad, col] == 1:
                cell_color = ALIVE
            else:
                cell_color = DEAD 
            
            pygame.draw.rect(screen, cell_color, (col * size, rad * size, size -1, size -1))       


        if numba_1 != delayer():
            screen.blit(setting_button, setting_rect) 
            pygame.display.flip()
            numba_1 = numba

def delayer():
    global numba
    numba += 1
    Timer(1, delayer).start
    return numba

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

