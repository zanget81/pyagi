__author__ = 'angel'

from src.constants import Constants
import pygame
import matplotlib
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg
import pylab

class Plot(object):

    def __init__(self, style):
        self.__style = style
        # figsize in Inches
        # dpi 100 dots per inch

        w = self.__style['rect'][Constants.WIDTH]/Constants.DPI
        h = self.__style['rect'][Constants.HEIGHT]/Constants.DPI

        self.__fig = pylab.figure(figsize=[w, h], dpi=Constants.DPI)
        self.__raw_data = None
        self.__canva = None

    def update(self, data):
        self.__dataCreated = data['created']
        self.__dataMerged = data['merged']

        ax = self.__fig.gca()
        ax.plot(self.__dataCreated, label='created')
        ax.plot(self.__dataMerged, label='merged')
        pylab.legend(loc='upper left')

        self.__canvas = agg.FigureCanvasAgg(self.__fig)
        self.__canvas.draw()
        renderer = self.__canvas.get_renderer()
        self.__raw_data = renderer.tostring_rgb()

    def draw(self, mainSurface, visible):
        if visible and self.__raw_data:
            surf = pygame.image.fromstring(self.__raw_data, self.__canvas.get_width_height(), "RGB")
            mainSurface.blit(surf, (self.__style['rect'][Constants.X], self.__style['rect'][Constants.Y]))

    def clean(self):
        pass