__author__ = 'angel'

class Label(object):

    def __init__(self, style):
        self.__style = style


    def draw(self, mainSurface, visible):
        if visible:
            option = self.__myFont.render(self.__text, True, self.__style['fontColor'])
            mainSurface.blit(option,(self.__style['leftMargin'], self.__style['rect'][1] + self.__style['topMargin']))