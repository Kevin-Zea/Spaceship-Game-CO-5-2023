import pygame
from game.components.spaceship import Spaceship
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, WHITE, CYAN
from game.components.enemys.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components import text_utils

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.isRunning = False
        self.bullet_handler = BulletHandler()
        self.player = Spaceship(self.bullet_handler)
        self.enemy_handler = EnemyHandler(self.bullet_handler)
        self.score = 0
        self.number_death = 0
        self.enemys_death = 0
        self.first = False
        self.shootTimes = 0
        self.timeSurvive = 0
        self.scores = []
        

    def run(self):
        # Game loop: events - update - draw
        # self.playing = True
        self.isRunning = True
        self.enemy_handler.iniciarEnemigos()
        while self.isRunning:
            self.events()
            self.draw()
            self.update()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
                self.playing = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                if self.first == True:
                    self.reset()
                self.first = True

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input)
            self.enemy_handler.update()
            self.bullet_handler.update(self.player)
            self.score = self.enemy_handler.numberEnemyDestroyer
            self.enemys_death = self.enemy_handler.enemistotal
            self.shootTimes = self.bullet_handler.bulletShoot
            self.tiempoSurvive()
            if not self.player.is_alive:
                self.scores.append(self.score)
                pygame.time.delay(500)
                self.playing = False
                self.number_death += 1

    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.drawScore()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
    
    def draw_menu(self):
        if self.number_death == 0:
            text, text_rect = text_utils.get_message("press ani key to start ", 30, WHITE, 550, 300)
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message("press ani key to start ", 30, WHITE, 550, 200)
            score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 20, WHITE, 550, 250)
            porcentajeEnemigosMuertos = (self.score * 100) / self.enemys_death
            enemysD, enemysD_rect = text_utils.get_message(f'% {porcentajeEnemigosMuertos} of enemys destroyed of {self.enemys_death}', 20 ,CYAN, 550, 300)
            shoots, shoot_rect = text_utils.get_message(f'Cantidad de veces en la que disparo {self.shootTimes}', 20, CYAN, 550, 350)
            tiempo, tiempo_rect = text_utils.get_message(f'your time of survive is: {self.timeSurvive}s', 20, CYAN, 550, 400)
            numeroIntentos, numeroIntentos_rect = text_utils.get_message(f'intents: {len(self.scores)}', 20, CYAN, 550, 420)

            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(enemysD, enemysD_rect)
            self.screen.blit(shoots, shoot_rect)
            self.screen.blit(tiempo, tiempo_rect)
            self.screen.blit(numeroIntentos, numeroIntentos_rect)

            i = 1
            heigth = 450
            self.scores = sorted(self.scores, reverse=True)
            for score in self.scores:
                point, point_rect = text_utils.get_message(f'{i}). {score} enemys destroyed', 20, CYAN, 550, heigth)
                i += 1
                heigth += 20
                self.screen.blit(point, point_rect)


    def reset(self):
        self.player.reset()
        self.bullet_handler.reset()
        self.enemy_handler.reset()
        self.score = 0
        self.enemys_death = 0
        self.timeSurvive = 0

    def drawScore(self):
        score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 20, WHITE, 1000, 40)
        tiempo, tiempo_rect = text_utils.get_message(f'your time of survive is: {self.timeSurvive}s', 20, CYAN, 950, 90)
        self.screen.blit(score, score_rect)
        self.screen.blit(tiempo, tiempo_rect)

    def tiempoSurvive(self):
        self.timeSurvive =+ pygame.time.get_ticks() // 1000