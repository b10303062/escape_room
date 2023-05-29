import pygame as pg
import random
import game

class Exit(pg.sprite.Sprite):
    WIDTH = 50
    HEIGHT = 10
    BASE_COLOR = "green"

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((Exit.WIDTH, Exit.HEIGHT))
        self.image.fill(Exit.BASE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.centerx = game.WIDTH / 2
        self.rect.bottom = 0
