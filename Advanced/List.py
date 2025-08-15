#  list is immutable and cannot be chnaged 

# creating an empty list

my_list=list()
print(my_list)

# creating a list 

my_list=["hello",6,"namaste",True]
print(my_list)

item=my_list[0]
print(item)



# Itertrate in the list using for in loop 
for i in my_list:
  print(i)
  


#  for checking if the item is in the list 

if "namaste" in my_list:
  print("yes present")
else:
  print("not present")



'''
                 Method of list 
'''

# 1. To find the length of the list 

print(len(my_list)) 

# 2. Append the item 

my_list.append("lemon")
print(my_list)

# 3. Inserting an item in a specific index 

my_list.insert(0,"kartik")
print(my_list)


# 4. Removing the last element of list 

item=my_list.pop()    # this returns the item and also removes it from last 
print(my_list)

# 5. Removing a specific element 

my_list.remove("kartik")
print(my_list)


#  remove all element from list 
# my_list.clear()
# print(my_list)

# to reverse a list 
item=my_list.reverse()
print(my_list)

# sort a list 

my_list1=[3,52,1,7]
item=my_list1.sort()
print(my_list1)


# to sort  a list but donot change the original list 

my_list1=[3,52,1,7]
my_newlist= sorted(my_list1)

print(my_list1)   # this will give the original list 
print(my_newlist)   # this will give the new sorted list 




# trick 

list_trick=[0]*5
print(list_trick)    # this print the [0,0,0,0,0]

# concat the list 

my_concat=my_list1+list_trick
print(my_concat)  


# slicing the list 

list_new=[1,2,3,4,5,6,7,8,9]
a=list_new[0::2]
b=list_new[::-1]    # reversing the list
list_new.reverse()
''' stepping in the list slicing means skiping that much of place '''
print(a)
print(b)
print(list_new)




'''   making a copy of list '''

list_orginal=["kartik","pant",2,4,True]
list_copy=list_orginal    
# this creates a copy but both refer to same location and if we make changes in copy list it also changes in the original list 

list_copy.append("banana")   # changes in both list
print(list_copy)
print(list_orginal)


#  to overcome this we make actual copy of the list 
list_orginal=["kartik","pant",2,4,True]

list_copy=list_orginal.copy()
list.copy=list(list_orginal)   # another method to make copy
list_copy=list_orginal[:]    # anotehr method to make copy 
list_copy.append("kela")
print(list_copy)
print(list_orginal)




''' 

Comprehensive list making 

helps to make action in inside the list 

'''



list_fresh=[1,2,4,5,6,8,9]

# to make a new list for square of items in the list 

list_square=[i*i for i in list_fresh]
print(list_fresh)
print(list_square)