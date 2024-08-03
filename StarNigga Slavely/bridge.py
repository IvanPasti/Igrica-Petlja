import pygame

# Bridge
class Bridge():

    def __init__(self, pos):
        
        self.image = pygame.image.load("Assets/Bridge/BRIDGE - DAY.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect(center = pos)