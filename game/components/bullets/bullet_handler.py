from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_PLAYER_TYPE, SHOOT_TYPE
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
        elif type == SHOOT_TYPE:
            objPlayer = BulletPlayer(center)
            center2 = (center[0] - 50, center[1])
            center3 = (center[0] + 50, center[1])
            objPlayer2 = BulletPlayer(center2)
            objPlayer3 = BulletPlayer(center3)
            self.bullets.append(objPlayer)
            self.bullets.append(objPlayer2)
            self.bullets.append(objPlayer3)
            self.bulletsPlayer.append(objPlayer)
            self.bulletsPlayer.append(objPlayer2)
            self.bulletsPlayer.append(objPlayer3)
            self.bulletShoot += 3

            
    def removeBullet(self, b):
        self.bullets.remove(b)
        self.bulletsPlayer.remove(b)

    def reset(self):
        self.bullets = []
        self.bulletsPlayer = []
        self.bulletShoot = 0
    
