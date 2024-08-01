import pygame, sys, random


# Player class
class Player(pygame.sprite.Sprite):

    def __init__(self, pos, group):

        super().__init__(group)
        self.down_sprites = []
        self.up_sprites = []
        self.left_sprites = []
        self.right_sprites = []
        self.idle_sprite = []
        self.down_current_sprite = 0
        self.up_current_sprite = 0
        self.left_current_sprite = 0
        self.right_current_sprite = 0

        self.idle_sprite.append(pygame.image.load("Igrica/Assets/Character/Woman/Woman_idle.PNG").convert_alpha())

        self.down_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Down/Move_down_1.PNG").convert_alpha())
        self.down_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Down/Move_down_2.PNG").convert_alpha())
        self.down_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Down/Move_down_3.PNG").convert_alpha())
        self.down_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Down/Move_down_2.PNG").convert_alpha())

        self.up_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Up/Move_up_1.PNG").convert_alpha())
        self.up_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Up/Move_up_2.PNG").convert_alpha())
        self.up_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Up/Move_up_3.PNG").convert_alpha())
        self.up_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Up/Move_up_2.PNG").convert_alpha())

        self.left_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Left/Move_left_1.PNG").convert_alpha())
        self.left_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Left/Move_left_2.PNG").convert_alpha())
        self.left_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Left/Move_left_3.PNG").convert_alpha())
        self.left_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Left/Move_left_2.PNG").convert_alpha())

        self.right_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Right/Move_right_1.PNG").convert_alpha())
        self.right_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Right/Move_right_2.PNG").convert_alpha())
        self.right_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Right/Move_right_3.PNG").convert_alpha())
        self.right_sprites.append(pygame.image.load("Igrica/Assets/Character/Woman/Move Anim/Right/Move_right_2.PNG").convert_alpha())



        self.image = self.idle_sprite[0]
        self.image = pygame.transform.scale(self.image, (40, 50))
        
        self.rect = self.image.get_rect(center = pos)
        
        self.direction = pygame.math.Vector2()
        self.speed = 3

        self.milk = 0
        self.wheat = 0
        self.coins = 0

        self.milk_font = pygame.font.SysFont("cascadia code", 50)
        self.wheat_font = pygame.font.SysFont("cascadia code", 50)
        self.coins_font = pygame.font.SysFont("cascadia code", 50)

    def input(self):

        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_w]:

            self.direction.y = -1

            self.up_current_sprite += 0.12

            if self.up_current_sprite > len(self.up_sprites):

                self.up_current_sprite = 0

            self.image = self.up_sprites[int(self.up_current_sprite)]
            self.image = pygame.transform.scale(self.image, (40, 50))
        
        elif self.keys[pygame.K_s]:

            self.direction.y = 1

            self.down_current_sprite += 0.12

            if self.down_current_sprite > len(self.down_sprites):

                self.down_current_sprite = 0

            self.image = self.down_sprites[int(self.down_current_sprite)]
            self.image = pygame.transform.scale(self.image, (40, 50))

        else:

            self.direction.y = 0
        
        if self.keys[pygame.K_a]:

            self.direction.x = -1

            self.left_current_sprite += 0.12

            if self.left_current_sprite > len(self.left_sprites):

                self.left_current_sprite = 0

            self.image = self.left_sprites[int(self.left_current_sprite)]
            self.image = pygame.transform.scale(self.image, (40, 50))
        
        elif self.keys[pygame.K_d]:

            self.direction.x = 1

            self.right_current_sprite += 0.12

            if self.right_current_sprite > len(self.right_sprites):

                self.right_current_sprite = 0

            self.image = self.right_sprites[int(self.right_current_sprite)]
            self.image = pygame.transform.scale(self.image, (40, 50))
        
        else:

            self.direction.x = 0


    def get_milk(self):

        if self.rect.colliderect(cow.rect) and cow.milk_avaible and self.keys[pygame.K_e]:

            self.milk += 1
            cow.milk_avaible = False

        if event.type == 1:

            cow.milk_avaible = True

    def hud(self):

        self.milk_text = self.milk_font.render(f"mleko:{self.milk}", True, "black")
        screen.blit(self.milk_text, (30, 30))

        self.wheat_text = self.wheat_font.render(f"pšenica:{self.wheat}", True, "black")
        screen.blit(self.wheat_text, (30, 70))

        self.coins_text = self.coins_font.render(f"novčić:{self.coins}", True, "black")
        screen.blit(self.coins_text, (30, 110))

    def update(self):

        self.input()
        self.get_milk()
        self.rect.center += self.direction * self.speed


# House class
class House(pygame.sprite.Sprite):

    def __init__(self, pos, group):

        super().__init__(group)
        self.image = pygame.image.load("Igrica/Assets/House/Level 1/HOUSE 1 - DAY.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect(center = pos)


# Water class
class Water():

    def __init__(self, pos):

        self.image = pygame.image.load("Igrica/Assets/Water/WATER TILE - DAY.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 2000))
        self.rect = self.image.get_rect(center = pos)


# Cow
class Cow():

    def __init__(self, pos):

        self.image = pygame.image.load("Igrica/Assets/Animals/Cows/Cow.PNG").convert_alpha()
        self.image = pygame.transform.scale(self.image, (90, 70))
        self.rect = self.image.get_rect(center = pos)
        self.milk_delay = 10000

        pygame.time.set_timer(1, self.milk_delay)

        self.milk_avaible = True

class Milk_Avaible_Signal():

    def __init__(self, pos):

        self.image = pygame.image.load("Igrica/Assets/Animals/Cows/milk.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
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

        for sprite in milk_signal_sprite:

            if cow.milk_avaible:

                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)


# Initialize
pygame.init()


# Window
screen = pygame.display.set_mode((1500, 900))
clock = pygame.time.Clock()


# Camera setup
camera_group = CameraGroup()


# World design
player = Player((100, 100), camera_group)

water = Water((1000, 300))

bridge = Bridge((1000, 300))

cow = Cow((300, 0))

milk_avaible_signal = Milk_Avaible_Signal((345, -45))

House((0, 0), camera_group)

no_clipable_sprites = [water, bridge, cow]
milk_signal_sprite = [milk_avaible_signal]


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
    player.hud()

    pygame.display.update()