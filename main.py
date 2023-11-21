# name = 'tlq'   имя
# print("hello,",name)
# age = 28
# print(age)
# a = 5
# print(a)
# print(id(a))
# print(type(a))
# a = "hello world"
# print(a)
# print(id(a))
# print(type(a))
# import math
# import re
# import sys

# a = b = c = 1
# print(a, b, c)

# a, b, c = "hello", 5, 9.2
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 1
# b = 2
# print("a:", a)
# print ("b:", b)
#
# c = a # 1
# a = b # 2
# b = c # 1
# print("a:", a)
# print("b:", b)

# print("строка")
# print('строка')

# a = 5
# b = 7
# c = 3
# r = a + b + c
# print('сумма', r)
# print('произведение', a * b * c)
# print('среднее орифметическое', r / 3)

# num = 4321
# a = num % 10
# print(a)
# num = num // 10
# print(num)
# b = num % 10
# print(b)
# num = num // 10

# a = 10
# b = 5
# print("a:", a)
# print("b:", b)
# a = a // b ** a
# print("A:", a)
# b += a * b
# print("B:", b)
# # либо b = a + b


# num1 = "5.2"
# num2 = 10
# print(type(num1))
# print(type(num2))
# res = float(num1) + num2
# print(res)

# name = "валера"
# age = 18
#
#
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print()
# print("Меня зовут", name, ". Мне", age, "лет.", sep=" ", end="\n\n")
# print("продолжение строки.")

# name = input("введите имя: ")
# print("hello", name,)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print(res)

# a = int(input("введите число: "))
# b = int(input("введите число: "))
# c = int(input("введите число: "))
# d = int(input("введите число: "))
#
# sum1 = a + b
# sum2 = c + d
#
# res = sum1 / sum2
# print(round(res, 2))

# b1 = True    # 1
# b2 = False    # 1
# print(b1 + 5)
# print(b2 + 5)
# print(type(b1))

# False = "", 0, False, None
# print(bool("python"))
# print(bool(""))    # False
# print(bool(112341))
# print(bool(False))
# print(bool(None))

# a = None
# print(a)
# print(a is None)
# a = 5
# print(a)
#
# print(5 > 2)
# print("привет" > "ПРИВЕТ")

# print(2 < 4 < 9)    # True True
# print(3 * 3 <= 7 >= 2)      # False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)      # 10 5 False


# && - and
# || - or
# ! - not

# print(5 - 3 == 2 and 1 + 3 == 4)    # True True
# print(5 - 3 == 2 or 1 + 3 == 4)     # True True

# print(not 9 - 9)        # True
# print(not 9-5)      # False

# cnt = 5
# if cnt < 10:
#     cnt += 1
#     print(cnt)


# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")


# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")


# a = int(input("введите первую сторону треугольника "))
# b = int(input("введите вторую сторону треугольника "))
# c = int(input("введите третью сторону треугольника "))
# if a > b < c:
#     print("равносторонний треугольник ")
# elif a == b or a == c or b == c:
#     print("равнобедренный треугольник ")
# else:
#     print("разносторонний треугольник ")


# day = int(input("Введите день недели цифрой: "))
# if 1 <= day <= 5:  # if (day >= 1) and (day <= 5):
#     print("это будний дни - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if "четверг"
#         if day == 5:
#             print("пятница")
# elif day == 6 or day == 7:
#     print("выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("такого дня недели не существует")


# res = int(input("введите номер месяца: "))
# if 12 or 1 or 2:
#     print("это зима - ", end="")
#     if res == 12:
#         print("декабрь")
#     if res == 1:
#         print("январь")
#     if res == 2:
#         print("февраль")
# elif day == 6 or day == 7:
#     print("выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("такого дня недели не существует")


# month = int(input("Введите номер месяца: "))
# if month == 1 or month == 2 or month == 12:
#     print("Зима")
# elif month == 3 or month == 4 or month == 5:
#     print("Весна")
# elif month == 6 or month == 7 or month == 8:
#     print("Лето")
# elif month == 9 or month == 10 or month == 11:
#     print("Осень")
# else:
#     print("Ошибка ввода данных")

#
# n = int(input("введите количество ворон от 0 до 9"))
# if 0 <= n <= 9:
#     print("на ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <=4:
#         print(n, "вороны")
#     else
#         print(n, "ворон")
# else:
#     print("ошибка ввода данных")

# day = 'понедельник'
# time = 17
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("выходной день")
#     case _:
#         print("такого дня недели не существует или не рабочее время")


# тернарные выражения

# a, b = 10, 20
# minim = a if a<b else b
# print(minim)

# a, b = 30, 30
# print("a == b" if a == b else "a > b" if a > b else "b > a")
#
# a, b = 30, 10
# print("a == b" if a == b else "a > b" if a > b else "b > a")
#
# a, b = 10, 30
# print("a == b" if a ==

# a, b = 30, 0
# print("на 0 делить нельзя" if b == 0 else a / b)


# try:    # попытаться
#     n = int(input("Введите целове число: "))
#     print(n * 2)
# except ValueError:      # исключение
#     print("что-то пошло не так")

# try:
#     n = int(input("введите делимое: "))
#     m = int(input("введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("нельзя вводить строки.")
# except ZeroDivisionError:
#     print("нельзя делить на ноль.")
# else:   # отработает если в блоке try не сработало усключение
#     print("Все в порядке, вы ввели числа", n, "и", m)
# finally:    # выводится в любом случае
#     print("конец программы")

#     n = input("введите первое число: ")
#     m = input("введите второе число: ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# итерация - один шаг цикла

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# n = int(input("укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1
# while n > 0:
#     print("*", end="")
#     n -= 1
# print("*" * n)

# a = int(input("введите начало диапазона: "))
# b = int(input("введите конец диапазона: "))
# res = 0
# while a <= b:   # 1 3 5
#     if a % 2:  # a % 2 != 0; a % 2 == 1;
#         res += a    # res + a
#     a += 1
# print("сумма целых нечетных чисел:", res)

# n = input("введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("введите целое число")
# if n % 2 == 0: print("четное")
# else:
#     print("нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# res = 1
# while True:
#     n = int(input("введите число: "))
#     if n == 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("цикл окончен, i =", i)

# for element in range(start, stop, step):

# for i in range(5, 10, 15):
#     print(i, end=" ")
#
# i = 5
# while i < 100:
#     print(i, end=" ")
#     i += 10


# остаток от деления
# a = int(input("введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")


# a = int(input("введите число от 10 до 100: "))
# for i in range(11, 100, 11):
#     print(i, end=" ")

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("DOne!")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("---")


# i = 1
# while i <= 5:
#     j = 1
#     while j <= 16:
#         if j % 2:
#             print("+", end=" ")
#         else:
# w = int(input("введите ширину прямоугольника: "))
# h = int(input("введите высоту прямоугольника: "))
# for i in range(h):                  # I - СТРОКА
#     for j in range(w):              # J - СТОЛБИК
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# a = [letter for letter in "hello"]
# print(a)

# num = [i for i in range(20) if i % 2 == 0]
# print(num)

# СПИСОК (List)
# nums = [8, 3, 4, 1, 9, "hello", 2.5]
# print(nums)
# print(type(nums))
# print(nums[0])
# print(nums[-1])
# print(nums[6])
# nums[3] = 256
# print(nums[3])
# nums[0] += 100
# print(nums)
#
# print(len(nums))

# s = []
# print(s)
# print(type(s))
#
# b = list('hello')
# print(b)
# print(type(b))

# n = list(range(2,10, 3))
# print(n)

# a = [0 for i in range(5)]
# print(a)
# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# a = [i * 3 for i in 'list']
# print(a)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = c * 3
# print(d)


# a = [0] * int(input("введите количество элементов в списке: "))
# # print(a)     # [0, 0, 0]
# for i in range(len(a)):
#     a[i] = input("==>>   ")
# print(a)


# a = [int(input("-->")) for i in range(int(input("введите количество элементов в списке: ")))]
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n =")))]

# a = ['один', 'два', 'три', 'четыре', 'пять']
# for i in range(len(a)):     # 0 1 2 3 4 (индексы)
#     print(a[i], end=" ")
# print()
# for el in a:    # 'один', 'два', 'три', 'четыре', 'пять' (доступ не к индексу)
#     print(el, end=" ")


# a = [int(input("-> ")) for i in range(int(input("n =")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]

# for i in a:
#     if i < 0:
#         s += i
# print("сумма отрицательных элементов: ", s)
#
# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]

# for i in range(len(n)):
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
# print("количество четных элементов: ", k)
# print("сумма нечетных элементов ", s)
#
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
# #     if a[i] > a[i - 1]:
# #         print(a[i], end=" ")

# for i in a:
#     if i > i - 1:
#         print(i, end=" ")

# import math
#
#
# num1 = math.sqrt(4)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# num4 = math.pi
# print(num1)
# print(num2)
# print(num3)
# print(num4)

# import math as
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
#
# print(num2)
# print(num3)

# from math import ceil, floor
#
# num2 = ceil(3.2)
# num3 = floor(5.8)
#
# print(num2)
# print(num3)

# from math import *
#
# num2 = ceil(3.2)
# num3 = floor(5.8)
#
# print(num2)
# print(num3)

