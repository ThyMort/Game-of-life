# tudo 
# 1 swinglish
# 2 seperation of concern
# 3 visa för limpan när det funkar så hittar vi på nått kul


import pygame
import time
import numpy as np

Död = (10, 10, 10)
Grid = (80, 80, 80)
Lever = (255, 255, 255) 

tid = 0.5
size = 10
screen = pygame.display.set_mode((80 * size, 60* size))

setting_img = pygame.image.load('red.png').convert_alpha()
width = setting_img.get_width()
height = setting_img.get_height()
print (width, height)

setting_button = pygame.transform.scale(setting_img, (int(width * 2), int(height * 2))) 
setting_rect = setting_button.get_rect(center = (790, 60))

def update(screen, cells, storlek = 10): 
    
    nya_celler = np.zeros((cells.shape[0], cells.shape[1]))

    for rad, col in np.ndindex(cells.shape):
        alive = np.sum(cells[rad-1:rad +2, col-1:col+2]) - cells[rad, col]
        
        if cells[rad, col] == 1:
            if 2 <= alive <= 3: 
                nya_celler[rad, col] = 1                    
                cellens_färg = Lever       
            else:
                nya_celler[rad, col] = 0    
                cellens_färg = Död
        else:
            if alive == 3:
                nya_celler[rad, col] = 1
                cellens_färg = Lever 
            else:
                nya_celler[rad, col] = 0    
                cellens_färg = Död

        pygame.draw.rect(screen, cellens_färg, (col * storlek, rad * storlek, storlek -1, storlek -1))

    return nya_celler


def main():
    
    pygame.init()
    pygame.display.set_caption('Mårts Game of Life')

    cells = np.zeros((6 * size, 8 * size))
    
    screen.fill(Grid) 
    update(screen, cells)

    screen.blit(setting_button, setting_rect)
    pygame.display.update()

    running = False
    
    while True:
        for event in pygame.event.get(): #quit
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN: # start
                if event.key == pygame.K_SPACE:
                    if running == False:
                        running = True
                        pygame.display.update(screen, cells)
                    else:
                        running = False
                        pygame.display.update(screen, cells)  
            
            if pygame.mouse.get_pressed()[0]: 
                
                pos = pygame.mouse.get_pos()

                if setting_rect.collidepoint(pos): #open settings
                    running = False
                    options()

                else:
                    cells[pos[1] // 10, pos[0] // 10] = 1
                    update(screen, cells)
                    ##pygame.display.update(screen, cells)
                    pygame.display.update()

        if running == True:
            pygame.display.update(screen, cells)

        time.sleep(tid)

def options():
    running_options = True
    settings_färg = (155, 185, 208)
    pygame.draw.rect(screen, settings_färg, (40* size, 30 *size))

    while running_options:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running_options = False
                    print('escape from options')

    main()

if __name__ == '__main__':
    main()

