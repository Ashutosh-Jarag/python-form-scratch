class car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class fortuner(car):
    def __init__(self,name):
        self.name = name

class Rangerover(car):
    def __init__(self,name):
        self.name=name
    
r1=Rangerover("Rangerover")
r1.start()
r1.stop()
print(r1.name)

f1 = fortuner("legender")
f1.start()
f1.stop()
print(f1.name)