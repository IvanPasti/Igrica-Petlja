import pygame

# Water class
class Water():

    def __init__(self, pos):

        self.image = pygame.image.load("Assets/Water/WATER TILE - DAY.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 2000))
        self.rect = self.image.get_rect(center = pos)