# import math
# dir(math)

# import time
# sec = time.time()
# print(sec)

# import time

# sec = time.time()
# print(sec)
# locale = time.ctime()
# print(locale)
# res = time.localtime()
# print(res)
# print(res.tm_year)
# print(res.tm_mon)

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Сегодня %B %d, %Y"))
# print(time.strftime("%d/%m/%Y, %H:%M:%S"))
# print("запуск программы...")
# time.sleep(5)
# print("программа завершилась")

# start = time.time()
# time.sleep(5)
# finish = time.time()
# print("время выполнения программы", finish - start, "секунд")

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# print("время выполнения программы", finish - start, "секунд")

# Срезы: список[start:stop:step]
# s = [5, 9, 3, 7, 1, 8]
# a = s[4:0:-1]
# print(a)

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[6:7])
# print(s[3:4])
# print(s[4:7])
# print(s[4:1:-1])
# print(s[2:5])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[3:5] = []
# print(s)
# del s[:]
# print(s)

# Методы списков

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s.append(99)  # добавляет в конец списка элемент
# print(s)
# s.extend([8, 9, 10])  # добавляет несколько элементов в конец списка
# print(s)
# s.extend("add")  # добавляет в список набор элементов
# print(s)
# s.insert(0, 100)    # добавляет в начало списка по номеру индекса
# print(s)
# s.insert(5, 100)    # добавляет по номеру индекса элемент
# print(s)

# s = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("введите число: "))
#     s.insert(0, x)
# print(s)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# s = []
# n = int(input("количество элементов': "))
# for num in range(n):
#     x = int(input("введите число: "))
#     if x % 3 ==0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
#
# print(c)    # [2, 1, 4, 3]

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
#     print(c)
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
#     print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)

# s = [4, 0, 2, 0, 3, 6, 0, 0, 7]
# s.remove(0)     # удаляет первый найденный элемент из списка по заданному значению
# print(s)
# last = s.pop()      # удаляет последний элемент из списка(если не указывать в скобках)и так же может его вернуть
# print(last)
# print(s)
#
# last = s.pop(0)    # удаляет по индексу элемента
# print(last)
# print(s)
#
# s.clear()       # очищает список
# print(s)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# print("Введите индекс: ")
# k = int(input("k = "))
# a.pop(k)
# print(a)


# s = [4, 0, 2, 0, 3, 6, 0, 0, 7]
# print(s)
# num = s.count(5)    # считает количество заданных элементов
# print(num)
# ind = s.index(3)    # возвращает индекс первого найденного элемента по его значению, если значение нет то получим Value Error
# print(ind)

# a = [1, 2, 3]
# b = a.copy()
# print("a =", a, id(a))
# print("b =", b, id(b))
# a.append(20)
# print("a =", a, id(a))
# print("b =", b, id(b))
# b.append(30)
# print("a =", a, id(a))
# print("b =", b, id(b))

# a = [1, 2, 3]     разворачивает элементы в обратную сторону
# a.reverse()
# print(a)

# s = [9, 7, 3, 4, 5, 2]
# s.sort()    # сортирует по возрастанию
# print(s)
# s.sort(reverse=True)    # сортирует по убыванию
# print(s)

# s2 = ["Виталя", "Серега", "Гришаня", "Валёк"]
# s2.sort(key=len)    # считает по длине строки(имени)
# print(s2)

# s = [9, 7, 3, 4, 5, 2]
# s.sort()    # возвращает исходный исписок и ничего не возвращает
# print(s)
#
# s2 = [9, 7, 3, 4, 5, 2]
# s3 = sorted(s2)     # sorted - возвращает новый список . Может работать и со списками и с другими типами данных
# print(s3)
# print(s2)

# Генерация случайных данных

# import random
# print(random.random())
# print(random.randint(5, 9))     # random от 5 до 9 включительно
# print(random.randrange(1, 9, 2))    # random start stop step ( начальный диапазон, конечный диапазон(не входит в диапазон), шаг)

# from random import *
# print(random())
# print(randint(5, 9))
# print(randrange(1, 9, 2))
# print(uniform(10.5, 25.5))      # принимает вещественные числа и возвращает вещественное число
# print(round(uniform(10.5, 25.5), 2))

# from random import *
# city = ["Москва", "Санкт-Петербург", "Екатеринбург", "Сочи", "Новосибирск"]
# print(choice(city))     # возвращает один элемент !!!CHOICE!!!
#
# from random import *
# city = ["Москва", "Санкт-Петербург", "Екатеринбург", "Сочи", "Новосибирск"]
# print(choices(city, k=3))    # возвращает больше одного элемента !!!CHOICES!!!

# a = [int(input("->"))]

# from random import randint
#
# a = [randint(50, 100) for i in range(3)]
# print(a)

# for i in range(3):
#     print(i)

# lst = [5, 3, 4, 2, 1, 8]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# from random import randint
# a = [randint(1, 100) for i in range(10)]
# print(a)
# m = max(a)
# print("Max:", m)
# a.remove(m)
# a.insert(0, m)
# print(a)

# from random import randint
# a = [randint(1, 100) for i in range(10)]
# print(a)
# minim = min(a)
# print("min:", minim)
# ind = a.index(minim)
# print(ind)
# # del a[:ind]
# b = a[ind:]
# print(b)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)     # true
# print('y' in x)     # false
# print('a' not in x)     # false
# print('y' not in x)     # true

# lst = []
# # if len(lst) == 0:
# if not lst:
#     print("Список пустой")
# print(bool(lst))

# from random import randint
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# # print("Третий список: ", c)
# # c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Третий список: ", c)
#
# с = (min(a), min(b), max(a), max(b))
# print("Третий список: ", c)

# m = [
#     [1, 2, 3, 4],       # 0 индекс
#     [5, 6, 7, 8],       # 1 индекс
#     [9, 10, 11, 12]     # 2 индекс
# ]
# print(m)
# print()
# print(len(m))
# print(m[1][2])      # [1] индекс списка, [2] индекс в списке
# for row in range(len(m)):       # 0 1 2 (индексы)
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y, "=", x + y)

# from random import randint
# w, h = 5, 4
# matrix = [[randint(1, 30) for x in range(w)]for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# from random import randint
# w, h = 3, 4
# s = 0
# matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         if x < 0:
#             s += 1
#             print(x, end="\t")
#     print()
# print(s)


# функции
# print()
#
#
# def hello(name, word):    # аргументы
#     print("Hello", name, "Say", word)
#
#
# hello("Tolyasik", "hi")     # параметры
# hello("Grinder", "hi")


# def get_sum(a, b):
#     print(a + b)
#
#
# n = 2
# m = 3
# get_sum(n, m)
# c = 5
# d = 6
# get_sum(c, d)


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")


# def get_sum(a, b):
#     print("Текст")
#     return a + b
#
#
# n = 2
# m = 3
# res = get_sum(n, m)
# print(res)


# def add(x, y):
#     if x > y:
#         return x - y
#     return x + y
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# m = add(a, b)
# print("Результат: ", m)


# def cube(a):
#     return a * a * a
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))


# def change(lst):
#     a = lst.pop()       # последний элемент
#     b = lst.pop(0)      # первый элемент
#     lst.append(b)       # добавляем первый элемент в конец
#     lst.insert(0, a)    # добавляем последний элемент в начало списка
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["С", "Л", "О", "Н"]))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["С", "Л", "О", "Н"]))


# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = 2
# b = 5
# if func(a, b):
#     print("Первое число больше второго")
# else:
#     print("первое число меньше второго")


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     else:
#         return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Ненадежный пароль")


# def get_sum(a, b=2, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# n = 2
# m = 5
# print(get_sum(1, d=n, b=m))


# def set_param(c=20, s="-"):
#     for i in range(c):
#         print(s, end="")
#     print()
#
#
# set_param(10, "+")
# set_param(5, "*")
# set_param(15, "#")
# set_param(7)        # дефис (-) - значение по умолчанию
# set_param()     # значение по умолчанию
# set_param(s="?")


# def digits_sum(n, even=True):      # n = 9874023
#     s = 0
#     while n > 0:
#         cur_digit = n % 10      # последняя цифра   3
#         if even and cur_digit % 2 == 0:      # s = 0 + 2 + 0 + 4
#             s += cur_digit
#         elif not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр: ")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))


# def display_info(name, age):
#     print("name;", name, "\nAge: ", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")

# a = 5
# print(a, id(a))         # ЧИСЛОВЫЕ ЗНАЧЕНИЕ ИЗМЕНЯЕМЫЕ СПИСКИ ДАННЫХ
# a = 6
# print(a, id(a))
#
# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.extend([4, 5, 6])      # СПИСКИ НЕИЗМЕНЯЕМЫЕ ДАННЫЕ
# print(lst1, id(lst1))

# a = "hello"
# b = "hello"
# a = [1, 2, 3]
# b = [1, 2, 3]
# a = 5
# b = 5
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# Изменяемые типы данных - list, set
# Неизменяемые типы данных - int, str, float, boolean , turple

# st = "hello"
# st = list(st)
# print(st[-1])
# st[-1] = 'q'
# print(st)

