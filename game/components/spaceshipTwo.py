import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_PLAYER_TYPE, DEFAULT_TYPE, SHIELD_TYPE, SHOOT_TYPE, COPLAYER_TYPE
import random

class SpaceshipTwo:
    x_POS = (SCREEN_WIDTH // 2) - 90
    Y_POS = 500
    TIMEFROZE = 5
    POWER_LIMIT = 15
    SPEED_X = [1, 2, 3, 4, 5]
    SPEED_Y = [1, 2, 3, 4, 5]
    LEFT = 'left'
    RIGTH = 'rigth'
    MOV_X = [LEFT, RIGTH]
    SHOOTING_TIME = 30
    INTERVAL = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
    def __init__(self, bulletHandler):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.x_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.bullethandler = bulletHandler
        self.timefroze = 0
        self.power_type = DEFAULT_TYPE
        self.has_power = False
        self.power_time = 0
        self.time = 0

        self.mov_x = random.choice(self.MOV_X)
        self.index = 0
        self.vel_x = random.choice(self.SPEED_X)
        self.vel_y = random.choice(self.SPEED_Y)
        self.interval = random.choice(self.INTERVAL)

    def update(self, user_input):
        self.timefroze += 1
        self.move()
        if self.has_power:
            self.set_power()

        self.shoot(self.bullethandler)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def shoot(self, bullethandler):
        if self.timefroze % self.TIMEFROZE == 0 and self.power_type == DEFAULT_TYPE:
            bullethandler.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)
        elif self.timefroze % self.TIMEFROZE == 0 and self.power_type == SHOOT_TYPE:
            bullethandler.add_bullet(SHOOT_TYPE, self.rect.center)

    def reset(self):
        self.rect.x = self.x_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.set_default_image()
        self.time = 0
        self.power_time = 0
        self.has_power = False
        self.power_type = DEFAULT_TYPE

    def set_power_image(self, image):
        self.image = image
        self.image = pygame.transform.scale(self.image, (40, 60))

    def set_default_image(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
    
    def set_power(self):
        if self.power_type == SHIELD_TYPE or self.power_type == SHOOT_TYPE or self.power_type == COPLAYER_TYPE:
            self.time += 1
            if self.time == 20:
                self.time = self.time // 20
                self.power_time += self.time
            if self.power_time == 15:
                self.set_default_image()
                self.power_time = 0
                self.time = 0
                self.has_power = False
                self.power_type = DEFAULT_TYPE
    
    def move(self):
        if self.mov_x == self.LEFT:
            self.rect.x -= self.vel_x
            if self.index > self.interval or self.rect.x <= 0:
                self.mov_x = self.RIGTH
                self.index = 0
        else:
            self.rect.x += self.vel_x
            if self.index > self.interval or self.rect.x >= SCREEN_WIDTH - self.rect.width:
                self.mov_x = self.LEFT
                self.index = 0

        self.index += 1

        
