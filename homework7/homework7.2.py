class Truck(Auto):
    def __init__(self,brand,age,mark,max_load,color = None,weight = None):
        super().__init__(brand,age,mark,color,weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()
    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)

class Car(Auto):
    def __init__(self,brand,age,mark,max_speed,color = None,weight = None):
        super().__init__(brand,age,mark,color,weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print("max speed is <max_speed>")

truck = Truck("mersedec",2002,"daimler",10,"green",2000)
truck.move()
truck.stop()
truck.birthday()
truck.load()
print(f"Brand:{truck.brand}",truck.age,truck.mark,truck.max_load,truck.color,truck.weight)

car = Car("ford",1995,"galaxy",100,"yellow",1500)
car.move()
car.stop()
car.birthday()