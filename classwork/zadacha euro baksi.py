from abc import ABC, abstractmethod


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


