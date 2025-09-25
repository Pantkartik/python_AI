# to count all the numbers in a sorted list 


list=[1,2,3,4,5,6]

print(len(list))


print(list.count(2))


# to reverse the given list 
list.reverse()
print(list)

# to find the sum and average of the list elements




def avg(list1):
    sum=0
    average=0
    for items in list1:
        sum=sum+items
    
    average=sum/n
    print("sum : ",sum )
    print("average : ",average)
list1=[4,3,2,6,7,7,8]
n=len(list1)
avg(list1)



# to append an item in the end of list 

list1.append(5)
list1.sort()

print(list1)


# to remove the all occurence of specific element in list 

list_3=[11,11,2,3,4,5,4,7,9,2]
list_3=set(list_3)
   # for removing occurence of or duplicate numbers 
print(list_3)
x=5
list_3=list(filter(x.__ne__,list))
print(list_3)