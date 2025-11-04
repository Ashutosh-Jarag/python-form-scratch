#  construcitor or __init__

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("constructor called")

s1 = student('ram',20)
print(s1.name,s1.age)

s2 = student('shyam',34)
print(s2.name,s2.age)