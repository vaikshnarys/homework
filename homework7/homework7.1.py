import time
class Auto:
    def __init__(self,brand,age,mark,color = None,weight = None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight
    def move(self):
        print("move")
    def stop(self):
        print("stop")
    def birthday(self):
        self.age += 1
        print(self.age)

ford = Auto("ford",2000,"escalate")

ford.move()
ford.stop()
ford.birthday()