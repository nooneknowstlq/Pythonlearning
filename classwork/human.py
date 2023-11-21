class Human:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.surname} {self.name} {self.age}")


class Student(Human):
    def __init__(self, surname, name, age, speciality, grouper, rating):
        super().__init__(surname, name, age)
        self.speciality = speciality
        self.grouper = grouper
        self.rating = rating

    def info(self):
        super().info()
        print(f"{self.speciality} {self.grouper} {self.rating}")


class Teacher(Human):
    def __init__(self, surname, name, age, speciality, experience):
        super().__init__()
        self.speciality = speciality
        self.experience = experience
        self.surname = surname
        self.name = name
        self.age = age

    def info(self):
        super().info()
        print(f"{self.speciality} {self.experience}")


class Graduate(Student):
    def __init__(self, surname, name, age, speciality, group, rating, topic):
        super().__init__(surname, name, age, speciality, group, rating)
        self.topic = topic

    def info(self):
        super().info()
        print(f"{self.topic}")


group = [
    Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
    Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
    Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
    Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
    Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
    Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
]

for i in group:
    i.info()