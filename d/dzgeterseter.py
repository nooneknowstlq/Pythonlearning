class Car:
    model = "name"
    years_of_issue = "0"
    manufacturer = "name"
    engine_power = "0"
    color = "white"
    price = "0"

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}\nГод выпуска: {self.years_of_issue}\nПроизводитель: {self.manufacturer}"
              f"\nМощность двигателя: {self.engine_power}"
              f"\nЦвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def input_info(self, first_name, years_of_issue, manufacturer, engine_power, color, price):
        self.model = first_name
        self.years_of_issue = years_of_issue
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.color = color
        self.price = price

    def set_model(self, value):
        self.model = value

    def get_model(self):
        return self.model

    def set_years_of_issue(self, value):
        self.years_of_issue = value

    def get_years_of_issue(self):
        return self.get_years_of_issue()

    def set_manufacturer(self, value):
        self.manufacturer = value

    def get_manufacturer(self):
        return self.manufacturer

    def set_engine(self, value):
        self.engine_power = value

    def get_engine(self):
        return self.engine_power

    def set_color(self, value):
        self.color = value

    def get_color(self):
        return self.color

    def set_price(self, value):
        self.price = value

    def get_price(self):
        return self.price


h1 = Car()
h1.print_info()
h1.input_info("X7 M50i", "2021", "BMW", "530 л.с", "white", "10790000")
h1.print_info()
