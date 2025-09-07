'''
constructor like __init__ is used to automatically allow to make a object without using the method name again and again 

'''

# class without the use of constuctor

class Car():
    def car_spec(self,brand,color):
        self.brand=brand
        self.color=color

car1=Car()  # we have to use car() to use the methods everytime
car1.car_spec('Lambo','green')
print(car1.brand,car1.color)


# class with use of constructors

class Car():
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

car1=Car('mercedes','black')
car2=Car('lambo','green')
print(car1.brand,car1.color)
print(car2.brand,car2.color)



'''
making a new data using constructor 

'''



class stud:
    def __init__(self,name,Class,sex):
        self.name=name
        self.Class=Class
        self.sex=sex
    
student1=stud('kartik','Btech Cse','Male')
list_student=[]
list_student.append(student1.name)
list_student.append(student1.Class)
list_student.append(student1.sex)

print(list_student)



