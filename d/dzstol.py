class Table:
    def __init__(self):
        self.__width = 0
        self.__length = 0
        self.__height = 0
        self.__radius = 0

    def get_width(self):
        return self.__width

    def set_width(self, value):
        if value > 0:
            self.__width = value

    def get_length(self):
        return self.__length

    def set_length(self, value):
        if value > 0:
            self.__length = value

    def get_height(self):
        return self.__height

    def set_height(self, value):
        if value > 0:
            self.__height = value

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius


table = Table()
table.set_width(200)
table.set_length(400)
table.set_height(75)
table.set_radius(20)
print(table.get_width())
print(table.get_length())
print(table.get_height())
print(table.get_radius())