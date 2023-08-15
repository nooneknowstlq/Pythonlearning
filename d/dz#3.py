# решение №1

num = int(input('Введите количество копеек (от 0 до 99): '))
if 0 <= num < 100:
    if (num == 1) or num in range(21, 92, 10):
        n = 1
        s = 'копейка'
    elif (2 <= num <= 4) or num in range(22, 93, 10) or num in range(23, 94, 10) or num in range(24, 95, 10):
        n = 1
        s = 'копейки'
    else:
        n = 1
        s = 'копеек'
else:
    n = 0
if n > 0:
    print(num, s)
else:
    print('Должно быть число от 0 до 99')


    решение №2
    def func(num):
        if num % 10 == 1 and num % 100 != 11:
            return f'{num} копейка'
        elif num % 10 in [2, 3, 4] and num % 100 not in [12, 13, 14]:
            return f'{num} копейки'
        else:
            return f'{num} копеек'


    print(func(int(input("введите число от 1 до 99: "))))
