class Car:
    counter=0
    def __init__(self,model,brand):
        
#  lets create a counter to count the car made 
        self.model=model
        self.brand=brand
        Car.counter+=1


# lets create objects car 

car_1=Car("model x ","tesla")
car_2=Car("model y","tesla")

print("Printing the number of car made ...... ")
print(Car.counter)

