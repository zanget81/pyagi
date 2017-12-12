__author__ = 'angel'

import pygame
from src.constants import Constants

class Tile(object):

    def __init__(self, style, titleText):
        self.__style = style
        self.__titleText = titleText
        self.__valueText = ''
        self.__myFont = pygame.font.SysFont(self.__style['font'], self.__style['fontSize'])

    def update(self, valueText):
        self.__valueText = str(valueText)

    def draw(self, mainSurface, visible):
        if visible:
            pygame.draw.rect(mainSurface, self.__style['backgroundColor'], self.__style['rect'])

            title = self.__myFont.render(self.__titleText, True, self.__style['fontColor'])
            value = self.__myFont.render(self.__valueText, True, self.__style['fontColor'])

            mainSurface.blit(title,(self.__style['rect'][Constants.X] + self.__style['leftMarginTitle'],
                                     self.__style['rect'][Constants.Y] + self.__style['topMarginTitle']))

            mainSurface.blit(value,(self.__style['rect'][Constants.X] + self.__style['leftMarginValue'],
                                    self.__style['rect'][Constants.Y] + self.__style['topMarginValue']))
