# to take the input from the user 

name= input("Enter the name : ")
print("Hello ",name)

#  we can use + to write a string with the other string 
#  this is called string concatenation
print ("Hello, " + name)  

#  another method 
print("Hello, ",end="")
print(name)

# another method 
print("Hello, ",name,sep="")

#  another method
print(f"Hello,{name}")

'''
If the user intentionally or by  mistake enter the space 
to overcome this we use 

# string.strip()
'''

name=name.strip().title() # can chain the methods

# capitilize the first letter 
# name=name.capitalize()

#  for capitalizing full name
name=name.title()

# to split the strings
first,last=name.split()

print("hello, ",first)

