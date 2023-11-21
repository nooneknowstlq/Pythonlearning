class Student:
    def __init__(self, name, brand, memory, processor):
        self.name = name
        self.brand = brand
        self.memory = memory
        self.processor = processor

    def __str__(self):
        return f'Student: {self.name}, model: {self.brand}  {self.memory}, processor: {self.processor}'


student1 = Student('Федя', 'Dell', 'Inspiron', 'i7')
student2 = Student('Вася', 'HP', 'Pavilion', 'i5')
student3 = Student('Дракон', 'Lenovo', 'IdeaPad', 'i3')

print(student1)
print(student2)
print(student3)
