import json


class Student:
    def __init__(self, name: object, marks: object) -> object:
        self.name = name
        self.marks = marks

    def __str__(self):
        # a = ""
        # for i in self.marks:
        #     a += str(i) + ", "
        # # return f"Студент: {self.name} - {a[:-2]}"
        # a = ", ".join(map(str, self.marks))
        # return f"Студент: {self.name} - {a}"

        return f"Студент: {self.name} - {', '.join(map(str, self.marks))}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_marks):
        self.marks[index] = new_marks

    def average_marks(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def dump_to_json(self, filename):
        data = {"name": self.name, "marks": self.marks}
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        with open(filename, "r") as f:
            print(json.load(f))


class Group:

    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        a = ''
        for i in self.students:
            a += str(i) + "\n"
        return f"{a}"
        a = '\n'.join(map(str, self.students))
        return f"группа:{self.group}\n{a}"

    @staticmethod
    def change_group(group1, group2, index):
        return group2.add_student(group1.remove_student(index))

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @staticmethod
    def dump_group(file, group):
        try:
            data = json.load(open(file))
        except FileNotFoundError:
            data = []

        with open(file, 'w') as f:
            stud_list = []
            for i in group.students:
                stud_list.append([i.name, i.marks])
            data.append(stud_list)
            json.dump(data, f, indent=2)

    @staticmethod
    def upload_group(file):
        with open(file, "r") as f:
            print(json.load(f))

st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
file1 = "student.json"
# st1.dump_to_json(file1)
# st1.load_from_file(file1)
# print(st1)
# st1.add_mark(4)
# print(st1)
# st1.delete_mark(2)
# print(st1)
# st1.edit_mark(1, 5)
# print(st1)
# print(st1.average_marks())
st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
st3 = Student('Birukov', [3, 2, 5, 4, 5])
sts = [st1, st2]
my_group = Group(sts, "ГК Python")
my_group.add_student(st3)
print(my_group)
print()
my_group.remove_student(1)
print(my_group)
print()
group22 = [st2]
my_group2 = Group(group22, "ГК Web")

Group.change_group(my_group, my_group2, 0)
print("-" * 20)
print(my_group)
print("-" * 20)
print(my_group2)

file2 = "group.json"
# Group.dump_group(file2, my_group)
# Group.dump_group(file2, my_group2)
Group.upload_group(file2)