__author__ = 'angel'

import pygame
from src.sideButton import SideButton
from src.constants import Constants

rect = [0, Constants.TOP_MENU_HEIGHT, Constants.SIDE_MENU_WIDTH, Constants.SIDE_MENU_BUTTON_HEIGHT]

buttonGenericStyle = {
    'font': Constants.FONT,
    'fontSize': Constants.SIDE_MENU_FONT_SIZE,
    'fontColor': Constants.SIDE_MENU_FONT_COLOR,
    'backgroundColor': Constants.SIDE_MENU_COLOR,
    'backgroundHighlightColor': Constants.SIDE_MENU_BUTTON_HIGHLIGHT_COLOR,
    'leftMargin': Constants.SIDE_MENU_TEXT_LEFT_MARGIN,
    'rightMargin': Constants.SIDE_MENU_TEXT_RIGHT_MARGIN,
    'topMargin': Constants.SIDE_MENU_TEXT_TOP_MARGIN,
}

INDICATOR = '>'

class SideMenu(object):

    def __init__(self, style, itemsOrder, items):
        self.__buttons = []
        self.__views = []
        self.__index = 0
        self.__style = style
        for item in itemsOrder:
            buttonStyle = dict(buttonGenericStyle)
            buttonStyle['rect'] = pygame.Rect(rect)
            self.__buttons.append(SideButton(buttonStyle, item, INDICATOR))
            self.__views.append(items[item])
            rect[1] = rect[1] + rect[3]

    def __updateFocus(self, pos):
        if pos:
            for index, button in enumerate(self.__buttons):
                if button.isClicked(pos):
                    self.__index = index
                    break

    def draw(self, mainSurface, pos):
        self.__updateFocus(pos)
        pygame.draw.rect(mainSurface, self.__style['backgroundColor'], self.__style['rect'])

        #We draw the buttons
        for index, button in enumerate(self.__buttons):
            button.draw(mainSurface, index == self.__index)

        #We draw the selected view
        for index, view in enumerate(self.__views):
            view.draw(mainSurface, index == self.__index)