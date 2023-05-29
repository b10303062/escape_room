import pygame as pg
import random
import game

class Room(pg.sprite.Sprite):
    WIDTH = game.WIDTH
    HEIGHT = game.HEIGHT
    BASE_COLOR = "white"

    def __init__(self, exit):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((Room.WIDTH, Room.HEIGHT))
        self.image.fill(Room.BASE_COLOR)

        self.rect = self.image.get_rect()
        self.rect.centerx = game.WIDTH / 2
        self.rect.centery = game.HEIGHT / 2
        self.items = []
        self.exit = exit

    def add_item(self, item):
        self.items.append(item)
