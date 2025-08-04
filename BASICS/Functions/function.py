# declaring the function 
def hello(name):
  print("Hello,",name)

name=input("Enter your name : ")
hello(name)


# to calculate the sum of two numbers usinf functions

def sum_num(a,b):
  return a+b

a=int(input("NUMBER : "))
b=int(input("NUMBER : "))
print(sum_num(a,b))


#  to find the valid age for DL

def valid_age(age):
  if age>=18 and age<=60  :
    print("Valid")
 
  else :
    print("Not Valid")
age=int(input("Enter the age : "))
valid_age(age)