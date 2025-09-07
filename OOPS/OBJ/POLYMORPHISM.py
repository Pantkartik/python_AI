'''

one name many forms 

ek word of uske use case bhot jyada 

runs

car runs fast 
boy runs fast
time runs fast 


here runs is used for different data types 

'''


# lets create a class using  a polymorphism 
class run():
    def speed(self):
        print('car runs with speed')
    
class human(run):
    def speed(self):
        print(f"humans can run with max speed of {"30 kmph"}")
class tiger(run):
    def speed(self):
        print(f"tiger can run with max speed of {"97 kmph "}")
        
kartik=human()
Tiger=tiger()
kartik.speed()
Tiger.speed()





#  another example 


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
