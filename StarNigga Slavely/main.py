import pygame, sys, random
from player import Player
from cow import Cow
from bridge import Bridge
from water import Water
from house import House
from button import Button
from milk_avaiable_signal import Milk_Avaible_Signal
from wheat import Wheat


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


# Shop
class Shop(pygame.sprite.Sprite):

    def __init__(self, pos, group):

        super().__init__(group)

        self.image = pygame.image.load("Assets/Shop/Shop.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.rect = self.image.get_rect(center = pos)
        self.rect = self.image.get_rect(center = pos)
        self.buy_image = pygame.image.load("Assets/Shop/Buy Button Shop.png").convert_alpha()
        self.buy_image = pygame.transform.scale(self.buy_image, (150, 150))
        self.sell_image = pygame.image.load("Assets/Shop/Shop Sell Button.png").convert_alpha()
        self.sell_image = pygame.transform.scale(self.sell_image, (150, 150))
        self.exit_image = pygame.image.load("Assets/Shop/Exit button.png").convert_alpha()
        self.exit_image = pygame.transform.scale(self.exit_image, (125, 125))
        self.milk_icon = pygame.image.load("Assets/Animals/Cows/milk.png").convert_alpha()
        self.milk_icon = pygame.transform.scale(self.milk_icon, (100, 100))
        self.milk_coin_icon = pygame.image.load("Assets/Shop/milk price.png").convert_alpha()
        self.milk_coin_icon = pygame.transform.scale(self.milk_coin_icon, (150, 150))
        self.sell_button = Button(Width // 2 + 390, Height // 2 - 205, self.sell_image, 0.8)
        self.buy_button = Button(Width // 2 + 390, Height // 2 - 205, self.buy_image, 0.8)
        self.exit_button = Button(Width // 2 + 490, Height // 2 - 340, self.exit_image, 0.8)
        self.milk_font = pygame.font.Font("Assets/Font/m5x7.ttf", 100)

        self.in_shop = False

    def shop_menu(self):

        pygame.draw.rect(screen, (255, 201, 14), pygame.Rect(Width // 2 - 600, Height // 2 - 350, 1200, 700))

        pygame.draw.rect(screen, (215, 167, 0), pygame.Rect(Width // 2 - 550, Height // 2 - 220, 1100, 150))
        pygame.draw.rect(screen, (215, 167, 0), pygame.Rect(Width // 2 - 550, Height // 2 - 30, 1100, 150))
        pygame.draw.rect(screen, (215, 167, 0), pygame.Rect(Width // 2 - 550, Height // 2 + 170, 1100, 150))

        screen.blit(self.milk_icon, (Width // 2 - 510, Height // 2 - 200))
        screen.blit(self.milk_coin_icon, (Width // 2 + 220, Height // 2 - 220))

        self.milk_text = self.milk_font.render("milk", True, "black")
        screen.blit(self.milk_text, (Width // 2 - 380, Height // 2 - 190))  

        self.sell_button.draw(screen)

        if self.sell_button.input():
             
            if player.milk > 0:

                player.milk -= 1
                player.coins += 3
        
        self.exit_button.draw(screen)

        if self.exit_button.input():

            self.in_shop = False


# Initialize
pygame.init()


# Window
Width, Height = 1700, 800
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("StarNigga Slavery")
clock = pygame.time.Clock()
 

pygame.time.set_timer(1, 5000)


# Camera setup
camera_group = CameraGroup()


# World design
water = Water((1000, 300))

bridge = Bridge((1000, 300))

cow = Cow((300, 0))
milk_avaible_signal = Milk_Avaible_Signal((313, -53))

wheat = Wheat((100, 500))

shop = Shop((1400, 0), camera_group)

house = House((0, 0), camera_group, screen, Width, Height)

player = Player((100, 100), camera_group, screen, cow, shop, house, wheat)

no_clipable_sprites = [water, bridge, cow, wheat]
milk_signal_sprite = [milk_avaible_signal]


# Main loop
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
    
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_e:

                player.get_milk()
        
        if event.type == 1:

            cow.milk_avaible = True
            print("milk")

    clock.tick(60)
    
    screen.fill("#7CFC00")

    camera_group.update()
    camera_group.custom_draw(player)
    player.hud()
    house.upgrade()

    if shop.in_shop:

        shop.shop_menu()
        player.speed = 0
    
    else:

        player.speed = 3

    pygame.display.update()