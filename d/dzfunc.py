

def outer(a, b, c):
    def inner(x, y):
        return x * y

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s


print(outer(2, 4, 6))
