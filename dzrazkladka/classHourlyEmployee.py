class HourlyEmployee(Employee):
    """сотрудники с почасовой оплатой"""

    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate(self):
        return self.hours_worked * self.hour_rate
