#  in inheritance we make a parent class and than we link the child classes to a parent class with the help of super()   all the attributes of parent is accesible to the child class also 



#  lets create a class ( parent : car )


class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def fullname(self):
        return f"{self.brand} {self.model}"
    

# child class 

class ElectricCar(Car):
    def __init__(self,brand,model,batterysize):
     super().__init__(brand,model)
    
     self.battery_size=batterysize
     

     
# printing the data of electric car 
electriccar=ElectricCar("Tesla","Model Y ","123 KWH ")
print(electriccar.brand,electriccar.model,electriccar.fullname())
    
        
        