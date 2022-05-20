import pygame
import time
import numpy as np

pygame.init()


Svart = (10, 10, 10)
Grid = (80, 80, 80)
Vit = (255, 255, 255) 
Röd = (255, 0, 0)

tid = 0.001
size = 100

button = pygame.Surface((20, 20))
button.fill(Röd) 
button_rect = button.get_rect(center = (780, 20))


def update(screen, cells, storlek, with_progress = False):
    nya_celler = np.zeros((cells.shape[0], cells.shape[1]))

    for rad, col in np.ndindex(cells.shape):
        alive = np.sum(cells[rad-1:rad +2, col-1:col+2]) - cells[rad, col]
        färg = Svart if cells[rad, col] == 0 else Vit

        if cells[rad, col] == 1:
            if 2 <= alive <= 3: 
                nya_celler[rad, col] = 1
                if with_progress:
                    färg = Vit
                
            else:
                if with_progress:
                    färg = Svart

        else:
            if alive == 3:
                nya_celler[rad, col] = 1
                if with_progress:
                    färg = Vit 

        pygame.draw.rect(screen, färg, (col * storlek, rad * storlek, storlek -1, storlek -1))
        screen.blit(button, button_rect)

    return nya_celler

screen = pygame.display.set_mode((8 * size, 6* size))

def main():

    pygame.display.set_caption('Mårts Game of Life')

    cells = np.zeros((60, 80))
    screen.fill(Grid)

    text = (pygame.font.SysFont('Corbel',35)).render('yes' , True , Röd)
    button.blit(text, (20, 30))
    
    screen.blit(button, button_rect)

    
    pygame.draw.rect

    update(screen, cells, 10)

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
                    update(screen, cells, 10)
                    pygame.display.update()

            pos = pygame.mouse.get_pos()
            
            if pygame.mouse.get_pressed()[0]: 
                pos = pygame.mouse.get_pos()
                
                if button_rect.collidepoint(pos): #open settings
                    running = not running
                    options()


                else:
                    cells[pos[1] // 10, pos[0] // 10] = 1 #placera cell
                    update(screen, cells, 10)
                    pygame.display.update()

        screen.fill(Grid)

        if running:
            cells = update(screen, cells, 10, with_progress = True)
            pygame.display.update()

        time.sleep(tid)

def options():
    running_options = True
    
    while running_options:
        screen.fill((Vit))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running_options = False

        pygame.display.update()


if __name__ == '__main__':
    main()