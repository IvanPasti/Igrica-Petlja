import pygame


# Initialize
pygame.init()


# Window
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Igrica")


# Clock
clock = pygame.time.Clock()
delta_time = clock.tick(60) / 1000


# Player
class Player:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.velocity = 50

        self.direction = "down"

        self.idle_woman_down = pygame.image.load("Igrica/Assets/Character/Woman/Woman_Idle.PNG")
        self.idle_woman_down = pygame.transform.scale(self.idle_woman_down, (45, 55))
        
        self.idle_woman_up = pygame.image.load("Igrica/Assets/Character/Woman/Woman_idle_up.PNG")
        self.idle_woman_up = pygame.transform.scale(self.idle_woman_up, (45, 55))

        self.idle_woman_right = pygame.image.load("Igrica/Assets/Character/Woman/Woman_idle_right.PNG")
        self.idle_woman_right = pygame.transform.scale(self.idle_woman_right, (40, 55))

        self.idle_woman_left = pygame.image.load("Igrica/Assets/Character/Woman/Woman_idle_left.PNG")
        self.idle_woman_left = pygame.transform.scale(self.idle_woman_left, (40, 55))

    def draw(self):

        if self.direction is "up":

            screen.blit(self.idle_woman_up, (self.x, self.y))

        elif self.direction is "down":

            screen.blit(self.idle_woman_down, (self.x, self.y))
        
        elif self.direction is "left":

            screen.blit(self.idle_woman_left, (self.x, self.y))

        elif self.direction is "right":

            screen.blit(self.idle_woman_right, (self.x, self.y))


player = Player(275, 275)


# House
class House:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.house_image_level_1 = pygame.image.load("Igrica/Assets/House/Level 1/HOUSE 1 - DAY.png")
        self.house_image_level_1 = pygame.transform.scale(self.house_image_level_1, (250, 250))

    def draw(self):

        screen.blit(self.house_image_level_1, (self.x, self.y))

house = House(300, 30)    


# Water
class Water:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.water_image = pygame.image.load("Igrica/Assets/Water/WATER TILE - DAY.png")
        self.water_image = pygame.transform.scale(self.water_image, (190, 800))

        self.water_detail_rock_1 = pygame.image.load("Igrica/Assets/Water/WATER DETAIL 1 - DAY.png")
        self.water_detail_rock_1 = pygame.transform.scale(self.water_detail_rock_1, (30, 30))
        
        self.water_detail_rock_2 = pygame.image.load("Igrica/Assets/Water/WATER DETAIL 2 - DAY.png")
        self.water_detail_rock_2 = pygame.transform.scale(self.water_detail_rock_2, (30, 30))
    
        self.water_detail_leaf = pygame.image.load("Igrica/Assets/Water/WATER DETAIL 5 - DAY.png")
        self.water_detail_leaf = pygame.transform.scale(self.water_detail_rock_2, (30, 30))


    def draw(self):

        screen.blit(self.water_image, (self.x, self.y))

water = Water(810, 0)


# Bridge
class Bridge:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.bridge_image = pygame.image.load("Igrica/Assets/Bridge/BRIDGE - DAY.png")
        self.bridge_image = pygame.transform.scale(self.bridge_image, (450, 150))

    def draw(self):

        screen.blit(self.bridge_image, (self.x, self.y))

bridge = Bridge(780, 300)


# Grass
class Grass:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.grass_image = pygame.image.load("Igrica/Assets/Grass/GRASS TILE - DAY.png")
        self.grass_image = pygame.transform.scale(self.grass_image, (890, 800))

    def draw(self):

        screen.blit(self.grass_image, (self.x, self.y))

grass = Grass(0, 0)


# Barn
class Barn:

    def __init__(self):

        self.is_open = True

        self.fence_horizontal_image = pygame.image.load("Igrica/Assets/Fence/FENCE horizontal.png")
        self.fence_horizontal_image = pygame.transform.scale(self.fence_horizontal_image, (80, 50))

        self.fence_vertical_image = pygame.image.load("Igrica/Assets/Fence/Fence vertical.PNG")
        self.fence_vertical_image = pygame.transform.scale(self.fence_vertical_image, (23, 100))

        self.fence_door_open_image = pygame.image.load("Igrica/Assets/Fence/Fence door open.PNG")
        self.fence_door_open_image = pygame.transform.scale(self.fence_door_open_image, (80, 50))

        self.fence_door_closed_image = pygame.image.load("Igrica/Assets/Fence/Fence door closed.PNG")
        self.fence_door_closed_image = pygame.transform.scale(self.fence_door_closed_image, (80, 50))

    def draw(self):

        screen.blit(self.fence_horizontal_image, (670, 700))
        screen.blit(self.fence_horizontal_image, (590, 700))
        screen.blit(self.fence_horizontal_image, (510, 700))
        screen.blit(self.fence_horizontal_image, (430, 700))

        screen.blit(self.fence_vertical_image, (430, 600))
        screen.blit(self.fence_vertical_image, (430, 500))

        screen.blit(self.fence_vertical_image, (730, 600))
        screen.blit(self.fence_vertical_image, (730, 500))

        screen.blit(self.fence_horizontal_image, (670, 450))
        screen.blit(self.fence_horizontal_image, (510, 450))
        screen.blit(self.fence_horizontal_image, (430, 450))

        if self.is_open is False:

            screen.blit(self.fence_door_closed_image, (590, 450))
        
        else:

            screen.blit(self.fence_door_open_image, (590, 450))


barn = Barn()



# Main loop
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    # Input  
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] or keys[pygame.K_UP]:

        player.y -= player.velocity * delta_time

        player.direction = "up"

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:

        player.y += player.velocity * delta_time

        player.direction = "down"

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:

        player.x -= player.velocity * delta_time

        player.direction = "left"
    
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:

        player.x += player.velocity * delta_time

        player.direction = "right"

    # Render on screen
    screen.fill("green")

    grass.draw()

    house.draw()

    water.draw()

    bridge.draw()

    barn.draw()

    player.draw()

    pygame.display.update()