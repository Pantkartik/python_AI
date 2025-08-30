'''

Defining a class car and than its propeties 

'''

# class Car():
#   def car_details(self,brand,color):
#     self.brand=brand
#     self.color=color
    
#   def show_details():
#     print(f"The car brand is {self.brand} and the color of the car is {self.color}")
#     print("done")

#   car1=Car()
#   car1.car_details('mercedes','white')
#   car1.show_details()    



class Player():
  def define_player(self,name,age,power):
    self.name = name
    self.age =  age
    self.power = power
    
  def show_player(self):
      print(f"The player name is {self.name} and the age of player is {self.age} and a power of {self.power}")

player1=Player()
player1.define_player('kartik',19,'coding')
player1.show_player()
    
    
  