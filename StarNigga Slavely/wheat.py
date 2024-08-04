import pygame


class Wheat():

    def __init__(self, pos):

        self.image = pygame.image.load("Assets/Hud/Hud wheat icon.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center = pos)
        self.wheat_delay = 5000
        self.upgraded = False
        self.give_wheat = 3

        pygame.time.set_timer(2, self.wheat_delay)