# кортежи (turple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(type(tpl))
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = ()
# print(type(a))

# a = tuple((1, 2, 3, 4, 5))
# print(a)
# print(type(a))
# print(a[-1])

# s = tuple([input("=>") for i in range(5)])
# print(s)

# from random import randint
#
#
# s = tuple(randint(0, 10) for i in range(5))
# print(s)

# s = tuple((2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# # print(t3 * 2)
# print(t3.count('a'))
# ch = ''
# if ch in t3:
#     print(t3.index(ch))
# else:
#     print("такого символа нет")
# for i in t3:
#     print(i * 2, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) +1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint
#
#
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl_1 = ran(0, 5)
# tpl_2 = ran(-5, 0)
# print(tpl_1)
# print(tpl_2)
# tpl_3 = tpl_1 + tpl_2
# print(tpl_3)
# print("0 =", tpl_3.count(0))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append("hi")
# del t[4][0]
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t     # распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
# # user = get_user()
# # n, year, married = user
# n, year, married = get_user()
# # print(user[0])
# # print(user[1])
# # print(user[2])
# print(n, year, married)

# tpl = (10, 20, 30)
# del tpl
# print(tpl)

# tpl = (10, 20, 30)
# lst = list(tpl)
# lst.append(50)
# print(lst)
# tpl = tuple(lst)
# print(tpl)

# countries = (
#     ("Germany", 80.2, (("Berlin", 3.326), ("Hamburg", 1.717))),
#     ("France", 66.2, (("Paris", 2.126), ("Marcele", 1.117))),
# )
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, ". Насиление: ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, "Население города: ", city_population)

# Множество (set)
# s = {"banana", "Apple", "orange"}
# print(s)
# print(type(s))
# for i in s:
#     print(i)

# a = set()
# print(a)
# print(type(a))

# s = {i * i for i in range(10)}
# print(s)
# print(64 not in s)

# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in s if 'a' in i}
# # a = {i for i in s if 'a' not in i}
# # a = ["A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s]
# a = {"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s if i[1] == 'c'}
# print(a)
#
# for i in s:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print("A" + i[1:])
#         else:
#             print('B' + i[1:])

# a = {"Tom", "Bob", "Alice"}
# a.add("Sam")
# print(a)
# # a.remove("Tom")
# # a.remove("Ann")     # KeyError
# # print(a.pop())
# a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# c = a & b
# c = a - b
# c = a ^ b
# print(c)
# a |= b
# print(a)

# s_1 = {1, 2}
# s_2 = {3}
# s_3 = {4, 5}
# s_4 = {3, 2, 6}
# s_5 = {6}
# s_6 = {7, 8}
# s_7 = {9, 8}
#
# # s = s_1 | s_2 | s_3 | s_4 | s_5 | s_6 | s_7
# s = s_1.union(s_2, s_3, s_4, s_5, s_6, s_7)
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# [1, 2, 3, 4, 5]
# s = frozenset({i ** 2 for i in range(10)})
# print(s)


# Словари (dict)

# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 3: 0}
# print(type(d))
# print(lst[0])
# print(d['one'])
# print(lst[2])
# print(d[3])

# d = {'one': 1, 'two': 2, 3: 0}
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d1))


# users = [('a', 'b'), ('c', 'd'), ('e', 'f')]
# print(users)
# d_users = dict(users)
# print(d_users)
# lst = list(d_users)
# print(lst)

# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[4])
# d[4] = 20
# print(d)


# d = {0: 'text', 'one': 1, (1, 2.3): 'кортеж', "список": [2, 3, 7, 6], True: 1}
# print(d)
# print(d[(1, 2.3)])
# print(d["список"][1])
# print(d[2][1])
# print('one' in d )
# print('one1' in d )
# print('text' in d )
# del d[0]
# print(d)
# print(d['one'])

# d = {'one': 1, 'two': 2, 'three': 3}
#
# # for key in d:
# #     print(key, d[key])
# key = 'three'
# if key in d:
#     del d[key]
#
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d)
#
# res = 1
# for key in d:
#     res *= d[key]
#
# print(res)

# d = {}
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)

# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# d = {3: 'x1', 7: 'x2', 5: 'x3', -1: 'x4'}
# print(d)
# print(len(d))

# goods = {
#     '1':['Core-i3-4330', 9, 4500],
#     '2':['Core-i5-4670K', 3, 8500],
#     '3':['AMD FX-6300', 6, 3500],
#     '4':['Pentium G3220', 8, 2100],
#     '5':['Core-i5-3450', 5, 6400],
# }
# for i in goods:
#     print(i, ") ", goods[i][0], "-", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         k = int(input("Количество: "))
#         goods[n][1] += k
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], "-", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")


# d = {3: 'x1', 7: 'x2', 5: 'x3', -1: 'x4'}
# print(d)
# print(d.keys())     # спиксок ключей
# print(d.values())       # список значений
# print(d.items())        # список и ключей и значений одновременно
# # for i, j  in d.items():
# #     print(i, j)
# print(list(d.values()))

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
#
# d2['b'] = 5
# d['e'] = 7


# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# # d.update({'r': 7, 't': 9})
# a = {'r': 7, 't': 9}
# c = d + a
# print(c)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
#
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
#
# print(d)
# print(new_d)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# s = dict()
# n = None
#
# for i in a:
#     if type(i) == str:
#         s[i] = []   # s['one'] = []
#         n = i       # n = 'one'
#     else:
#         s[n].append(i)  #       s['one'] = [1, 2, 3]
# print(s)


# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# s = list(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
# print(s)

# a = ['декабрь', 'январь', 'февраль']
# b = [12, 1, 2]
# f = {k: v for k, v in zip(a, b)}
# print(f)

# a = [1, 2, 3]
# c = [4.0, 8.5, 9.4]
# d = ['a', 'b', 'c']
# b = list(zip(a, c, d))
# print(b)

# dict_one = {'name': 'Igor', 'last_name': 'Doe', 'job': "Consultant"}
# dict_two = {'name': 'Irina', 'last_name': 'Smith', 'job': "Manager"}
#
# for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# two = [(1, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]
# a, b = zip(*two)
# print(a)
# print(b)

# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})

# s = ['red', 'blue', 'green']
# # j = 1
# for j, i in enumerate(s, 1):
#     print(j, ") ", i, sep="")
#     # j += 1

# def func(*args):
#     return args
#
# print(func(5))
# print(func(5, 2, 4))


# def summa(*param):
#     res = 0
#     for i in param:
#         res += i
#     return res
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8))
# print(summa(3, 4, 5))

# def ch(*args):
#     average = sum(args) / len(args)
#     print("Среднее арифметическое", average)
#     res = []
#     for num in args:
#         if average > num:
#             res.append(num)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
# print(func(5))


# def print_scores(student, *scores):
#     print("student: ", student, end=": ")
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_scores("Jhonatan", 100, 95, 88, 82, 92)
# print_scores("Rick", 82, 92)

# def func(**args):
#     return args
#
# print(func(a=1, b=2, c=3))

# def func(a, *args, d=1, **kwargs):
#     return a, args, kwargs, d
#
#
# print(func(5, 1, 7, 9, 8, 4, 6, d=7, b=2, c=3))

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()
#
# def outer(who):
#     who = "Alex"
#
#     def inner():
#         print("hello", who)
#
#     inner()
#
#
# outer("world")


# Замыкания


# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# i = outer(5)
# print(i(10))
#
# j = outer(6)
# print(j(20))


# print(outer(4)(6))        # в анонимных функциях


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a
#         c.append(4)
#         a = a + 1
#         return a, b, c
#
#     return func2

#
# func = func1()
# print(func())


# def func(city):
#     s = 0   # 2
#
#     def inner():
#         nonlocal s
#         s += 1      # s = s + 1 => 2
#         print(city, s)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res2 = func("Сочи")
# res2()

# students = {
#     "Alice": 98,
#     "Bob": 94,
#     "Frad": 45,
#     "David": 55,
#     "Ella": 80,
#     "Fiona": 67,
#     "Grace": 74
# }
#
#
# def make(lower, upper):
#     def inner(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return inner

#
# ball_A = make(80, 100)
# ball_B = make(70, 80)
# ball_C = make(50, 70)
# ball_D = make(0, 50)
# print(ball_A(students))
# print(ball_B(students))
# print(ball_C(students))
# print(ball_D(students))


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         return print()
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 7)
# print(obj1.add())   # сумма чисел
# print(obj1.sub())   #  разность
# print(obj1.mul())   #   произведение чисел


# анонимные функции (lambda-выражения)

# def summa(x, y):
#     return x + y
#
#
# print(summa(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x=5, y=7: x + y)())
# print((lambda *args: args)(1, 7, 8, 9, 4, 5, 6))

# a = lambda x, y: x + y
# print(a(1, 2))


# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t("abc "))

#
# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(42)
# print(f(1))
#
#
# def outer1(n):
#     return lambda x: x + n
#
#
# f1 = outer1(42)
# print(f1(1))
#
#
# outer2 = lambda n: lambda x: x + n
#
#
# f2 = outer2(42)
# print(f2(1))
#
# print((lambda n: lambda x: x + n)(42)(1))
#
# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))\


