import pygame as pg
import random
import game

class Item(pg.sprite.Sprite):
    WIDTH = 30
    HEIGHT = 40
    BASE_COLOR = "white"

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((Item.WIDTH, Item.HEIGHT))
        self.image.fill(Item.BASE_COLOR)
        self.rect = self.image.get_rect()
        self.set_xy()

    def set_xy(self):
        self.rect.x = random.randrange(0, (game.WIDTH - self.rect.width))
        self.rect.y = random.randrange(0, (game.HEIGHT - self.rect.height))

