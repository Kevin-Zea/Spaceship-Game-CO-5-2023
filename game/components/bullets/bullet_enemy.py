from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY, SHIELD_TYPE
import pygame

class BulletEnemy(Bullet):
    WIDTH = 15
    HEIGTH = 32
    SPEED = 20
    def __init__(self, center):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image, center)

    def update(self, player):
        self.rect.y += self.SPEED
        if self.rect.colliderect(player.rect) and player.power_type != SHIELD_TYPE:
            player.is_alive = False
        
        

    def draw(self, screen):
        return super().draw(screen)