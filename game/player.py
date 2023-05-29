import pygame as pg
import game

class Player(pg.sprite.Sprite):
    WIDTH = 50
    HEIGHT = 50
    BASE_COLOR = "black"
    SPEED = 8

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((Player.WIDTH, Player.HEIGHT))
        self.image.fill(Player.BASE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.centerx = game.WIDTH / 2
        self.rect.bottom = game.HEIGHT - 10

    def update(self):
        key_pressed = pg.key.get_pressed()  # return a dict of boolian values
        if key_pressed[pg.K_d]:
            self.rect.x += Player.SPEED
        if key_pressed[pg.K_a]:
            self.rect.x -= Player.SPEED
        if key_pressed[pg.K_s]:
            self.rect.y += Player.SPEED
        if key_pressed[pg.K_w]:
            self.rect.y -= Player.SPEED

        if self.rect.right > game.WIDTH:
            self.rect.right = game.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > game.HEIGHT:
            self.rect.bottom = game.HEIGHT
