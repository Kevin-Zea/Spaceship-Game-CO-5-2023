import pygame
import random

from game.components.enemys.enemy import Enemy
from game.utils.constants import ENEMY_1

class Ship(Enemy,):
    WIDTH = 40
    HEIGTH = 60

    def __init__(self, multiplicador):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, ((self.WIDTH * multiplicador), (self.HEIGTH * multiplicador)))
        super().__init__(self.image)