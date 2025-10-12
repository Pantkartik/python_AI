#  lets us make a class which is of a car and object of class and attribute like model, brand and print the instanaces 



class Car:
    def __init__ (self,brand,model):
        self.brand=brand
        self.model=model


#  to make a functionality of writing full name of the car brand and model 
    def full_name(self):
        return f"My car is {self.brand} {self.model}"
#  making the objects 

# my_car=Car("tata","harrier")
# # printing the instanaces of the class objects
# print(my_car.brand,my_car.model)


#  making another object

my_newcar=Car("Mercedes","S class")
print(my_newcar.brand,my_newcar.model)


# calling the function for printing the full name

print(my_newcar.full_name())