# def sort_val(i):
#     return i[1]
#
#
# d = {'c': 10, 'a': 15, 'b': 4}
# q = list(d.items())
# print(q)
# q.sort(key=sort_val, reverse=True)
# print(q)
# d1 = dict(q)
# print(d1)


# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Федя', 'last name': 'Иванов', 'rating': 6},
#     {'name': 'Игорь', 'last name': 'Сидоров', 'rating': 3},
#     {'name': 'Данил', 'last name': 'Фисташкин', 'rating': 4},
#     {'name': 'Гоша', 'last name': 'Бирюков', 'rating': 7}
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res2 = sorted(players, key=lambda item: item['rating'])
# print(res2)
#
# res3 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res3)


# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[1](12, 5)
# print(b)

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье'),
# }
#
# d[2]()
# print(d[2])

# map(func, iter), filter(func, iter)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, 5, 10]
#
# # a = list(map(mult, lst))
# a = list(map(lambda t: t * 2, lst))
# print(a)


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = list(map(lambda x, y: x + y, l1, l2))
# print(l3)

# t = ('abcd', 'abc', 'cdert', 'def', 'gfi')
#
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)


# b = [66, 98, 68, 59, 76, 60, 74, 81, 60]
# res = list(filter(lambda s: (s > 75) and s < 80, b))
# print(res)

# Декаратор
# def hello():
#     return 'hello "hello"'
#
#
# def super_func(func):
#     print('Hello "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'hello "hello"'
#
#
# print(id(hello))
# test = hello
# print(id(test))
# print(test())


# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# def func_test():
#     print("Hello 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# @my_decorator
# def func_test():
#     print("Hello 'func_test'")
#
#
# func_test()


# def my_decorator(func):     # декорирующая функия
#     def wrap():
#         print('*' * 20)
#         func()
#         print('=' * 20)
#     return wrap
#
#
# @my_decorator       # декоратор
# def func_test():        # декорируемая функция
#     print("Hello 'func_test'")
#
#
# func_test()


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "<b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "<i>"
#
#     return wrap
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())


