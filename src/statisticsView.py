__author__ = 'angel'

import pygame
from src.constants import Constants
from src.plot import Plot

rectPlot = [0, Constants.TOP_MENU_HEIGHT, Constants.PLOT_WIDTH, Constants.PLOT_HEIGHT]

plotGenericStyle = {

}

class StatisticsView(object):

    def __init__(self, x, y, model):
        self.__x = x
        self.__y = y
        self.__model = model

        #Creating status plot widget
        rectPlot[Constants.X] = rectPlot[Constants.X] + self.__x + Constants.SIDE_MENU_TEXT_LEFT_MARGIN
        rectPlot[Constants.Y] = rectPlot[Constants.Y] + self.__y
        plotStatusStyle = dict(plotGenericStyle)
        plotStatusStyle['rect'] = pygame.Rect(rectPlot)

        self.__plotStatus = Plot(plotStatusStyle)

        # We get the initial data to populate the screen
        self.getData()

    def getData(self):
        self.__model.getLast7DaysPrs(self.update)

    def update(self, data):
        self.__plotStatus.update(data)

    def draw(self, mainSurface, visible):
        self.__plotStatus.draw(mainSurface, visible)

    def clean(self):
        self.__plotStatus.clean()
