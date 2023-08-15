def avg(fn):
    def wrap(*args):
        a = ", ".join(map(str, args))
        print("Среднее арифметическое:", a, "=", fn(*args) / len(args))
    return wrap


@avg
def summa(*args):
    a = ""
    for i in args:
        a += str(i) + ", "
    print("Сумма чисел:", a[:-2], "=", sum(args))
    return sum(args)


summa(2, 3, 3, 4)