# def cnt(fn):
#     c = 0
#
#     def wrap():
#         nonlocal c
#         c += 1
#         fn()
#         print("Вызов функции:", c)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print(arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Резникова")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args", args)
#         print("kwargs", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(arg1):     # 3
#     def outer(func):        # return_num
#         def wrap(*args, **kwargs):     # num
#             return arg1 * func(*args, **kwargs)
#
#         return wrap
#     return outer
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def outer(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Неверный тип данных")
#
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Неверный тип данных")
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return outer
#
#
# @typed(int, int, int)
# def type_fn(x, y, z):
#     return x * y * z


# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x * y * z

# def typed_fn3(x, y, z="Hello!"):
#     return (x + y) * z


# print(typed_fn3("hello", "world", ))
#
# # print(typed(3, 4, 5))
# # print(type_fn(3, 4, "!"))
# print(typed_fn2("Hello", "world", "!"))


# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))

# print(bin(18))      # 0b10010
# print(oct(18))      # 0o22
# print(hex(18))      # 0x12

# q = "pyt"
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# print("t" in e)
# print(e[1: -1:2])

# print("C:\\folder\\file.txt")
# print(r"C:\folder\file.txt")
# print(r"C:\folder\file.txt\\"[:-1])
# print(r"C:\folder\file.txt" + "\\")
# print("C:\\folder\\file.txt\\")

# x = 10
# y = 5
# # print(f"{x=}")
# # print("x=", x, sep="")
# print(x, "x", y, "/", 2, "=", x * y / 2)    #   10 x 5 / 2 = 25.0
# print(f"{x} x {y} / 2 = {x * y / 2}")       #   10 x 5 / 2 = 25.0

# num = 74
# print(f"{{{num}}}")
#
# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print(r'home' + "\\" + dir_name + "\\" + file_name)
# print(f'home\\{dir_name}\\{file_name}')


# s = """Hello
# world"""
#
# s1 = '''Hello
# World'''
#
# print(s)
# print(s1)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)

# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))

# print(ord('a'))
#
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break
#
#
# s = "Test string for me"
# arr = [ord(x) for x in s]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("->")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) -1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(12356))

# a = 122
# b = 97
# if b > a:
#     a, b = b, a
# for i in range(b, a + 1):
#     print(chr(i), end=" ")
#
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")


# from random import randint
#
# shortes = 7
# longest = 10
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     rand_len = randint(shortes, longest)
#     res = ""
#     for i in range(rand_len):
#         rand_char = randint(min_ascii, max_ascii)
#         res += rand_char
#
#     return res
#
#
# print("Ваш случайный пароль:", random_password())

# s = "hello, WORLD! I am learning Python!"
# print(s.capitalize())       # hello, WORLD! I am learning Python!
# print(s.lower())    # hello, world! i am learning pyhon!
# print(s.upper())    # HELLO, WOLRD! I AM LEARNING PYTHON!
# print(s.swapcase())     # HELLO, world! i AM LEARNING pYTHON!
# print(s.title())        # Hello, World! I Am Learning Python!
#
# print(s.count("h", 1, -4))  # количество заданных элементов
# print(s.find("Python1"))    # возвращает индекс заданного элемента или "-1" - , если элемента нет

# s = "I am learning Python. Hello, WORLD!"
# s = s[:s.find('h')] + s[s.rfind('h'):]
# print(s)

#   удаляют пробельные символы в строке
# print("    ру")
# print("    ру".lstrip())
# print("   n   ру".lstrip())
# print("    ру   ".rstrip())
# print("   ру   ".strip())


# print("http://www.python.org".lstrip("/:pths"))
# print("http://www.python.org".lstrip("/:pths").rstrip("org."))
# print("http://www.python.org".strip("/:pthsorg."))

# s = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(s.replace('Nython', 'Python', 2))     # поиск и замена символов

# s = "-"
# seq = ('a', 'b', 'c')
# print(s.join(seq))
#
# print("...".join(["1", "99"]))
#
# print(":".join("hello"))

# print('Строка разделенная пробелами'.split())       # разбивает строку на список подстрок
# print('www.python.org.ru'.split(".", 2))
# print('www.python.org.ru'.rsplit(".", 1))

# a = input("Введите ФИО: ").split()
# print(a)
# print(f'{a[0]} {a[1][0]}. {a[2][0]}.')

# Регулярные выражения

# import re
#
# s = "Я ищу совпадения в 2023 году. И  [^] я их найду в 2 счёта. 478_9-6. Hello world"
# reg = r'\d'     # [3-5]
# reg = r'\w'     # [3-5]
# reg = r'\d+'
# reg = r'\S'
# reg = r'\s'
# reg = r'\bсов'
# reg = r'сов\B'
# reg = r'[3-6]'
# reg = r'\W'
# reg = r'\D'
# reg = r'\AЯ ищу'
# reg = r'Hello\Z'
# reg = r'[3-6][0-9]'
# reg = r'[А-яЁё]'
# reg = r'[A-Za-z]'
# reg = r'[\[^]\]'
# print(re.findall(reg, s))       # возвращает список, содержащий все совпадения или []
# print(re.search(reg, s))        # возвращает первое совпадение с искомого шаблона
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# print(re.match(reg, s))     #   возвращает первое совпадение с искомым шаблоном только в начале строки
# print(re.split(reg, s, 5))      #   разбивает строку на список подстрок по заданному шаблону
# print(re.sub(reg, "!", s))      # поиск и замена
# print(re.findall(reg, s))
# print(ord("а"))
# print(ord("я"))
# print(ord("ё"))
# reg = r'20*'

# + от 1 до бесконечности повторений
# * от 0 до бесконечности повторений
# ? от 0 до 1 повторения

# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = '[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, s))

# print(re.findall(reg, s))

# d = "Цифры: 7, +17, -42, 0013, 0.3"
# print(re.findall(r'[+-]?\d+', d))

# print ("hello")
# print('hello github')
#
# print("ура у меня вышло")

# import re
#
# s = "05-03-1987 # дата рождения"
# print("Дата рождения:", re.sub('#.*', '', s))
# # Дата рождения: 05.03.1987
# print("Дата рождения:", re.sub("-", ".", re.sub('#.*', '', s)))

# import re
#
#
# s = "12 сентября 2023 год"
# req = r'\d{4}'
# print(re.findall(req, s))

# import re

# s = '+7 499 456-45 78, +74994564578, 7 (499) 456 45 78, 74994564578'
# req = r"\+?7\d{10}"
# print(re.findall(req, s))

# s = "Я ищу совпадения в 2023 году. И  я их найду в 2 счёта"
# reg = r'^\w+\s\w+'
# print(re.findall(reg, s))

# def validate_login(name):
#     return re.findall(r'[A-Za-z_-]{3,16}', name)
#
#
# print(validate_login("Python_master"))


# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# text = "hello world"
# print(re.findall(r"\w\+", text, flags=re.DEBUG))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта"
# reg = 'я'
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """
# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, flags=re.DOTALL))
# print(re.findall('one$', text))

# print(re.findall("""[a-z.-]+@[a-z.-]+""", 'test@mail.ru'))
# print(re.findall("""
# [a-z.-]+    # part 1
# @           # @
# [a-z.-]+    # part 2
# """, 'test@mail.ru', re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))

# text = "<body> Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))     # *?, +?, ?? - ленивый способ      {m, n}?, {,n}?, {m,}?

# s = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий|Николай"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# # reg = r"(?:int|double)\s*=\s*\d+[.\w+]*"
# reg = r"(int|double)\s*=\s*(\d+[.\w+]*)"
# print(re.findall(reg, s))

# s = '127.0.0.1'
# s = '192.168.255.255'
# reg = r'\d{1,3}.\d{1,3}.\d{1.3}.\d{1.3}'
# print(re.findall(reg, s))

# s = 'Word2016, PS6, AI5'
# reg = r'(([a-z]+)(\d+))'
# print(re.findall(reg, s, re.I))

# s = "5 + 7*2 - 4"
# reg = r'\s*[+*-]\s*'
# print(re.split(reg, s))
#
# s1 = "5 + 7*2 - 4"
# reg1 = r'\s*([+*-])\s*'
# print(re.split(reg1, s1))

# a = '31-08-2021'
# reg = r'(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(reg, a))

# s = "Я ищу совпадения в 2023 году. И  я их найду в 2 счёта"
# reg = r'(\d+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])

# s = "Самолет прилетает 10/23/2023. Будем рады вас видеть после 10/24/2023."
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

# s = "yandex.com and yandex.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s))

# ФАЙЛЫ

# f = open('test.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('text.txt', 'r')
# print(f.readline())
# f.close()

# f = open('text.txt', 'r')
# print(f.readlines())
# f.close()
#
# f = open('text.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# count = 0
# f = open('text.txt', 'r')
# for line in f:
#     count += 1
# f.close()
# print(count)

# f = open('text.txt', 'r')
# print(len(f.readlines()))
# f.close()

# f = open('xyz.txt', 'w')
# f.write('Hello\nWorld')
# f.close()

# f = open('xyz.txt', 'a')
# lines = ['\nThis is line 1', '\nThis is line 2']
# print(f.writelines(lines))
# f.close()

# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()

# f = open('text2.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать строку в файл;")
# f.close()
#
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# read_file[1] = "Hello world!\n"
# print(read_file)
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(read_file)
# f.close()

# f = open('test.txt')
# print(f.read(3))
# print(f.tell())     # на какой позиции находится курсор
# print(f.seek(1))    # перемещает курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open('test.txt', 'r+')

# with open('test.txt', 'w+') as f:
#     print(f.write('0123456789'))


# def longest_words(file):
#     with open(file, 'r') as text:
#         w = text.read().split()
#         print(w)
#         max_length = max(w)
#         print(max_length)
#
#
# print(longest_words('file.txt'))

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №8\nСтрока №9\nСтрока №10\n"

# with open('one.txt', 'w') as f:
#     f.write(text)

# for line in fr:
#     line = line.replace('Строка', 'Линия -')
#     fw.write(line)


# read_file = 'one.txt'
# write_file = 'two.txt'
# res = 'three.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'r') as fw, open(res, 'w') as res:
#     # f1 = fr.readlines()
#     # f2 = fw.readlines()
#     # print(f1)
#     # print(f2)
#     # f3 = f1 + f2
#     # res.writelines(f3)
#     for i, j in zip(fr, fw):
#         print(i)
#         print(j)
#         res.write(i + " -> " + j)

# МОДУЛИ OS(OS.PATH)

# import os

# print("Текущая директория:", os.getcwd())       # путь к файлу
# print(os.listdir())     # список папок и файлов, находящихся в текущей директории
# print(os.listdir("D:"))     #  путь к элементу

# os.mkdir("folder1")     # создать папку (одну)
# os.makedirs("nested1/nested2/nested3")      # создает много папок в папках

# os.remove('test.txt')       #  удаляет файл

# os.rmdir('folder1')      # удаление папки ( но только пустую папку )

# os.rename("xyz.txt", "first.txt")       #  переименовывает файл
# os.rename("first.txt", "nested1/first.txt") #   переносит файл в папку
# os.rename('folder', 'nested1')

# for root, dirs, files in os.walk('nested1'):
#     print('Root:', root)
#     print('Dirts', dirs)
#     print('files', files)

# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в папке {root_tree}")
#     print('-' * 50)
#
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#
#     print('-' * 50)
#
#
# remove_empty_dirs('nested1')

# import os.path

# import time

# print(os.path.split(r'C:\Users\Anatoly Mikushin\PycharmProjects\pythonProject\nested1\nested2\nested3\two.txt'))    # разбивает путь на кортежи (путь и имя документа)
#
# print(os.path.exists(r'C:\Users\Anatoly Mikushin\PycharmProjects\pythonProject\nested1\nested2\nested3\two.txt'))   # проверяет существование пути
#
# print(os.path.join(r'C:\Users\Anatoly Mikushin\PycharmProjects\pythonProject', 'nested2', 'two.txt'))

# dirs = ['Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         print(file_path)
#         open(file_path, 'w').close()
#
# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f"Какой-то текст для файла {file}")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, file in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(file)
#     print('-' * 50)
#
# print_tree('Work', topdown=False)
# print_tree('Work', topdown=True)


# path = "main.py"
# size = os.path.getsize(path)    # 'bytes'
# print(size // 1024, "КВ")   # размер файла
# ctime = os.path.getmtime(path)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(ctime)))   # время создания файла в секундах
# print(os.path.getsize(path), 'bytes')
# print(os.path.getctime(path))       # время создания файла в секундах
# print(os.path.getatime(path))       # время последнего доступа к файлу
# print(os.path.getmtime(path))       # время последнего изменения файла


# file_path = 'Work/F1/f11.txt'
#
# if os.path.exists(file_path):
#     dir0, name = os.path.split(file_path)
#     atime = os.path.getmtime(file_path)
#     print(f"{name} ({dir0})")
# else:
#     print(f'Файл {file_path} не существует')


# file_path = 'nested1/nested2'

# dir_name = 'nested1'
#
# objs = os.listdir(dir_name)
# print(objs)
#
# for obj in objs:
#     if os.path.isfile(obj):
#         print(obj)

# рекурсия


# def elevator(n):
#     if n == 0:
#         print("вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input('на каком вы этаже?'))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res      # res = res + i # 25 = 16 + 9
#
#
# print(sum_list([1, 3, 5, 7, 9]))    # 25

# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254, 16))


# names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))

# def count_item(item_list):
#     ...
#
#
# pr

# def remove(text):
#     if not text:
#         return ""
#     if text[0] == '\t' or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" Hello\tWorld     "))


# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# print(p1.x)
# print(p1.y)
# p1.x = 10
# print(p1.x)
# print(type(p1))


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p2 = Point()
# p1.set_coord(5, 10)
# # Point.set_coord(p1, 5, 10)
# print(p1.__dict__)
# p2.set_coord(20, 70)
# # Point.set_coord(p2, 20, 70)
# print(p2.__dict__)
#
# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print("Персональные данные".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: {self.country}"
#               f"\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_city(self, value):
#         self.city = value
#
#     def get_city(self):
#         return self.city
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.set_city("Питер")
# h1.print_info()
# print(h1.get_city())

# class Person:
#     skill = 10
#
#     # name = ""
#     # surname = ""
#
#     def __init__(self, name, surname):  # инициализация
#         self.name = name
#         self.surname = surname
#         print("инициализатор")
#
#     def __del__(self):      # деструктор
#         print("Деструктор")
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника", self.skill)
#
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
# del p1
# print()
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     count = 0
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def get_coord(self):
#         return self.x, self.y
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# p2 = Point(2, 7)
# print(p2.get_coord())
# p3= Point(10, 20)
# print(p3.get_coord())
# print(p3.count)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "Выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последний робот")
#         print("Работающих роботов осталось", Robot.k)
#
#     def say_hello(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hello()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot("C-3PO")
# droid2.say_hello()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot("R5-ST")
# droid3.say_hello()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут какую то работу\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
# del droid1
# del droid2
# del droid3
# print("Численность роботов:", Robot.k)


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @staticmethod
#     def __check_value(z):
#         if (z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         # if isinstance(x, int) or isinstance(x, float) and isinstance(y, int) or isinstance(y, float):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#
# p1 = Point(5, 10)
# # print(p1.__x, p1.__y)
# # p1.__x = 100
# # p1.__y = "abc"
# # print(p1.__x, p1.__y)
# p1.set_coord(20, "abc")
# p1.set.
# print(p1.get_coord())
# # print(p1.__dict__)
#
#
#
# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#     def __set_x(self, x):
#         if Point.__check_value(x):
#

# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# print(p1.name)
# print(p1.__dict__)


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__ = age
#
#     @property
#     def age(self):
#         return self.__age
# #
#     @age.setter
#     def age(self, value):
#         self.__age = value
#
#     @age.deleter
#     def age(self):
#         del self.__name
#
#
# p1 = Person("Vasya", 30)
# print(p1.__dict__)
# p1.name = "Igor"
# print(p1.name)
# del p1.name
# print(p1.__dict__)


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# # print(Point.__dict__)
# print(p1.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# class Numbers:
# @staticmethod
# def max(a, b, c, d):
#     mx = a
#     if b > mx:
#         mx = b
#     if c > mx:
#         mx = c
#     if d > mx:
#         mx = d
#     return mx
#     @staticmethod
#     def max(*args):
#         res = args[0]
#         for i in args:
#             if i > res:
#                 res = i
#         return res
#
#     @staticmethod
#     def min(*args):
#         res = args[0]
#         for i in args:
#             if i < res:
#                 res = i
#         return res
#
#
#     @staticmethod
#     def average(*args):
#         # return sum(args) / len(args)
#         res = 0
#         count = 0
#         for i in args:
#             res += i
#             count += 1
#         return res / count
#
#     @staticmethod
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact *= i
#         return fact
#
#
# print("Максимальное число:", Numbers.max(3, 5, 7, 9))
# print("Минимальное число:", Numbers.min(3, 5, 7, 9))
# print("Среднее арифметическое: ", Numbers.average(3, 5, 7, 9))
# print("Факториал числа:", Numbers.factorial(5))


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day45, month, year = map(int, date_as_string.split("."))
#         date1 = cls(day45, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <=3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# # dt1 = Date.from_string("23.10.2023")
# # print(dt1.string_to_db())
# # dt2 = Date.from_string("23.12.2023")
# # print(dt2.string_to_db())
# dates = [
#     "30.12.2023",
#     "30-12-2023",
#     "01.01.2023",
#     "12.31.2023"
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         dt1 = Date.from_string(string_date)
#         print(dt1.string_to_db())
#     else:
#         print("Неправильная дата или формат строки с датой")


# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Не верный формат ФИО")
#         letters = "".join(re.findall('[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         # print(letters)
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть цифрами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Соболев Игорь Валентинвич"
# print(p1.fio)
# p1.old = 27
# print(p1.old)
# p1.password = "4321 587585"
# print(p1.password)
# p1.weight = 60.5
# print(p1.weight)
# print(p1.__dict__)


# наследование

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#         print("Инициализатор базового класса")
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args, **kwargs):
#         print("Переопределенный инициализатор класса Line")
#         # Prop.__init__(self, *args, **kwargs)
#         super().__init__(*args, **kwargs)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# # class Rect(Prop):
# #     # def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
# #     #     self._sp = sp
# #     #     self._ep = ep
# #     #     self._color = color
# #     #     self._width = width
# #
# #     def draw_rect(self):
# #         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# # print(issubclass(Point, object))
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 2)
# line.draw_line()
# # rect = Rect(Point(30, 40), Point(70, 80))
# # rect.draw_rect()
# # print(line._width)
# # print(rect._width)


