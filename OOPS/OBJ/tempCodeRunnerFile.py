class Player:
  def __init__(self,name,health,attack):
    self.name=name
    self.health=health
    self.attack=attack
    
    def attack_enemy(self):
      print(f"{self.name} is attacking {self.attack}")
      
      
  
  
warrior = Player("kartik",100,20)


warrior.attack_enemy()