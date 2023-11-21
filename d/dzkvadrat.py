from math import pi


class Table:
    def __init__(self, width=None, length=None, radius=None):
        if radius is None:
            self._width = width
            self._length = length
        else:
            self.radius = radius

    def calc_area(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")


class SqTable(Table):
    def calc_area(self):
        return self._width * self._length


class RoundTable(Table):
    def calc_area(self):
        return round(pi * self.radius ** 2, 2)


t = SqTable(10, 20)
print(t.__dict__)
print(t.calc_area())


t1 = RoundTable(radius=20)
print(t1.__dict__)
print(t1.calc_area())
