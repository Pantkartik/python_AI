class Car():
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

car1=Car('mercedes','black')
car2=Car('lambo','green')
print(car1.brand,car1.color)
print(car2.brand,car2.color)