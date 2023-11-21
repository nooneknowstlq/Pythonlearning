class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Point3D(self.x / other.x, self.y / other.y, self.z / other.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.z}"


point1 = Point3D(12, 15, 18)
point2 = Point3D(6, 3, 9)

addition = point1 + point2
subtraction = point1 - point2
multiplication = point1 * point2
division = point1 / point2

print("Координаты 1-й точки:", repr(point1))
print("Координаты 2-й точки:", repr(point2))
print("Сложение координат:", addition)
print("Вычитание координат:", subtraction)
print("Умножение:", multiplication)
print("Деление:", division)
print("Равенство Координат:", point1 == point2)
print("x =", point1.x, "x1 =", point2.x)
print("y =", point1.y, "y1 =", point2.y)
print("x =", point1.z, "z1 =", point2.z)

point1.x = 20
print("Запись значения в координату x:", point1.x)
