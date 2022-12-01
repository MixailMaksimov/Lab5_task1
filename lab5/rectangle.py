class Rectangle:
    def __init__(self,name, width, height, color ):
        self.__name = name
        self.__width = width
        self.__height = height
        self.__color = color

    def getArea(self, width, height):
        return width * height

    def __repr__(self):
        print("Фигура: " + str(self.__name) + \
              ", Цвет : " + str(self.__color) + \
              ", Площадь : " + str(self.getArea(self.__width, self.__height)))