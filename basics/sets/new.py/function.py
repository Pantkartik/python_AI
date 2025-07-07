
# Write a program with the following functions:
# print_name() → prints your name

# square(n) → returns the square of a number

# check_even(n) → prints whether the number is even or odd





# def print_name() :
#     print("kartik")
# print_name()

# n=print(input("Enter the n : "))
# def square(n):
#     print(square())

# radius=float(input("Enter the radius "))
# def area_circle(radius):
    
#     print(3.14*(radius**2))
# area_circle(radius)


# # Write a function is_positive(n) to check if a number is positive.
# number=int(input("Enter the number > "))

# def is_positive(number) :
#     if(number>0):
#         print("POSTIVE")
#     else :
#         print("NEGATIVE")
# is_positive(number)


# Write a function that takes a number and returns "Prime" or "Not Prime
def isprime(n):
    if n<=1 :
        return "NOT prime"
        for i in range(2,100):
            if(n%i==0):
                 return "Not prime"
        return "prime"
n=int(input("Enter the number  " )) 
print(isprime(n))
       

