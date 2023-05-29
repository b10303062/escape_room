import pygame as pg
import os
from game.player import Player
from game.exit import Exit
from game.item import Item
from game.room import Room
import game


class Engine:
    # static variables
    def __init__(self, first_room):
        pg.init()
        self.screen = pg.display.set_mode((game.WIDTH, game.HEIGHT))
        pg.display.set_caption(game.TITLE)
        self.clock = pg.time.Clock()
        self.player = Player()
        self.exit = Exit()
        self.active_sprites = pg.sprite.Group()
        self.current_room = first_room

    def set_current_room(self, room):
        self.current_room = room

    def set_active_sprites(self):
        self.active_sprites.empty()
        self.active_sprites.add(self.player)
        self.active_sprites.add(self.current_room.items)
        self.active_sprites.add(self.current_room.exit)
