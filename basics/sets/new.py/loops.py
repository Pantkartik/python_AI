# print 1 to 10 with help of for loop
# for i in range(11) :
#     print(i)
# print only even no from 1 to n 
# n=int(input("Enter the range of loop : "))
# for i in range(1,n+1) :
#     if i%2==0 :
#         print(i)

# ran_num=234
# num=int(input("Enter the number : "))
# while(ran_num!=num) :
#     print("Wrong try again : ")
#     num=int(input("Enter the number again : "))
    
# print("correct")


# to print table of num entered by user
# num=int(input(" Num : "))
# for i in range( 0,11) :
#     print(num*i)


# while loop to print the sum of first natural number sum 
# sum=0
# i=1

# while i<11 :
#     sum=sum+i
#     print(sum)
#     i+=1


#  Write a for loop to print all letters in the word "Artificial".
# a="artificial"
# a=list(a)
# print(a,type(a))
# i=0
# y=0
# count=0
# for y in range(len(a)) :
#     while (i<len(a)):
#         if(a[i]=='a') :
#             print("found at ",a[i])
#             count+1
#             print(count)
#             break
#     i+=1


# a="artificial"
# a=list(a)
# for i in range(0,len(a)) :
#     print(a[i])

#  Write a program that prints numbers from 1 to 50 but skips multiples of 5 using continue.
for i in range(1,51):

    if(i%5==0)  :
        continue
    print(i)