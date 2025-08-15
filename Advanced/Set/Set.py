'''
          SETS  : UNORDERED , MUTABLE,NO DUPLICATE 

'''

myset={1,2,3,4,5,6}
print(myset,type(myset))

# sets does'nt allow duplicates
myset={1,2,3,4,5,6,2,3,1}   # this has 2,1,3 as duplicate so it will ignore that 

print(myset)



# another way to make a set

myset1=set([1,2,1,4,5,"Hello",2])
print(type(myset1),myset1)



# empty set
empty_set=set()
print(empty_set)


''' 
Adding elements in the set 

'''

#  Method 1 : Using the split() method 

add_set=set(input("Enter the elements : ").split())
print(add_set)




#  Method 2 : Using asking evry time for items 

add_set=set()
n=int(input("Enter the set size : "))
for i in range (n):
  items=input(f"Enter the element {i+1 : } ")
  add_set.add(items)
print(add_set)


'''
Removing the Elements in the set

'''


add_set.remove(5)
add_set.discard()    # ----> this removes the elements 
add_set.clear()      # -----> removes elements 
add_set.pop()        # ----->   to remove the element from last 
print(myset)




'''
Traversing the set 

'''



set_traverse=set()
set_traverse=set(input("Enter the elements : ").split())



for i in set_traverse:
  print(i)


  
'''
Checking if there is element in the set 

'''
set_check={1,3,52,1,26,7}
if 52 in set_check:
  print("Sorting the set : \n")
  sorted_set=sorted(set_check)
  print(sorted_set)
  print(len(sorted_set))
else:
  print("NOt present")
  
  
  
  