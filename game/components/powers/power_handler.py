from game.components.powers.shield import Shield
from game.components.powers.bomb import Bomb
from game.components.powers.treeShoot import TreeShoot
from game.components.powers.coplayer import Coplayer
from game.utils.constants import SPACESHIP_SHIELD, SCREEN_HEIGHT, SHIELD_TYPE, BOMB_TYPE, SHOOT_TYPE
import random
import pygame

class PowerHandler:

    def __init__(self):
        self.powers = []
        self.when_appears = random.randint(3, 7)
        self.identy_power = random.randint(1, 4)

    def generatePowers(self):

        if self.identy_power == 1:
            power = Shield()
            self.powers.append(power)
        elif self.identy_power == 2:
            bomb = Bomb()
            self.powers.append(bomb)
        elif self.identy_power == 3:
            shoot = TreeShoot()
            self.powers.append(shoot)
        elif self.identy_power == 4:
            coplayer = Coplayer()
            self.powers.append(coplayer)
        self.identy_power = random.randint(1, 4)
        self.when_appears = self.when_appears * 2
        


    def update (self, player):
        current_time = pygame.time.get_ticks() // 1000
        if current_time % self.when_appears == 0 and len(self.powers) <= 0:
            self.generatePowers()

        for power in self.powers:
            power.update()
            if player.rect.colliderect(power.rect):
                player.power_type = power.type
                player.has_power = True
                if power.type == SHIELD_TYPE:
                    player.set_power_image(SPACESHIP_SHIELD)
                elif power.type == BOMB_TYPE:
                    power.explosion()
                    self.powers.remove(power)
                else:
                    self.powers.remove(power)


            if power.rect.y >= SCREEN_HEIGHT:
                self.powers.remove(power)
            
            

    def draw(self, screen):
        for power in self.powers:
            power.draw(screen)
    
    def reset(self):
        self.when_appears = random.randint(3, 7)
        self.powers = []
    