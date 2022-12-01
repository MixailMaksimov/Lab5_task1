from lab5.circle import *
from lab5.square import *

def main():
    rect = Rectangle("Прямоугольник", 10, 5, "Красный")
    circ = Circle("Круг", 10, "Зелёный")
    squ = Square("Квадрат", 5, 5, "Синий")
    rect.__repr__()
    circ.__repr__()
    squ.__repr__()

if __name__ == "__main__" :
    main()