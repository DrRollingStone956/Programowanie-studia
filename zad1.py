class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return sum(self.marks) / len(self.marks) > 50


stud1 = student("Gabriel", [90, 100, 100])
stud2 = student("Wiktoria", [40, 30, 20])
print(stud1.is_passed())
print(stud2.is_passed())