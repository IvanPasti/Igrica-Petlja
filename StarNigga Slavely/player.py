import pygame

pygame.init()

# Player class
class Player(pygame.sprite.Sprite):

    def __init__(self, pos, group, screen, cow, shop, house, wheat):

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
        self.screen = screen
        self.cow = cow
        self.shop = shop
        self.house = house
        self.wheat = wheat

        self.idle_sprite.append(pygame.image.load("Assets/Character/Woman/Woman_idle.PNG").convert_alpha())

        self.down_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Down/Move_down_1.PNG").convert_alpha())
        self.down_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Down/Move_down_2.PNG").convert_alpha())
        self.down_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Down/Move_down_3.PNG").convert_alpha())
        self.down_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Down/Move_down_2.PNG").convert_alpha())

        self.up_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Up/Move_up_1.PNG").convert_alpha())
        self.up_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Up/Move_up_2.PNG").convert_alpha())
        self.up_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Up/Move_up_3.PNG").convert_alpha())
        self.up_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Up/Move_up_2.PNG").convert_alpha())

        self.left_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Left/Move_left_1.PNG").convert_alpha())
        self.left_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Left/Move_left_2.PNG").convert_alpha())
        self.left_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Left/Move_left_3.PNG").convert_alpha())
        self.left_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Left/Move_left_2.PNG").convert_alpha())

        self.right_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Right/Move_right_1.PNG").convert_alpha())
        self.right_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Right/Move_right_2.PNG").convert_alpha())
        self.right_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Right/Move_right_3.PNG").convert_alpha())
        self.right_sprites.append(pygame.image.load("Assets/Character/Woman/Move Anim/Right/Move_right_2.PNG").convert_alpha())

        self.hud_coin_image = pygame.image.load("Assets/Hud/hud coin icon.png").convert_alpha()
        self.hud_coin_image = pygame.transform.scale(self.hud_coin_image, (50, 50))

        self.hud_milk_image = pygame.image.load("Assets/Hud/hud milk icon.png").convert_alpha()
        self.hud_milk_image = pygame.transform.scale(self.hud_milk_image, (50, 50))

        self.hud_wheat_image = pygame.image.load("Assets/Hud/Hud wheat icon.png").convert_alpha()
        self.hud_wheat_image = pygame.transform.scale(self.hud_wheat_image, (50, 50))

        self.image = self.idle_sprite[0]
        self.image = pygame.transform.scale(self.image, (40, 50))
        
        self.rect = self.image.get_rect(center = pos)
        
        self.direction = pygame.math.Vector2()
        self.speed = 3

        self.milk = 0
        self.wheat_inventory = 0
        self.coins = 100

        self.milk_font = pygame.font.Font("Assets/Font/m5x7.ttf", 50)
        self.wheat_font = pygame.font.Font("Assets/Font/m5x7.ttf", 50)
        self.coins_font = pygame.font.Font("Assets/Font/m5x7.ttf", 50)

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

        if self.rect.colliderect(self.cow.rect) and self.cow.milk_avaible:

            self.milk += self.cow.milk_give
            self.cow.milk_avaible = False

    def use_shop(self):

        if self.rect.colliderect(self.shop.rect) and self.keys[pygame.K_e]:

            self.shop.in_shop = True

    def use_upgrade_house(self):

        if self.rect.colliderect(self.house.rect) and self.keys[pygame.K_e]:
            print(self.cow, self.wheat)
            if self.cow.upgraded and self.wheat.upgraded and self.house.house_level == 1:

                self.house.in_menu = True
            
            elif self.house.house_level == 1:

                self.house.in_menu_cow_wheat = True
            
        if self.house.upgrade_button.input() and self.coins >= 50 and self.house.in_menu:

            self.house.house_level = 2
            self.house.image = self.house.image_2
            self.house.in_menu = False
            self.coins -= 50
            
        if self.house.upgrade_cow_button.input() and self.coins >= 10 and not self.cow.upgraded and self.house.in_menu_cow_wheat:

            print("upgrade")
    
            self.coins -= 10
            self.cow.upgraded = True
            self.cow.milk_give = 2
        
        if self.house.upgrade_wheat_button.input() and self.coins > 10 and not self.wheat.upgraded and self.house.in_menu_cow_wheat:

            print("Upgrade")

            self.coins -= 10
            self.wheat.upgraded = True
            self.wheat.give_wheat = 6

    def hud(self):

        self.milk_text = self.milk_font.render(f"{self.milk}", True, "black")
        self.screen.blit(self.milk_text, (70, 15))
        self.screen.blit(self.hud_milk_image, (10, 10))

        self.wheat_text = self.wheat_font.render(f"{self.wheat_inventory}", True, "black")
        self.screen.blit(self.wheat_text, (70, 76))
        self.screen.blit(self.hud_wheat_image, (10, 75))

        self.coins_text = self.coins_font.render(f"{self.coins}", True, "black")
        self.screen.blit(self.coins_text, (70, 141))
        self.screen.blit(self.hud_coin_image, (10, 140))

    def update(self):

        self.input()
        self.use_shop()
        self.use_upgrade_house()
        self.rect.center += self.direction * self.speed