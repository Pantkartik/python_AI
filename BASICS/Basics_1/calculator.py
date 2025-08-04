x,y=1,2
z= x+y
print(z)         # this will give 3 

x=input("Enter the x : ")
y=input("Enter the y : ")
z=x+y
print(z)      # this will give 12 

#  to overcome this we have to explicit change in the data type
x=int(input("Enter the x : "))
y=int(input("Enter the y : "))
z=x+y
print(z)      # this will change string to int return 3


#  float 

x=float(input("Enter the x : "))
y=float(input("Enter the y : "))
z=round(x+y)
print(f"{z:,}")   # for comma we use f is for formatting ==> {z:,}

#  output is 1,000 if input is 1000