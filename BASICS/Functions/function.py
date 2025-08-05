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


#  using main function to define functions anywhere in the program



def main():
  name=input("Enter the name : ")
  hello(name)

def hello(to):
  print("Hello, ",to)

main()


# return function 

def main():
  x=int(input("Enter the number : "))
  print("Square of x is ",square(x))

def square(n):
  return n*n

main()