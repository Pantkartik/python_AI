'''
Lamda function is a method/tarika by which we are able to write a function name in a short line of code

'''


'''
lets create a function with the help of a lamda function 


function name = lambda x(argument): return value 

'''

i=int(input("Enter the number : "))
tuf=lambda i:i*10
print(tuf(i))



def add_10(x):
  return x+10
print(add_10(5)) 





def sum(x,y):
  return x+y
print(sum(4,2))



mult = lambda x,y: x*y
print(mult(5,2))




'''  Sorting the tuple '''

trial=[(1,2),(15,1),(5,-1),(10,4)]
trial1=(2,4,1,4,12,10)
trial_sorted=sorted(trial1,key=lambda x : x[1])
print(list(trial_sorted))





''' Mapping function '''
'''  
map(func,seq)

'''

'''
map function is used to do specific task in the list elements 

'''

list_1=[1,2,3,4,5]
b=list(map(lambda x:x*2,list_1))
print(b)






''' Filter Function '''
list1=[1,2,3,4,5,6]
even_number=filter(lambda x: x%2==0,list1)
print(list(even_number))


#  using list comprehension for the above filter and map

'''  Filter using the list comprehension  '''
list_new=[1,2,3,4,5,6]
c= [ x for x in list_new if x%2==0]
print(c)







'''  Reduce function '''


from functools import reduce
list_reduce=[1,2,3,4,5,6]

product_A=reduce(lambda x , y : x*y,list_reduce)
print(product_A)