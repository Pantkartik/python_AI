'''
OOPS CONCEPTS 

1. CLASS
2. OBJECT
3. INHERITANCE
4. POLYMORPHISM
5. ENCAPSULATION

'''

####################################################

'''
oops helps in making the code more reusable and modular , prevent attacks by making the code more secure and less prone to bugs. 

also helps in reducing code duplication and improving code maintainability.

'''



# lets try is a code without oops 

player1 = "kartik"
age = 30
height = "6 feet"
# 

player2 = "naman"
age = 25
height= "5.5 feet"

def attack():
  print(f"{player1} is attacking {player2}")

attack()


# this code is not using OOP principles




'''
let use oops concept 

'''

class Player:
  def __init__(self,name,health,attack):
    self.name=name
    self.health=health
    self.attack=attack
    
    def attack_enemy(self):
      print(f"{self.name} is attacking {self.attack}")
      
      
  
  
warrior = Player("kartik",100,20)


warrior.attack_enemy()
