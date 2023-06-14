import random
from game.utils.constants import SCREEN_WIDTH

class Enemy:
    Y_POS = 20
    X_POS = [50, 10, 150, 200, 250, 300, 350, 400, 450, 500]
    SPEED_X = [1, 2, 3, 4, 5]
    SPEED_Y = [1, 2, 3, 4, 5]
    LEFT = 'left'
    RIGTH = 'rigth'
    MOV_X = [LEFT, RIGTH]
    INTERVAL = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
        self.index = 0
        self.vel_x = random.choice(self.SPEED_X)
        self.vel_y = random.choice(self.SPEED_Y)
        self.interval = random.choice(self.INTERVAL)

    def update(self):
        self.rect.y += self.vel_y
        if self.mov_x == self.LEFT:
            self.rect.x -= self.vel_x
            if self.index > self.interval or self.rect.x <= 0:
                self.mov_x = self.RIGTH
                self.index = 0
        else:
            self.rect.x += self.vel_x
            if self.index > self.interval or self.rect.x >= SCREEN_WIDTH - self.rect.width:
                self.mov_x = self.LEFT
                self.index = 0

        self.index += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)