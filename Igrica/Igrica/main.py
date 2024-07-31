import pygame, sys, random


# Player class
class Player(pygame.sprite.Sprite):

    def __init__(self, pos, group):

        super().__init__(group)
        self.image = pygame.image.load("Igrica/Assets/Character/Woman/Woman_idle.PNG").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 60))
        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2()
        self.speed = 3

    def input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:

            self.direction.y = -1
        
        elif keys[pygame.K_s]:

            self.direction.y = 1

        else:

            self.direction.y = 0
        
        if keys[pygame.K_a]:

            self.direction.x = -1
        
        elif keys[pygame.K_d]:

            self.direction.x = 1
        
        else:

            self.direction.x = 0
    
    def update(self):

        self.input()
        self.rect.center += self.direction * self.speed


# House class
class House(pygame.sprite.Sprite):

    def __init__(self, pos, group):

        super().__init__(group)
        self.image = pygame.image.load("Igrica/Assets/House/Level 1/HOUSE 1 - DAY.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect(center = pos)


# Barn class
class Barn(pygame.sprite.Sprite):

    def __init__(self, pos, group):

        super().__init__(group)
        self.image = pygame.image.load("Igrica/Assets/Barn/Barn.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect(center = pos)


# Water class
class Water():

    def __init__(self, pos):

        self.image = pygame.image.load("Igrica/Assets/Water/WATER TILE - DAY.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 2000))
        self.rect = self.image.get_rect(center = pos)


# Bridge
class Bridge():

    def __init__(self, pos):
        
        self.image = pygame.image.load("Igrica/Assets/Bridge/BRIDGE - DAY.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect(center = pos)


# Camera class
class CameraGroup(pygame.sprite.Group):

    global no_clipable_sprites

    def __init__(self):

        super().__init__()

        self.display_surface = pygame.display.get_surface()

        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

    def center_target_camera(self, target):

        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self, player):

        self.center_target_camera(player)

        for sprite in no_clipable_sprites:

            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):

            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)


# Initialize
pygame.init()


# Window
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()


# Camera setup
camera_group = CameraGroup()


# World design
player = Player((100, 100), camera_group)
water = Water((1000, 300))
bridge = Bridge((1000, 300))
House((0, 0), camera_group)
Barn((450, 5), camera_group)

no_clipable_sprites = [water, bridge]


# Main loop
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    clock.tick(60)
    
    screen.fill("#7CFC00")

    camera_group.update()
    camera_group.custom_draw(player)

    pygame.display.update()