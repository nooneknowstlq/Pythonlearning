
class NoneNegative:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.__name} должно быть положительным")
        instance.__dict__[self.__name] = value


class Order:
    price = NoneNegative()
    quantity = NoneNegative()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


apple_order = Order('apple', 5, 10)
print(apple_order.total())