import pygame
import numpy as np

DEAD = (10, 10, 10)
ALIVE = (255, 255, 255) 

def update(screen, cells, size): 
    
    new_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for rad, col in np.ndindex(cells.shape):
        alive = np.sum(cells[rad-1:rad +2, col-1:col+2]) - cells[rad, col]
        
        if cells[rad, col] == 1:
            if 2 <= alive <= 3: 
                new_cells[rad, col] = 1                    
                cell_color = ALIVE       
            else:
                new_cells[rad, col] = 0    
                cell_color = DEAD
        else:
            if alive == 3:
                new_cells[rad, col] = 1
                cell_color = ALIVE 
            else:
                new_cells[rad, col] = 0    
                cell_color = DEAD

        pygame.draw.rect(screen, cell_color, (col * size, rad * size, size -1, size -1))
   
    return new_cells