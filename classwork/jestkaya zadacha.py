import re


class UserData:
    def __init__(self, fio, old, ps, weight):
        # self.verify_fio(fio)
        # self.verify_old(old)
        # self.verify_weight(weight)
        # self.verify_ps(ps)

        self.fio = fio
        self.old = old
        self.password = ps
        self.weight = weight

    @staticmethod
    def verify_fio(fio):
        if not isinstance(fio, str):
            raise TypeError("ФИО должно быть строкой")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Не верный формат ФИО")
        letters = "".join(re.findall('[a-zа-яё-]', fio, flags=re.IGNORECASE))
        # print(letters)
        for s in f:
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквы и дефис")

    @staticmethod
    def verify_old(old):
        if not isinstance(old, int) or old < 14 or old > 120:
            raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")

    @staticmethod
    def verify_weight(w):
        if not isinstance(w, float) or w < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")

    @staticmethod
    def verify_ps(ps):
        if not isinstance(ps, str):
            raise TypeError("Паспорт должен быть строкой")
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")
        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть цифрами")

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, ps):
        self.verify_ps(ps)
        self.__password = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight


p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
p1.fio = "Соболев Игорь Валентинвич"
print(p1.fio)
p1.old = 27
print(p1.old)
p1.password = "4321 587585"
print(p1.password)
p1.weight = 60.5
print(p1.weight)
print(p1.__dict__)
