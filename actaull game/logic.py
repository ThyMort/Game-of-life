import numpy as np

cells = np.zeros((60, 80))

def update(active= False): 
    
    global cells

    new_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for rad, col in np.ndindex(cells.shape):
        alive = np.sum(cells[rad-1:rad +2, col-1:col+2]) - cells[rad, col]

        if active: 
            if cells[rad, col] == 1:
                if 2 <= alive <= 3: 
                    new_cells[rad, col] = 1                    
              
                else:
                    new_cells[rad, col] = 0    
                    
            else:
                if alive == 3:
                    new_cells[rad, col] = 1
                   
                else:
                    new_cells[rad, col] = 0   
            
            cells = new_cells 
        
    return cells

def place_cell(place):
    global cells

    #if cells[place[1] // 10, place[0] // 10] == 1:
        #cells[place[1] // 10, place[0] // 10] = 0
    #else:
    cells[place[1] // 10, place[0] // 10] = 1
    