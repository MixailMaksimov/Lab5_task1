import math

class Circle:

    def __init__(self, name , radius, color ):
        self.__name = name
        self.__radius = radius
        self.__color = color

    def getCircleArea(self, radius):
        return math.ceil(math.pi * radius ** 2)

    def __repr__(self):
        print("Фигура: " + self.__name + \
              ", Цвет : " + str(self.__color) + \
              ", Площадь : " + str(self.getCircleArea(self.__radius)))
