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
import math
import re
import sys

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

import re

s = "Я ищу совпадения в 2023 году. И  [^] я их найду в 2 счёта. 478_9-6. Hello world"
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

d = "Цифры: 7, +17, -42, 0013, 0.3"
print(re.findall(r'[+-]?\d+', d))