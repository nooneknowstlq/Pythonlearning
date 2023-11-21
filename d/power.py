class Power:
    def __init__(self, output):
        self.output = output

    def __call__(self, func):
        def wrap(a, b):
            return func(a, b) ** self.output

        return wrap


@Power(3)
def mult(a, b):
    return a * b


result = mult(2, 2)
print("Результат:", result)
