class vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print("brand",self.brand)
        print("speed",self.speed)


class Car(vehicle):
    def __init__(self,brand,speed,fules):
        super().__init__(brand,speed)
        self.fules = fules

    def display(self):
        self.show()
        print("fules",self.fules)


object = Car("xyz",89,200)
object.display()            


        