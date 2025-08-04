def valid_age(age):
  if age>=18 and age<=60  :
    print("Valid")
 
  else :
    print("Not Valid")
age=int(input("Enter the age : "))
valid_age(age)