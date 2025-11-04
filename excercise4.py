# OOPs Example

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return sum(self.marks)/len(self.marks)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Total: {self.total()}")
        print(f"Average: {self.average()}")
        print("--------------------")

s1 = Student("Rahul", [90, 85, 76])
s2 = Student("Sonia", [93, 87, 79])

s1.display()
