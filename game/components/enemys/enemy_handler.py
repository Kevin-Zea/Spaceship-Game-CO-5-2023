from game.components.enemys.ship import Ship
from game.components.enemys.shipTwo import ShipTwo
import random
class EnemyHandler:
    enemigos = random.randint(1, 5) 
    def __init__(self):
        self.enemies = []
        for i in range(self.enemigos):
            multiplicador = random.randint(1, 3)
            self.enemies.append(Ship(multiplicador))
            self.enemies.append(ShipTwo(multiplicador))

    def update(self):
        for enemy in self.enemies:
            enemy.update()

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)