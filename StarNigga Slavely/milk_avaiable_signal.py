import pygame

class Milk_Avaible_Signal():

    def __init__(self, pos):

        self.image = pygame.image.load("Assets/Animals/Cows/milk.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center = pos)