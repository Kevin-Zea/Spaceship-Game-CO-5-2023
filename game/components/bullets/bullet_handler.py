from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_PLAYER_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_player import BulletPlayer

class BulletHandler:
    def __init__(self):
        self.bullets = []
        self.bulletsPlayer = []
        self.bulletShoot = 0

    def update(self, player):
        for bullet in self.bullets:
            bullet.update(player)
            if not bullet.is_alive:
                self.removeBullet(bullet)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
    
    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            obj = BulletEnemy(center)
            self.bullets.append(obj)
        elif type == BULLET_PLAYER_TYPE:
            objPlayer = BulletPlayer(center)
            self.bullets.append(objPlayer)
            self.bulletsPlayer.append(objPlayer)
            self.bulletShoot += 1
    def removeBullet(self, b):
        self.bullets.remove(b)
        self.bulletsPlayer.remove(b)

    def reset(self):
        self.bullets = []
        self.bulletsPlayer = []
        self.bulletShoot = 0
    
