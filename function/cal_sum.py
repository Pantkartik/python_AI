# # creating a function to add two number 
# def sum_num(a,b):
#     sum=a+b
#     return sum

# #  calling a function 
# a=int (input("Enter the number a : "))
# b=int (input("Enter the number b : "))

# sum1=sum_num(a,b)   


# # a=3
# # b=1
# # print(a+b)

#  to creat#  to create a python function which calculates the average of three numbers 
def avg_num(a,b,c):
    avg=(a+b+c)/3
    return avg

a=int(input(" a: "))
b=int(input(" b: "))
c=int(input(" c: "))
average=avg_num(a,b,c)
print(average)
