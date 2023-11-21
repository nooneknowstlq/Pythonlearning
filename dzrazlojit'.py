class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    "Административныве работники, имеют фиксированную зарплату"
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate(self):
        return self.hours_worked * self.hour_rate


class ComissionEmployee(SalaryEmployee):
    # """Торговые предстаители, фиксириованная зп + комиссия"""
    def __init__(self, id, name, weekly_salary, comission):
        super().__init__(id, name, weekly_salary)
        self.comission = comission

    def colculate(self):
        fixed = super().calculate()
        return fixed + self.comission


class PayrollSystem:
    def calc(self, employees):
        print("Расчет заработной платы")
        print("=" * 50)
        for employee in employees:
            print(f"Заработная плата: {employee.id} - {employee.name}")
            print(f"- Проверить сумму: {employee.calculate()}")
            print()


salary = SalaryEmployee(1, 'Vasya Pupkin', 1500)
hourly = HourlyEmployee(2, 'Petr Petrovich', 40, 15)
comission = ComissionEmployee(3, 'Kot Kotovich', 1000, 250)
system = PayrollSystem()
system.calc([salary, hourly, comission])