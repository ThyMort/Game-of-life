import pygame
import time
import numpy as np

Död = (10, 10, 10)
Grid = (80, 80, 80)
Lever = (255, 255, 255) 

tid = 0.001
size = 10

screen = pygame.display.set_mode((80 * size, 60* size))
pygame.display.set_caption('Mårts Game of Life')

setting_img = pygame.image.load('red.png').convert_alpha()
width = setting_img.get_width()
height = setting_img.get_height()
print (width, height)

setting_button = pygame.transform.scale(setting_img, (int(width * 2), int(height * 2))) 

setting_rect = setting_button.get_rect(center = (790, 60))


def update(screen, storlek, with_progress = False, cells = np.zeros((6 * size, 8 * size))):
    print (cells)
    
    if type(cells) == 'numpy.ndarray':
        nya_celler = np.zeros((cells.shape[0], cells.shape[1]))

    for rad, col in np.ndindex(cells.shape):
        alive = np.sum(cells[rad-1:rad +2, col-1:col+2]) - cells[rad, col]
        cellens_färg = Död if cells[rad, col] == 0 else Lever

        if cells[rad, col] == 1:
            if 2 <= alive <= 3: 
                nya_celler[rad, col] = 1
                if with_progress:
                    cellens_färg = Lever
                
            else:
                if with_progress:
                    cellens_färg = Död

        else:
            if alive == 3:
                nya_celler[rad, col] = 1
                if with_progress:
                    cellens_färg = Lever 

        pygame.draw.rect(screen, cellens_färg, (col * storlek, rad * storlek, storlek -1, storlek -1))
        screen.blit(setting_img, setting_rect)

    return nya_celler



def main():
    
    pygame.init()
    
    screen.fill(Grid)

    screen.blit(setting_img, setting_rect )

    update(screen, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False
    
    while True:
        for event in pygame.event.get(): #quit
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN: # start
                if event.key == pygame.K_SPACE:
                    running = not running
                    pygame.display.update(screen, 10)

            
            
            if pygame.mouse.get_pressed()[0]: 
                
                pos = pygame.mouse.get_pos()

                
                if setting_rect.collidepoint(pos): #open settings
                    running = not running
                    options()

                else:
                    if pos[1] == 1:
                        cells = pos[1]
                    
                    else:
                        cells = pos[0] = 1 #placera cell
                    pygame.display.update(screen, 10, cells)

        screen.fill(Grid)

        if running:
            pygame.display.update(screen, cells, 10, with_progress = True)

        time.sleep(tid)

def options():
    running_options = True
    cells = np.zeros((60, 80))

    while running_options:
        screen.fill((Lever))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running_options = False
                    print('escape from options')
   
    
        pygame.display.update(screen, 10, with_progress = True)


if __name__ == '__main__':
    main()

