# encapsuulation means to private a object or attribute using a __ before the attribute and to acces it we use get_attribute


class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    def get_brand(self):
        return f"Brand is : {self.__brand}"
    def price(self):
        return "1000000.00 rupees"
        
    
    
class Petrol(Car):
    def __init__(self,brand,model,speed):
        super().__init__(brand,model)
    
    
#  now accesing the brand without encapsulation

my_car=Petrol("tata","punch","200 kmph")
print(my_car.get_brand())    # easily can be accesed 

print(my_car.price())
#  to prevent this we use private (__attribute_name)