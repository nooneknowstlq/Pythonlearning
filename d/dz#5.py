a = [int(input(">>")) for i in range(int(input("Количество элементов в списке: ")))]
print("Список элементов: ", a)
s = 0
for i in range(len(a)):
    if a[i] > 0:
        s += a[i]
        print("Положительные элементы: ", s)
print("Сумма положительных элементов = ", s)