import pygame as pg
import game
from game.engine import Engine

# initialize the game
game_engine = Engine()

# game loop
game_on = True
while game_on is True:

    # Process player inputs
    for event in pg.event.get():
         if event.type == pg.QUIT:
             game_on = False

    # Do logical updates here.
    game_engine.player.update()

    # Fill the display with a solid color
    game_engine.screen.fill(game.SOLID_COLOR)

    # Render the graphics here.
    game_engine.screen.blit(game_engine.player.image, game_engine.player.rect)

    pg.display.flip()  # Refresh on-screen display
    game_engine.clock.tick(game.FPS)  # wait until next frame (at 60 FPS)

pg.quit()
