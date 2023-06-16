from game.components.enemys.ship import Ship
from game.components.enemys.shipTwo import ShipTwo

import random
class EnemyHandler:
    def __init__(self, bulletHandler):
        self.enemies = []
        self.bullet = bulletHandler
        self.numberEnemyDestroyer = 0
        self.enemistotal = 0
        

    def update(self):
        for enemy in self.enemies:
            
            enemy.update(self.bullet)
            if enemy.isDestroyed:
                self.numberEnemyDestroyer += 1
            if enemy.is_alive == False:
                self.remove_enemy(enemy)
        
        if len(self.enemies) <= 2:
            self.add_enemy()

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        enemigoIdentidad = random.randint(1, 2)
        multiplicador = random.randint(1, 3)
        if enemigoIdentidad == 1:
            self.enemies.append(Ship(multiplicador))
        else:
            self.enemies.append(ShipTwo(multiplicador))
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
