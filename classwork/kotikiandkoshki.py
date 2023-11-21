from random import randint, choice


class Cat:
    def __init__(self, name, age, pol):
        self.name = name
        self.age = age
        self.pol = pol

    def __str__(self):
        if self.pol == "M":
            return f"{self.name} is good boy!!"
        elif self.pol == "F":
            return f"{self.name} is good girl!!"
        else:
            return f"{self.name} is good Kitty!!!"

    def __repr__(self):
        return f"Cat(name='{self.name}, age={self.age}, pol='{self.pol}')"

    def __add__(self, other):
        if self.pol != other.pol:
            return [Cat("Not name", 0, choice(["M", "F"])) for _ in range(randint(1, 5))]
        else:
            raise TypeError("Types are not supported!")


cat1 = Cat("Tom", 4, "M")
cat2 = Cat("Elsa", 5, "F")
# cat3 = Cat("Murzik", 3, "M")
print(cat1)
print(cat2)
print(cat1 + cat2)
