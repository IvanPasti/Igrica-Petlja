import pygame

# Cow
class Cow():

    def __init__(self, pos):

        self.image = pygame.image.load("Assets/Animals/Cows/Cow.PNG").convert_alpha()
        self.image = pygame.transform.scale(self.image, (90, 70))
        self.rect = self.image.get_rect(center = pos)
        self.milk_delay = 10000
        self.milk_avaible = True

        pygame.time.set_timer(1, self.milk_delay)