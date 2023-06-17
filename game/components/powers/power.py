import pygame
import random
from game.utils.constants import SCREEN_WIDTH

class Power:
    WIDTH = 30
    HEIGTH = 30
    POWER_SPEED = 10
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, SCREEN_WIDTH - 50)
        self.rect.y = 0
        self.is_alive = True

    def update(self):
        self.rect.y += self.POWER_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)