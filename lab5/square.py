from lab5.rectangle import *

class Square(Rectangle):


    def __init__(self,name, width, height, color):
        super().__init__(name, width, height, color)

    def getAreaSquare(self, width, height):
        return super().getArea(width, height)

    def repr(self):
        print("Фигура: " + self.__name + \
              " цвет : " + str(self.__color) + \
              " площадь : " + str(self.getAreaSquare(self.__width, self.__height)))
