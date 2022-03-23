import pygame
import time

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000, 500))
    surface.fill((125, 99, 26))
    pygame.display.flip()

    time.sleep(5)