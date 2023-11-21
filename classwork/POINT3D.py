
class Integer:
    @staticmethod
    def verify_coord(coord):
        if not isinstance(coord, int):
            raise TypeError(f"Координата {coord} должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        instance.__dict__[self.name] = value


class Point3d:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p1 = Point3d(1, 2, 3)
print(p1.z)
p1.z = 5
print(p1.__dict__)


