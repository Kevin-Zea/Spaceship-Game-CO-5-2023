import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BACK = pygame.image.load(os.path.join(IMG_DIR, 'Other/fondo.jpeg'))
GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))



HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
BOMB_TYPE = 'bomb'
SHOOT_TYPE = 'treeshoot'
COPLAYER_TYPE = 'coplayer'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BOMB_POWER = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_4.png"))
SHOOT_POWER = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_5.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png"))
ENEMY_5 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_5.png"))
ENEMY_6 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_6.png"))
ENEMY_7 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_7.png"))

FONT_STYLE = 'freesansbold.ttf'

BULLET_ENEMY_TYPE = 'enemy'
BULLET_PLAYER_TYPE = 'player'

WHITE = (65, 7, 111)
CYAN = (21, 255, 182)