a = [int(input("-> ")) for i in range(int(input("n = ")))]
print(a)
s = k = 0
for i in range(len(a)):
    if a[i] != 0:
        k += 1
    s += a[i]
print(s / k)