# class Figure:
#     def __init__(self, color):
#         self.color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть положительным числом")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Ширина должна быть положительным числом")
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника:", end=" ")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# print(rect.color)
# print(rect.width)
# print(rect.height)
# print(rect.area())


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("координаты должны быть целыми числами")
#
#
# class Rect(Prop):
#
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(20, 40), Point(100, 200))
# line.draw_line()
#
# rect = Rect(Point(45, 90), Point(20, 95))
# rect.draw_rect()
# rect.set_coord(Point(10.5, 50), Point(45.8, 94.8))
# rect.draw_rect()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.border)
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid red")
# shape2.show_rect()


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))


# перегрузка методов

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp=None, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Координаты должны быть целым числом")
#         elif sp is None:
#             if ep.is_int():
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целым числом")
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("координаты должны быть целыми числами")
#
#
# line = Line(Point(1,2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(20, 40), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(-10, -20))
# line.draw_line()


# абстрактивные методы

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):
#         raise NotImplementedError("в дочернем классе должен быть определен методов draw()")
#
#
# class Line(Prop):
#
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figure = list()
# figure.append(Line(Point(0, 0), Point(10, 10)))
# figure.append(Line(Point(10, 10), Point(20, 10)))
# figure.append(Rect(Point(50, 50), Point(100, 100)))
# figure.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figure:
#     f.draw()


# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length
#                 self._width = width
#                 self._length = length
#         else:
#             self.radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self.radius ** 2, 2)
#
#
# t = SqTable(10, 20)
# print(t.__dict__)
# print(t.calc_area())
#
#
# t1 = RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.calc_area())


# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на е2е4")
#
#
# # q = Chess()
# q = Queen()
# q.move()
# q.draw()


# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     rub = "RUB"
#     euro = "EUR"
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 76.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return round(self.value * Dollar.rate_to_rub, 2)
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, "=", self.convert_to_rub(), Currency.rub)
#
#
# class Euro(Currency):
#     rate_to_euro = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return round(self.value * Euro.rate_to_euro, 2)
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, "=", self.convert_to_rub(), Currency.rub)
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 50)
# for elem in d:
#     elem.print_value()
#
# print("*" * 50)
#
# for elem in e:
#     elem.print_value()


# интерфейсы

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child display1")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild display2")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()


# вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_method():
#         print("Статический метод")
#
#     def obj_method(self):
#         print("Метод экземпляра")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Вложенный класс")
#             print(MyOuter.age)
#             MyOuter.outer_method()
#             print(self.obj.name)
#             self.obj.obj_method()
#
#
# out = MyOuter('внешний')
# print(out.name)
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#
#         def display(self):
#             print('name', self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()


# class Intern:
#     def __init__(self):
#         self.name = 'Smith'
#
#     def display(self):
#         print("Name:", self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
#
# d1.display()
# d2.display()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Outer show")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Inner show")
#
#         class InnerClass:
#             def show(self):
#                 print("InnerClass show")
#
#
# outer = Outer()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         # self.os = self.OS()
#         # self.cpu = self.CPU
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i9"
#
#
# comp = Computer()
# # ny_os = comp.os
# # my_cpu = comp.cpu
# my_os = Computer.OS()
# my_cpu = Computer.CPU()
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)


# class Point:
#     def __init__(self, *args):
#         print(args)
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(5, 7, 10)
# print(len(p))


import math
import pickle

# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(1, 2)
# print(pt.length)
# print(pt.__dict__)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
# print("pt =", pt.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)
# print(pt3.__dict__)


# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def __init__(self):
#         Creature.__init__(self)
#         # super().__init__(name)
#         print("Инициализатор класса Animal")
#
#
# class Pet(Creature):
#     def __init__(self, age):
#         self.age = age
#         print("Инициализатор класса Pet")
#
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# dog = Dog("Buddy")
# dog.bark()
# # dog.sleep()
# # dog.play()
# print(Dog.__mro__)
#
#
# class Point:
#     def __init__(self):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width} ")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "Green", 5)

# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Инициализатор класса B")
#
#
# class C(A):
#     def __init__(self):
#         super().__init__()
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print("Инициализатор класса D")
#
#
# d = D()
# # print(D.mro())
# print(D.__mro__)


# Миксины (примеси)

# class Displayer:
#     @staticmethod
#     def display(messege):
#         print(messege)
#
#
# class LogerMixin:
#     def log(self, messege, filename="logfile.txt"):
#         with open(filename, "a") as fh:
#             fh.write(messege)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LogerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="subclasslog.txt")
#
#
# subclass = MySubClass()
# subclass.display("Строка будет печататься и сохраняться в файл")


# class Goods:
#     def __init__(self, name, weight, price):
#         print("Инит гудс")
#         super().__init__()
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("инит миксин")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00")
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
#
# n = Notebook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()


# перегрузка операторов

# 24*60*60 = 86400 (количество секунду в одном дне)

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, int):
#             raise ArithmeticError("Правый операнд должен быть типом clock")
#         return Clock(self.sec - other.sec)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключи должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключи должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         elif key == "min":
#             self.sec = s + 60 * value + h * 3600
#         elif key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(8000)
# print(c1["hour"], c1["min"], c1["sec"])
# с1["hour"] = 14
# c1["min"] = 18
# c1["sec"] = 55
# c2 = Clock(200)
# с4 = Clock(300)
# c3 = c1 + c2 + с4
# c1 -= c2
# print(c3.get_format_time())
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c3.get_format_time())
# print(c4.get_format_time())


# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым неотцирательным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", 5, 5, 3, 4, 5)
# # print(s1.marks[2])
# print(s1[2])
# print(s1.__dict__)
# # s1.marks[2] = 4
# s1[2] = 4
# s1[10] = 4
#
# del s1[2]
# print(s1.__dict__)
#
# l1 = [5, 5, 3, 4, 5]
# print(l1.extend([None] * 6))
# print(l1)


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     # if isinstance(g, Rectangle):
#     print(g.get_perimetr())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text("Python")
# print(t1.total(35))
# print(t2.total(35))


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}")
#
#     def make_sound(self):
#         print(f"{self.name} мяукаеи")
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}")
#
#     def make_sound(self):
#         print(f"{self.name} гавкает")
#
#
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
#
# for animal in (cat, dog):
#     animal.info()
#     animal.make_sound()


# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"{self.surname} {self.name} {self.age}")
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, speciality, grouper, rating):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.grouper = grouper
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.grouper} {self.rating}")
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, speciality, experience):
#         super().__init__()
#         self.speciality = speciality
#         self.experience = experience
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.experience}")
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, speciality, group, rating, topic):
#         super().__init__(surname, name, age, speciality, group, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"{self.topic}")
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     i.info()


