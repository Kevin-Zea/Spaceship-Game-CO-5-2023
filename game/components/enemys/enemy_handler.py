from game.components.enemys.ship import Ship
from game.components.enemys.shipTwo import ShipTwo
from game.components.enemys.shipTree import ShipTree
from game.components.enemys.shipFour import ShipFour
from game.components.enemys.shipFive import ShipFive
from game.components.enemys.shipSix import ShipSix
from game.components.enemys.shipSeven import ShipSeven
import pygame


import random
class EnemyHandler:
    def __init__(self, bulletHandler, powerhandler):
        self.enemies = []
        self.bullet = bulletHandler
        self.numberEnemyDestroyer = 0
        self.enemistotal = 0
        self.powerhandler = powerhandler
        

    def update(self):
        for enemy in self.enemies:
            
            enemy.update(self.bullet, self.powerhandler)
            if enemy.isDestroyed:
                self.numberEnemyDestroyer += 1
            if enemy.is_alive == False:
                self.remove_enemy(enemy)
        
        if len(self.enemies) <= 2:
            self.add_enemy()

        tiempo = pygame.time.get_ticks() // 1000

        if tiempo % 60 == 0:
            self.add_enemy()

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        enemigoIdentidad = random.randint(1, 7)
        multiplicador = random.randint(1, 3)
        if enemigoIdentidad == 1:
            self.enemies.append(Ship(multiplicador))
        elif enemigoIdentidad == 2:
            self.enemies.append(ShipTwo(multiplicador))
        elif enemigoIdentidad == 3:
            self.enemies.append(ShipTree(multiplicador))
        elif enemigoIdentidad == 4:
            self.enemies.append(ShipFour(multiplicador))
        elif enemigoIdentidad == 5:
            self.enemies.append(ShipFive(multiplicador))
        elif enemigoIdentidad == 6:
            self.enemies.append(ShipSix(multiplicador))
        elif enemigoIdentidad == 7:
            self.enemies.append(ShipSeven(multiplicador))
        self.enemistotal += 1


    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
    
    def reset(self):
        self.enemies = []
        self.numberEnemyDestroyer = 0
        self.iniciarEnemigos()
    
    def iniciarEnemigos(self):
        i = 0
        while i <= random.randint(1, 10):
            self.add_enemy()
            i += 1
