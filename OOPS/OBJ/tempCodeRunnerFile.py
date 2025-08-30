class action():
    def fight(self):
        print(f"We are good to go ! ")

class boeing(action):
    def flight(self):
        print("Runway Free !")
        print(f"The Boeing 777 is set to fly lets go ! ")
        
        print(" GEAR UP !")

class airbus(action):
    def flight(self):
        print("Runway Free !")
        print(f"The Airbus A380 is set to fly lets go ! ")
        
        print(" GEAR UP !")
        

Runway1=boeing()
Runway2=airbus()

Runway1.flight()
Runway2.flight()
