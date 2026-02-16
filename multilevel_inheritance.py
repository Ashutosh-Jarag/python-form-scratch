class car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class kia(car):
    def __init__(self, name):
        self.name = name

class sonet(kia):
    def __init__(self, type):
        self.type = type

k1 = kia('sonet')
print(k1.name)