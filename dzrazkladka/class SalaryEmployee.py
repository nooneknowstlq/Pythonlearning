class SalaryEmployee(Employee):
    "Административныве работники, имеют фиксированную зарплату"
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate(self):
        return self.weekly_salary