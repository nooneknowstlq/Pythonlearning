class ComissionEmployee(SalaryEmployee):
    """Торговые предстаители, фиксириованная зп + комиссия"""
    def __init__(self, id, name, weekly_salary, comission):
        super().__init__(id, name, weekly_salary)
        self.comission = comission

    def colculate(self):
        fixed = super().calculate()
        return fixed + self.comission