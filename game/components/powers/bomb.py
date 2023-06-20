from game.components.powers.power import Power
from game.utils.constants import BOMB_POWER, BOMB_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH
import pygame

class Bomb(Power):

    def __init__(self):
        super().__init__(BOMB_POWER, BOMB_TYPE)
    
    def explosion(self):
        current = pygame.time.get_ticks()
        self.rect.y = (300)
        self.rect.x = (300)
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.rect = self.image.get_rect()
        if current % 3 == 0:
            self.delete()
    
    def delete(self):
        self.image = pygame.transform.scale(self.image, (0, 0))
        self.rect = self.image.get_rect()