# Функторы - это объекты класса, которые можно выполнять как функции


# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c2 = Counter()
# c2()


# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = string_strip("?:!.; ")
# print(s1(" Hello Wolrd!? "))


# class StringStrip:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         print(args)
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(self.__chars)
#
#
# s2 = StringStrip("?:!.; ")
# print(s2("  ?  Hello World  "))


# класс как декоратор
# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, *args, **kwargs):
#         print("*" * 50)
#         print("args", args)
#         print("kwargs", kwargs)
#         return f"Перед вызовом функции\n{self.fn(*args, **kwargs)}\nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func2(a, b, c):
#     return a * b * c
#
#
# @MyDecorator
# def func3(a, b):
#     return a + b
#
#
# print(func(2, 5))
# print(func2(2, 5, 2))
# print(func3(b=2, a=5))


# class Decor:
#     def __init__(self, string):
#         self.string = string
#
#     def __call__(self, func):
#         def wrap(x, y):
#             print("*" * 20)
#             print(self.string, end=" ")
#             func(x, y)
#             print("=" * 20)
#
#         return wrap
#
#
# @Decor("Значения:")
# def add(a, b):
#     print(a, b)
#
#
# add(2, 5)


# декорирование методов

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()


# декораторы классов

# def decor(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decor
# class ActualClass:
#     def __init__(self):
#         print("__init__")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))


# дескрипторы -
#  это класс (название не принципиально) в котором могут быть определены следуюзие методы
# __get__()
# __set__()
# __delete__()
# __set_name__()


# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{value} должно быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value

# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__surname = value
#
#
# p = Person("Ivan", "Petrov")
# # p.name.set("Igor")
# print(p.name)
# print(p.surname)


# метаклассы

# a = 5
# print(type(a))
# print(type(int))


# class MyList(list):
#     def get_length(self):
#         return len(self)
#
#
# lst = MyList()
# lst.append(1)
# lst.append(2)
# lst[0] = 3
# print(lst, lst.get_length())


#  Создание модулей


# import geometry.rect
# import geometry.sq
# import geometry.trian
# from geometry import rect, sq, trian
# # from geometry import *
#
#
# def run():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#     # print(r1.get_per_rect(), r2.get_per_rect())
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#     # print(s1.get_per_sq(), s2.get_per_sq())
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     run()

# from car import electrocar
#
#
# car = electrocar.ElectroCar("Tesla", "T", 2018, 99000, 100)
# car.show_car()
# car.description_battery()


# упаковка данных (Сериализация и Десериализация данных)

# 1. marshal
# 2. pickle
# 3. json

# dump() - сохраняет данные в открытый файл
# load() - считывает данные из открытого файла

# dumps() - сохраняет данные в строку
# loads() - считывает данные из строки

# import pickle


#
# file_name = "tarakan.txt"
#
# shop_list = {
#     "фрукты": ["яблоки", "манго"],
#     "овощи": ("морковь",),
#     "бюджет": 1000
# }
#
# with open(file_name, "wb") as fh:
#     pickle.dump(shop_list, fh)
#
# with open(file_name, 'rb') as fh:
#     shop = pickle.load(fh)
#
# print(shop)


# class Test:
#     num = 35
#     string = "Привет"
#     lst = [5, 9, 6]
#     d = {"one": "a", "two": (1, 2, 3)}
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.string}\nСписок: {Test.lst}\nСловарь: {Test.d}"
#
#
# obj = Test()
# obj_save = pickle.dumps(obj)
# print(obj_save)
#
# print(pickle.loads(obj_save))


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
#
# print(item3.__dict__)
# print(item3)


# import json

# data = {
#     'name': 'Olga',
#     'age': 25,
#     20: None,
#     'hobbies': ('running', 'singing', 'fishing'),
#     True: 1,
#     'children': [
#         {
#             'first_name': 'Alice',
#             'age': 6
#         }
#     ]
# }
#
# print(data)
#
# with open("data_file.json", "w") as fw:
#     json.dump(data, fw)
#
#
# with open("data_file.json", "r") as fw:
#     file = json.load(fw)
#
# print(file)


# x = {
#     "name": "Виктор"
# }
# y = json.dumps(x)
# print(json.dumps(x, ensure_ascii=False))
# # print(json.loads(y))


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())


# import requests
# import json
#
# import users as users
#
# responce = requests.get("http://jsonplaceholder.typicode.com/todos")
# todos = json.loads(responce.text)
# # print(todos[0:1])
#
# todos_by_user = {}  # {1: 11, 2: 8, 3: 7, 4: 6, 5: 12, 6: 6, 7: 9, 8: 11, 9: 8, 10: 12}
#
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)  # [(5, 12), (10, 12), (1, 11), (8, 11), (7, 9), (2, 8), (9, 8), (3, 7), (4, 6), (6, 6)]
# max_completed = top_users[0][1]  # 12
# print(max_completed)
#
# users = []  # [5, 10]
# for user, num_complete in top_users:
#     if num_complete < max_completed:    # 11 < 12
#         break
#     users.append(str(user))
#
# print(users)
#
# max_user = " and ".join(users)
# print(max_user)
#
# # users = ['9']
#
# m = "s" if len(users) > 1 else " "
# print(f"users {max_user} completed {max_completed} TODOs")
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
#
# with open("data.json", "w") as f:
#     filter_todos = list(filter(keep, todos))
#     json.dump(filter_todos, f, indent=2)


# CSV (Camma Sepatared Values) - переменные, разделенные запятыми

# import csv

# with open("data1.csv") as r_file:
#     file_reader = csv.reader(r_file, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             # print(row)
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#     print(f"Всего в файле {count} строк.")

# with open("data1.csv") as r_file:
#     file_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=";", fieldnames=file_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"файл содержит столбцы: {', '.join(row)}")
#         print(f"{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1


# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator='\r')
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", delimiter=";", lineterminator='\r'9, 15])
#     writer.writerow(["Саша", 5, 12])
#     writer.writerow(["Маша", 11, 18])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('sw_data_1.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator='\r')
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)

# with open('student_1.csv', 'w') as f:
#     names = ["Имя", "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=";", lineterminator='\r', fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Саша", "Возраст": 6})
#     file_writer.writerow({"Имя": "Саша", "Возраст": 15})
#     file_writer.writerow({"Имя": "Саша", "Возраст": 18})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
#
# with open("dict.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator='\r', fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)


# import requests
# import json
#
#
# response = requests.get("")
# todos = json.loads(response.text)

# Парсинг сайтов

# from bs4 import BeautifulSoup


# import re


# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois')
#     if "Copywriter" in whois:
#         return tag
#     return None


# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
# for i in salary:
#     get_salary(i.text)

# row = soup.find_all("div", class_="row")
# copywriter = []
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)
# row = soup.find("div", class_="name").text
# row = soup.find_all("div", class_="row")[1]
# row = soup.find("div", id="whois")
# row = soup.find("div", {"data-set": "salary}")
# row = soup.find("div", string="Alena")
# row = soup.find("div", string="Alena").parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous()
# print(row)
# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# # r = requests.get("http://ru.wordpress.org")
# # print(r.status_code)
# # print(r.headers)
# # print(r.content)
# # print(r.text)
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         write = csv.writer(f, delimiter=";", lineterminator="\n")
#         write.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[1]
#     plugins = p1.find_all("article")
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         # url = plugin.find("h3").find("a").get("href")
#         url = plugin.find("h3").find("a")["href"]
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refined(rating)
#         data = {'name': name, "url": url, "rating": r}
#         write_csv(data)
#
#
# def main():
#     url = "http://ru.wordpress.org/plugins"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refind_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open("plugins_1.csv", 'a', encoding="utf-8-sig") as f:
#         write = csv.writer(f, delimiter=';', lineterminator="\r")
#         write.writerow((data['name'], data['url'], data['snippet'], data['active'], data['cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("article", class_="plugin-card")
#     for el in p1:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ""
#         url = el.find('h3').find("a")['href']
#         snippet = el.find("div", class_="entry-excerpt").text.strip()
#         active = el.find("span", class_="active-installs").text.strip()
#         c = el.find("span", class_="tested-with").text.strip()
#         cy = refind_cy(c)
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cy': cy
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(9, 25):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# from parse_site import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()

# import socket
# import view import index
#
#
# URLS = {
#     '/': index,
#     '/blog': 'blog page'
# }
#
#
# def parse_request(request):
#     parse = request.split()
#     method = parse[0]
#     url = parse[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return "HTTP/1.1 405 Method Not Allowed!\n\n", 405
#     if url not in URLS:
#         return "HTTP/1.1 404 Page Not Found!\n\n", 404
#     return "HTTP/1.1 200 OK!\n\n", 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Страница не найдена</h3>'
#     elif code == 405:
#         return '<h1>405</h1><h3>Метод запрещен</h3>'
#     return URLS[url]
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     # body =                  URLS.get(url, "Errors 404")
#     body = generate_content(code, url)
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))     # 127.0.0.1:5000
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(10240)
#         print(f"Клиент {addr} => \n{request.decode('utf-8')}\n")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == "__main__":
#     run()


