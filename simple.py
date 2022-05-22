import pygame

pygame.init()

pos = pygame.mouse.get_pos()

cells = [pos[1] // 10, pos[0] // 10] = 1

print(cells)

