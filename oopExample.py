class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def average(self):
        return sum(self.grades) / len(self.grades)
alice = Student('Alice', [10, 20, 30])
print(alice.average())