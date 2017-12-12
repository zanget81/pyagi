__author__ = 'angel'

import pygame

class SideButton(object):

    def __init__(self, style, text, indicator):
        self.__style = style
        self.__text = text
        self.__indicator = indicator
        self.__myFont = pygame.font.SysFont(self.__style['font'], self.__style['fontSize'])

    def isClicked(self, pos):
        return self.__style['rect'].collidepoint(pos)

    def draw(self, mainSurface, highLight):
        pygame.draw.rect(mainSurface, self.__style['backgroundHighlightColor']  if highLight else self.__style['backgroundColor'], self.__style['rect'])
        option = self.__myFont.render(self.__text, True, self.__style['fontColor'])
        indicator = self.__myFont.render(self.__indicator, True, self.__style['fontColor'])

        mainSurface.blit(option,(self.__style['leftMargin'], self.__style['rect'][1] + self.__style['topMargin']))
        mainSurface.blit(indicator,( self.__style['rect'][2] - self.__style['rightMargin'], self.__style['rect'][1] + self.__style['topMargin']))
