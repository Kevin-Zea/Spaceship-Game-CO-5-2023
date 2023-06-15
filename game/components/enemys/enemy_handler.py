from game.components.enemys.ship import Ship
from game.components.enemys.shipTwo import ShipTwo

import random
class EnemyHandler:
    enemigos = random.randint(1, 5) 
    def __init__(self, bulletHandler):
        self.enemies = []
        self.bullet = bulletHandler

        for i in range(self.enemigos):
            multiplicador = random.randint(1, 3)
            self.enemies.append(Ship(multiplicador))
            self.enemies.append(ShipTwo(multiplicador))

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.bullet)
            if enemy.is_alive == False:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        enemigoIdentidad = random.randint(1, 2)
        multiplicador = random.randint(1, 3)

        if len(self.enemies) <= 2:
            if enemigoIdentidad == 1:
                self.enemies.append(Ship(multiplicador))
            else:
                self.enemies.append(ShipTwo(multiplicador))

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
