class Account:
    currency = "RUB"
    currency_usd = "USD"
    currency_eur = "EUR"
    rate_usd = 0.013
    rate_eur = 0.011

    def __init__(self, surname, num, percent, value=0):
        self.__surname = surname
        self.__num = num
        self.__percent = percent
        self.__value = value
        print(f"Счет # {self.__num}, принадлежащий {self.__surname}, был открыт")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет # {self.__num}, принадлежащий {self.__surname}, был закрыт")

    def get_percent(self):
        return self.__percent

    def get_value(self):
        return self.__value

    def get_surname(self):
        return self.__surname

    def get_num(self):
        return self.__num

    def set_percent(self, percent):
        self.__percent = percent

    def set_value(self, val):
        self.__value = val

    def set_surname(self, surname):
        self.__surname = surname

    def set_num(self, num):
        self.__num = num

    def print_info(self):
        print("Информация о счете:")
        print("-" * 20)
        print(f"#{self.get_num()}")
        print(f"Владелец: {self.get_surname()}")
        self.print_balance()
        print(f"Проценты {self.get_percent():.0%}")
        print("-" * 20)

    def add_money(self, val):
        self.__value += val
        print(f"{val} {Account.currency} было успешно добавлено!")
        self.print_balance()

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print("Проценты были успешно начислены!")
        self.print_balance()

    def print_balance(self):
        print(f"Текущий баланс: {self.get_value()} {Account.currency}")

    def convert_to_usd(self):
        usd_val = Account.convert(self.get_value(), Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.currency_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.get_value(), Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.currency_eur}")

    def withdraw_money(self, val):
        if val > self.__value:
            print(f"К сожалению, у вас нет {val} {Account.currency}.")
        else:
            self.__value -= val
            print(f"{val} {Account.currency}, было успешно снято!")

        self.print_balance()

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate


acc = Account("Федор", "8888", 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

Account.set_usd_rate(2)
acc.convert_to_usd()

Account.set_eur_rate(3)
acc.convert_to_eur()
print()

acc.set_percent(0.08)
acc.set_value(5000)
acc.set_surname("Петя")
acc.set_num("9999")
acc.print_info()
print()

acc.add_percents()
print()

acc.withdraw_money(8000)
print()

acc.withdraw_money(100)
print()

acc.add_money(9000)
print()

acc.withdraw_money(300)