# import socket
# from view import index, blog
#
# URLS = {
#     '/': index,
#     '/blog': blog
# }
#
#
# def parse_request(request):
#     parse = request.split()
#     method = parse[0]
#     url = parse[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return "HTTP/1.1 405 Method Not Allowed!\n\n", 405
#     if url not in URLS:
#         return "HTTP/1.1 404 Page Not Found!\n\n", 404
#     return "HTTP/1.1 200 OK!\n\n", 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Found!</h3>'
#     elif code == 405:
#         return '<h1>405</h1><h3>Method Not Allowed!</h3>'
#     return URLS[url]()
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)  # URLS.get(url, "Errors 404")
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))  # 127.0.0.1:5000
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент {addr} => \n{request.decode('utf-8')}\n")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == "__main__":
#     run()


# import sqlite3
#
#
# # con = sqlite3.connect("profile.db")
# # cur = con.cursor()
# #
# # cur.execute("""""""")
# #
# # con.close()
#
#
# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     #     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     #     name TEXT NOT NULL,
#     #     summa REAL,
#     #     date BLOB
#     # )""")
#     cur.execute("DROP TABLE users")
#
# print("Hello")


# import sqlite3
#
# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
# cur.execute("""
# CREATE TABLE IF NOT EXISTS person(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# phone BLOB NOT NULL DEFAULT "+79090000000",
# age INTEGER CHECK(age > 0 AND age < 100),
# email TEXT UNIQUE
# )""")
# cur.execute("""
# ALTER TABLE person
# RENAME TO person_table;
# """)
# cur.execute("""
# ALTER TABLE person_table
# ADD COLUMN address TEXT;
# """)
# cur.execute("""
# ALTER TABLE person_table
# RENAME COLUMN address TO home_address;
# """)
# cur.execute("""
# ALTER TABLE person_table
# DROP COLUMN home_address;
# """)
# cur.execute("""
# DROP COLUMN home_address;
# """)
#
# with sqlite3.connect("db_3.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT *
#         FROM T1
#         ORDER BY FName
#         LIMIT 2, 5
#     """)
#
#     # res = cur.fetchall()    #   =>  []
#     # print(res)
#
#     # for res in cur:
#     #     print(res)
#
#     res = cur.fetchone()        # ()
#     print(res)
#     res2 = cur.fetchmany(2)      # => [(), ()]
#     print(res2)
#     res3 = cur.fetchall()
#     print(res3)


# import sqlite3
# 
# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 14000),
#     ('Daewoo', 12000),
#     ('Citroen', 17000),
#     ('Honda', 33000),
# ]
# 
# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )""")
# 
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)
# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})
# cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
# for car in cars:
#     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)
# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
# cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")

# con.commit()
# con.close()


# import sqlite3
#
# con = None
# try:
#     con = sqlite3.connect("car.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars2 SET price = price + 200;
#     """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса", e)
# finally:
#     if con:
#         con.close()


# import sqlite3

# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
# def write_ava(name, data):
#     try:
#         with open(name, 'wb') as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#
#     return True
#
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );""")
#
#     cur.execute("SELECT ava FROM users")
#     img = cur.fetchone()['ava']
#     write_ava("out.png", img)

# img = read_ava(1)
# if img:
#     binary = sqlite3.Binary(img)
#     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))


# cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
# last_row_id = cur.lastrowid
# buy_car_id = 2
# cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))

# cur.execute("SELECT model, price FROM cars")

# row = cur.fetchone()
# print(row)
# row2 = cur.fetchmany(5)
# print(row2)
# # row3 = cur.fetchall()
# # print(row3)
# for res in cur:
#     print(res['model'], "->", res[1])


# import sqlite3
#
#
# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)


# with open("sql_dump.sql", "w") as f:
#     for sql in con.iterdump():
#         f.write(sql)

# for sql in con.iterdump():
#     print(sql)


# SQLAlchemy ORM


# import os
#
# from models.database import DATABASE_NAME, Session
# import create_database as db_creator
# from models.lesson import Lesson, association_table
# from models.student import Student
# from models.group import Group
# from sqlalchemy import and_, or_, not_, desc
#
# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()
#
#     session = Session()
    # print(session.query(Lesson).all())
    # print("*" * 60)
    #
    # for it in session.query(Lesson):
    #     print(it)
    # print("*" * 60)
    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print("*" * 60)
    #
    # print(session.query(Lesson).count())
    # print("*" * 60)
    #
    # print(session.query(Lesson).first())
    # print("*" * 60)
    #
    # for it in session.query(Lesson).filter(not_(Lesson.id > 3),
    #                                        not_(Lesson.lesson_title.like("Ф%"))):
    #     print(it)
    #     print("*" * 60)
    #
    # for it, gr in session.query(Lesson.lesson_title, Group.group_name).filter(
    #         and_(association_table.c.lesson_id == Lesson.id,
    #              association_table.c.group_id == Group.id, Group.group_name == 'MDA-9')):
    #     print(it, gr)
    # print("*" * 60)
    #
    # print(session.query(Lesson).filter(Lesson.lesson_title is not None).all())
    # print("*" * 60)
    #
    # print(session.query(Lesson).filter(Lesson.lesson_title.in_(['Математика', 'Линейная алгебра'])).all())
    # print("*" * 60)
    #
    # print(session.query(Student).filter(not_(Student.age.between(16, 17))).all())
    # print("*" * 60)
    #
    # for it in session.query(Student).filter(Student.age.like("1%")).limit(4).offset(3):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(Student).order_by(desc(Student.surname)):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(Student).join(Group).filter(Group.group_name == 'MDA-7'):
    #     print(it)
    # print("*" * 60)

    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print("*" * 60)
    #
    # i = session.query(Lesson).first()
    # i.lesson_title = "Информатика"
    # session.add(i)
    # session.commit()

    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print("*" * 60)
    #
    # session.query(Lesson).filter(Lesson.lesson_title.like("%м%")).update({"lesson_title": "Математика"},
    #                                                                      synchronize_session='fetch')
    # session.commit()

    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print("*" * 60)
    #
    # i = session.query(Lesson).filter(Lesson.lesson_title == "М").first()
    # session.delete(i)
    # session.commit()
    #
    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print("*" * 60)


# шаблонизатор jinja

# from jinja2 import Template
#
# per = {
#     "name": "Игорь", "age": 28
# }
#
# tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.name }}.")
# msg = tm.render(p=per)
#
# print(msg)


from jinja2 import Template
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per = Person("Игорь", 28)
# print(per.get_name())
#
# tm = Template("Мне {{ p.get_age() }} лет. Меня зовут {{ p.get_name() }}.")
# msg = tm.render(p=per)
#
# print(msg)


# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Сочи'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
#
# link = """<select>
# {% for c in cities -%}
# {% if c.id > 3 -%}
#     <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#     {% elif c.city == "Москва" -%}
#         <option>{{ c['city'] }}</option>
#     {% else -%}
#         {{ c['city'] }}
# {% endif -%}
# {% endfor -%}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)


# active = [
#     {'href': "index", 'link': 'Главная'},
#     {'href': "news", 'link': 'Новости'},
#     {'href': "about", 'link': 'О компании'},
#     {'href': "shop", 'link': 'Магазин'},
#     {'href': "contacts", 'link': 'Контакты'},
# ]
#
# link = """<ul>
# {% for c in active %}
#     {% if c.link == "Главная" %}
#         <li><a href>="/{{c['href']}}" class="active">{{ c['link'] }}</a></li>
#     {% else %}
#         <li><a href="/{{c['href']}}">{{ c['link'] }}</a></li>
#     {% endif -%}
# {% endfor -%}
# </ul>"""
# tm = Template(link)
# msg = tm.render(active=active)
# print(msg)


# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300}
# ]
#
# tpl = "{{ cs | random }}"
# # tpl = "{{ (cs | max(attribute='price')).model }}"


# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)


# МАКРООПРЕДЕЛЕНИЯ

# html = """
# {% macro input_text(name, value='', type='text', size=20) -%}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {% endmacro -%}
#
# <p>{{ input_text('username') }}</p>
# <p>{{ input_text('email') }}</p>
# <p>{{ input_text('password') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)


# html = """
# {% macro input_text(name, placeholder, type="text") -%}
#     <input type="{{ type }}" name="{{ name }}" "placeholder="{{ placeholder }}">
# {% endmacro -%}
#
# <p>{{ input_text("firstname", "Имя") }}</p>
# <p>{{ input_text("lastname", "Фамилия") }}</p>
# <p>{{ input_text("address", "Адрес") }}</p>
# <p>{{ input_text("phone", "телефон", "tel" )}}</p>
# <p>{{ input_text("email", "почта", "email" )}}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)

# from jinja2 import Environment, FileSystemLoader
#
#
# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 33, "weight": 94.0}
# ]
#
# file_loader = FileSystemLoader('shablon')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('main1.html')
# msg = tm.render(users=persons, title="About Jijna",
#                 text="содержимое сайта")
#
# print(msg)

# from jinja2 import Environment, FileSystemLoader
#
# subs = ["Культура", "Наука", "Политика", "Спорт"]
#
# file_loader = FileSystemLoader('shablon')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('about.html')
# msg = tm.render(list_table=subs)
#
# print(msg)


# Flask


from flask import Flask


