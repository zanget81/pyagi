__author__ = 'angel'

import pygame

from src.constants import Constants
from src.window import Window
from src.model import Model
from src.gerritRequester import GerritRequester
from src.config import Config

def main():

    my_clock = pygame.time.Clock()
    config = Config()

    """ Set up the game and run the main game loop """
    pygame.init()  # Prepare the pygame module for use
    mainWindow = Window(Model(GerritRequester(config)))

    # you have to call this at the start,
    pygame.font.init()

    while True:
        try:
            pos = 0

            ev = pygame.event.poll()    # Look for any event
            if ev.type == pygame.QUIT:  # Window close button clicked?
                break                   #   ... leave game loop
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                break

            # handle MOUSEBUTTONUP
            if ev.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

            mainWindow.updateWindow(pos)
            pygame.display.update()

            #force a constant frame rate of 60fps
            my_clock.tick(Constants.FRAME_RATE)
        except KeyboardInterrupt:
            break

    mainWindow.clean()
    pygame.quit()     # Once we leave the loop, close the window.

if __name__ == "__main__":
    main()
