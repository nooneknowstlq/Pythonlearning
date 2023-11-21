class Rectangle:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def set_square(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            self.__x = x
            self.__y = y
        else:
            print("Нужно указать число")

    def get_square(self):
        return self.__x * self.__y

    def set_perimeter(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            self.__x = x
            self.__y = y
        else:
            print("Нужно указать число")

    def get_perimeter(self):
        return (self.__x + self.__y) * 2

    def set_hypotenuse(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            self.__x = x
            self.__y = y
        else:
            print("Нужно указать число")

    def get_hypotenuse(self):
        return (self.__x ** 2) + (self.__y ** 2)


p1 = Rectangle(3, 9)
p1.__x = 3
p1.__y = 9
p1.set_square(3, 9)
p1.set_perimeter(3, 9)
p1.set_hypotenuse(3, 9)

print("Длина прямоугольника:", p1.__x, "\nШирина прямоугольника:", p1.__y, "\nПлощадь прямоугольника:",
      p1.get_square(), "\nПериметр прямоугольника:", p1.get_perimeter(), "\nГипотенуза прямоугольника:",
      p1.get_hypotenuse())


