import pygame
from button import Button

# House class
class House(pygame.sprite.Sprite):

    def __init__(self, pos, group, screen, width, height):

        super().__init__(group)
        self.image_1 = pygame.image.load("Assets/House/Level 1/HOUSE 1 - DAY.png").convert_alpha()
        self.image_1 = pygame.transform.scale(self.image_1, (300, 300))

        self.image_2 = pygame.image.load("Assets/House/Level 2/HOUSE 2 - DAY.png").convert_alpha()
        self.image_2 = pygame.transform.scale(self.image_2, (300, 300))

        self.arrow_image = pygame.image.load("Assets/House/house upgrade arrow.png").convert_alpha()
        self.arrow_image = pygame.transform.scale(self.arrow_image, (200, 150))

        self.upgrade_button_image = pygame.image.load("Assets/House/upgrade.png").convert_alpha()
        self.upgrade_button_image = pygame.transform.scale(self.upgrade_button_image, (400, 150))

        self.image = self.image_1

        self.house_level = 1

        self.rect = self.image.get_rect(center = pos)
        self.screen = screen
        self.width = width
        self.height = height

        self.upgrade_button = Button(self.width // 2 - 200, self.height // 2 + 150, self.upgrade_button_image, 0.8)
    
    def upgrade_menu(self):

        pygame.draw.rect(self.screen, (255, 201, 14), pygame.Rect(self.width // 2 - 600, self.height // 2 - 350, 1200, 700))

        self.screen.blit(self.image_1, (self.width // 2 - 550, self.height // 2 - 300))
        
        self.screen.blit(self.arrow_image, (self.width // 2 - 100, self.height // 2 - 175))

        self.screen.blit(self.image_2, (self.width //2 + 250, self.height // 2 - 300))

    def upgrade(self):

        self.upgrade_menu()
        self.upgrade_button.draw(self.screen)