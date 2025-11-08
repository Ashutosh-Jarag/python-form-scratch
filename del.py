class p:
    def __init__(self,name):
        self.name = name


s1 = p("name")
print(s1.name)

del s1

print(s1)
