import pygame
import time
import numpy as np

Svart = [10, 10, 10]
Vit = (255, 255, 255) 
Grid = (20, 30, 250)
Zombie = (170, 170, 170)
Size = 10



def update(screen, cells, storlek, with_progress = False):
    ny_cell = np.zeros((cells.shape[0], cells.shape[1]))

    for rad, col in np.ndindex(cells.shape):
        alive = np.sum(cells[rad-1:rad +2]) - cells[rad, col]
        färg = Svart if cells[rad, col] == 0 else Vit

        if cells[rad, col] == 1:
            if 2 <= alive <= 3: 
                ny_cell[rad, col] = 1
                if with_progress:
                    färg = Vit
                
            else:
                if with_progress:
                    färg = Zombie


        else:
            if alive == 3:
                ny_cell[rad, col] = 1
                if with_progress:
                    färg = Vit 

        
        pygame.draw.rect(screen, färg, (col * storlek, rad * storlek, storlek -1, storlek -1))
        
    return ny_cell


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cells = np.zeros((60, 80))
    screen.fill(Grid)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(Grid)

        if running:
            cells = update(screen, cells, 10, with_progress = True)
            pygame.display.update()

        time.sleep(0.001)


if __name__ == '__main__':
    main()