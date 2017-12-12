import pygame
from src.constants import Constants
from src.sideMenu import SideMenu
from src.overviewView import OverviewView
from src.statisticsView import StatisticsView

sideMenuStyle = {
    'top': Constants.TOP_MENU_HEIGHT,
    'backgroundColor': Constants.SIDE_MENU_COLOR,
    'rect': pygame.Rect(0, Constants.TOP_MENU_HEIGHT, Constants.SIDE_MENU_WIDTH, Constants.WINDOW_HEIGHT - Constants.TOP_MENU_HEIGHT)
}

class Window(object):
    mainSurface = None
    internalModel = None
    views = None

    def __init__(self, modelInstance):
        #assign model
        self.internalModel = modelInstance

        self.internalModel.registerView('OVERVIEW', OverviewView(Constants.SIDE_MENU_WIDTH, Constants.TOP_MENU_HEIGHT, self.internalModel))
        self.internalModel.registerView('STATISTICS', StatisticsView(Constants.SIDE_MENU_WIDTH, Constants.TOP_MENU_HEIGHT, self.internalModel))

        self.views = self.internalModel.getViews()

        # Create surface of (width, height), and its window.
        self.mainSurface = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption(Constants.TITLE)

        #We create the side menu
        self.__sideMenu = SideMenu(sideMenuStyle, self.internalModel.getSideMenuOption(), self.views)

        pygame.mouse.set_visible(1)

        #getting model information
        #infoToDisplay = internalModel.getInfo()

    def draw(self):
        #Create top menu
        pygame.draw.rect(self.mainSurface, Constants.TOP_MENU_COLOR, pygame.Rect(0, 0, Constants.WIDTH, Constants.TOP_MENU_HEIGHT))

        #So first fill everything with the background color
        self.mainSurface.fill(Constants.BACKGROUND_COLOR)

    def updateWindow(self, pos):
        self.draw()
        self.__sideMenu.draw(self.mainSurface, pos)

    def clean(self):
        for index, item in enumerate(self.views):
            self.views[item].clean()
