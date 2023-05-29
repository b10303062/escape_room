import pygame as pg
import os
from game.player import Player
import game

class Engine:
    # static variables
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((game.WIDTH, game.HEIGHT))
        pg.display.set_caption(game.TITLE)
        self.clock = pg.time.Clock()
        self.player = Player()

