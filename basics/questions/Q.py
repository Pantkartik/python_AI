# to  print the numbers from 1 to 100
# i=1
# while i<=100 :
#     print(i)
#     i+=1


#  to print the number from 100 to 1 
# i=100
# while i>0 : 
#     print(i)
#     i-=1

#  to print multiplication table of a number n 
# i=1
# n=int(input('Enter the n : '))
# while i!=11 :
#     print(n*i)
#     i+=1

# print the elements of list using loop
# list=[1,4,9,16,25,36,49,64,81,100]
# for i in range(1,len(list)) :
#     print(i)
# # search x in tuple tuple=(1,4,9,16,25,36,49,64,81,100)

tuple=(1,4,9,16,25,36,49,64,81,100)
tuple=list(tuple)
# print(tuple)
x=int(input("Enter the number to seacrh : "))
is_found=False
for i in range(1,len(tuple)) : 
    if(tuple[i]== x) :
        is_found=True
if is_found == True : 
    print("Found ")
else :
    print("Not found")
        


