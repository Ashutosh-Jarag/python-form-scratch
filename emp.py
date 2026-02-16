class emp:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show(self):
        print("role:", self.role)
        print("dept:", self.dept)
        print("salary:", self.salary)

class engineer(emp):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer", "IT", 300000)
    
e1 = emp('developer', 'IT', 2000)
e1.show()

e2 = engineer('ram', 24)
e2.show()