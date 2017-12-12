__author__ = 'angel'

import pygame
from src.tile import Tile
from src.constants import Constants

NUMBER_OF_TILES = 1

rect = [0, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT]

tileGenericStyle = {
    'font': Constants.FONT,
    'fontSize': Constants.SIDE_MENU_FONT_SIZE,
    'fontColor': Constants.TILE_FONT_COLOR,
    'backgroundColor': Constants.TILE_COLOR
    }

tilesTitles = ['PRs OPEN']

tilesProperties = {
    'PRs OPEN' : {
        'leftMarginTitle': 20,
        'topMarginTitle': 5,
        'leftMarginValue': 20,
        'topMarginValue': 35
    }
}

class OverviewView(object):

    def __init__(self, x, y, model):
        self.__x = x
        self.__y = y
        self.__tiles = []
        self.__model = model

        rect[Constants.X] = rect[Constants.X] + self.__x + Constants.SIDE_MENU_TEXT_LEFT_MARGIN
        rect[Constants.Y] = rect[Constants.Y] + self.__y

        for x in range(0, NUMBER_OF_TILES):
            tileStyle = dict(tileGenericStyle)

            if tilesTitles[x] in tilesProperties:
                tileStyle.update(tilesProperties[tilesTitles[x]])

            tileStyle['rect'] = pygame.Rect(rect)
            self.__tiles.append(Tile(tileStyle, tilesTitles[x]))

        # We get the initial data to populate the screen
        self.getData()

    def getData(self):
        self.__model.getTotalOpenPrs(self.update)

    def update(self, data):
        for index, tile in enumerate(self.__tiles):
            tile.update(data)

    def draw(self, mainSurface, visible):
        for index, tile in enumerate(self.__tiles):
            tile.draw(mainSurface, visible)

    def clean(self):
        pass
