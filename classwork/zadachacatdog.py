class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}")

    def make_sound(self):
        print(f"{self.name} мяукаеи")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}")

    def make_sound(self):
        print(f"{self.name} гавкает")


cat = Cat("Пушок", 2.5)
dog = Dog("Мухтар", 4)

for animal in (cat, dog):
    animal.info()
    animal.make_sound()