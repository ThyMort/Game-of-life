# tudo 
# 1 swinglish
# 2 seperation of concern
# 3 visa för limpan när det funkar så hittar vi på nått kul


import pygame
import time
import numpy as np

DEAD = (10, 10, 10)
GRID = (80, 80, 80)
ALIVE = (255, 255, 255) 

delay = 0.001
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

    cells = np.zeros((6 * size, 8 * size))
    
    screen.fill(GRID) 
    logic.py(screen, cells, size)
    screen.blit(setting_button, setting_rect)

    pygame.display.flip()
    pygame.display.update()

    game_logic = True
    running = False
    
    while game_logic:
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
            
            if pygame.mouse.get_pressed()[0]: 
                print ('id does')
                pos = pygame.mouse.get_pos()

                if setting_rect.collidepoint(pos): #open settings
                    running = False
                    options()
                    print ('option')
                    game_logic = False

                else:
                    cells[pos[1] // 10, pos[0] // 10] = 1
                    update(screen, cells, size)
                    pygame.display.update()
                    print ('placerar')

            if running == True:
                cells = update(screen, cells, size)
                screen.blit(setting_button, setting_rect)
                pygame.display.update()
        
        time.sleep(delay)

def options():

    running_options = True
    settings_color = (155, 185, 208)
    
    pygame.draw.rect(screen, settings_color, ((size, size),(40* size, 30 *size)))
    
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
                    game_logic = True

    pygame.display.flip()

    

                
if __name__ == '__main__':
    main()

