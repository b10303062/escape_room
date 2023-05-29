import pygame as pg
import game
from game.engine import Engine
from game.room import Room
from game.item import Item
from game.exit import Exit
import random


def generate_room():
    a_exit = Exit()
    a_room = Room(a_exit)
    for i in range(random.randrange(1, 10)):
        a_item = Item()
        a_room.add_item(a_item)

    return a_room


# initialize the game
first_room = generate_room()
game_engine = Engine(first_room)
game_engine.set_active_sprites()

# game loop
game_on = True
while game_on is True:

    # Process player inputs
    for event in pg.event.get():
         if event.type == pg.QUIT:
             game_on = False

    # Do logical updates here.
    game_engine.active_sprites.update()

    # Fill the display with a solid color
    game_engine.screen.fill(game.SOLID_COLOR)

    # Render the graphics here.
    game_engine.active_sprites.draw(game_engine.screen)

    pg.display.flip()  # Refresh on-screen display
    game_engine.clock.tick(game.FPS)  # wait until next frame (at 60 FPS)

pg.quit()
