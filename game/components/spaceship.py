import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_PLAYER_TYPE, DEFAULT_TYPE, SHIELD_TYPE, SHOOT_TYPE, COPLAYER_TYPE

class Spaceship:
    x_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    TIMEFROZE = 5
    POWER_LIMIT = 15
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
        self.shoot_sound = pygame.mixer.Sound('game/assets/sounds/shoot.mp3')

    def update(self, user_input):
        self.timefroze += 1
        if self.has_power:
            self.set_power()
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(self.bullethandler)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
        else:
            self.rect.x = SCREEN_WIDTH
    
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        else:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 60:
            self.rect.y += 10

    def shoot(self, bullethandler):
        if self.timefroze % self.TIMEFROZE == 0 and self.power_type == SHOOT_TYPE:
            bullethandler.add_bullet(SHOOT_TYPE, self.rect.center)
        if self.timefroze % self.TIMEFROZE == 0:
            bullethandler.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)
        self.shoot_sound.play()

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
        if self.power_type == SHIELD_TYPE or self.power_type == SHOOT_TYPE:
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
        
