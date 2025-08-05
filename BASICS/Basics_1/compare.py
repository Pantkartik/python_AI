#  condition statements 
# x= int(input("Enter the number : "))
# if x>=18 and x<=50:
#   print("You are eligible for driving ")
# else:
#   print("Not eligible ")

  #  check whether the number is even or odd
x=int(input("Enter the number : "))
while x>0:
    if x%2==0:
      print("even")
      break
    else:
      print("odd")
      break
    
    
# switch case 
n=int(input("Enter the number : "))

match n:
  case 1:
    print("Hello ")
  case 2:
    print("hola")
  case 3: 
    print("namaste ")
  case 4:
    print("ram ram bhai")
  case _:
    print("error")