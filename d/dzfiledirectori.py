import os

root = r"C:\Users\Anatoly Mikushin\PycharmProjects\pythonProject\files"
obj = os.listdir(root)
print(obj)

lst = []
for ob in obj:
    p = os.path.join(root, ob)
    print("p =>", p)
    lst.append(p)

print(lst)

obj_sort = sorted(lst, key=os.path.isfile, reverse=True)
print(obj_sort)