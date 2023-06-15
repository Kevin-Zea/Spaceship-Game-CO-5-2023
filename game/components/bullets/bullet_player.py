from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET
import pygame

class BulletPlayer(Bullet):
    WIDTH = 15
    HEIGTH = 32
    SPEED = 20
    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image, center)
    
    def update(self, enemy):
        self.rect.y -= self.SPEED
        # if self.rect.colliderect(enemy.rect):
        #     enemy.is_alive = False

    def draw(self, screen):
        return super().draw(screen)