
class Power:
    def __init__(self, func):
        self.func = func

    def __call__(self, x, y):
        return self.func(x, y) ** 2


@Power
def mult(a, b):
    return a * b


print(mult(2, 3))

class Decor:
    def __init__(self, string):
        self.string = string

    def __call__(self, func):
        def wrap(x, y):
            print("*" * 20)
            print(self.string, end=" ")
            func(x, y)
            print("=" * 20)

        return wrap


@Decor("Значения:")
def add(a, b):
    print(a, b)


add(2, 5)