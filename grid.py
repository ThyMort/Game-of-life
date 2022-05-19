import pygame
import time
import numpy as np

Svart = (10, 10, 10)
Grid = (40, 40, 40)
Zombie = (170, 170, 170)
Vit = (255, 255, 255) 

tid = 0.5
size = 100

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
                    färg = Zombie


        else:
            if alive == 3:
                nya_celler[rad, col] = 1
                if with_progress:
                    färg = Vit 

        pygame.draw.rect(screen, färg, (col * storlek, rad * storlek, storlek -1, storlek -1))
        
    return nya_celler



def main():
    pygame.init()
    screen = pygame.display.set_mode((8 * size, 6* size))
    
    button_1 = pygame.Rect(50, 100, 200, 50)
    pygame.draw.rect(screen, (255, 0, 0), button_1)

    cells = np.zeros((60, 80))
    screen.fill(Grid)
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
            
            if pygame.mouse.get_pressed()[0]: #placera cell
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

            button = pygame.Rect(50, 100, 200, 50)
            
            if button.collidepoint(pos):
                if click:
                    options()

 
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
 
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
        'options', (255, 255, 255), screen, 20, 20
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()


if __name__ == '__main__':
    main()