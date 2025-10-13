# polymorphism means that we make same method or function but the fucntion or use of it is different 



class Car:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
        
    def fuel_type(self):
        return "petrol or electric "


class Electric(Car):
    def __init__(self,model,brand):
        super().__init__(model,brand)
        
        
my_electric_car=Electric("tesla","5")
print(my_electric_car.fuel_type())



my_petrol_car= Car("tata","10")
print(my_petrol_car.fuel_type())
