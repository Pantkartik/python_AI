#  Tuple is ordered ,immutable ,allows the duplicate 


tuple="kartik","pant",23
print(tuple,type(tuple))


# making a tuple containing only 1 element 
tuple1=("Kela")
print(tuple1,type(tuple1))    # this will give type string 
tuple2=("kela",)
print(tuple2,type(tuple2))



'''  converting list to tuple '''
convert_list_to_tuple=tuple(['HELLO',"namaste","kela khao kela khao "])
print(convert_list_to_tuple,type(convert_list_to_tuple))



'''  converting a tuple to list '''
tuple=('HELLO',"namaste","kela khao kela khao ")
convert_tuple_to_list=list(tuple)
print(convert_tuple_to_list,type(convert_tuple_to_list))



'''  Accesing item in a tuple'''

acces_tuple="kartik","india",34,6
item=acces_tuple[0]
print(item)


'''  Iterating in a tuple '''

iterate_tuple=(1,2,3,4,5,'Python')
for i in iterate_tuple:
  print(i)
  
  
''' checking if an element is in the tuple '''
check_tuple=tuple(['name',"age",24])
if 'name' in check_tuple:
  print("Yes")
else:
  print("No")
  
  
''' Method in Tuple '''
method_tuple=tuple(['hello','holla',"namaste","ram ram"])

# 1. length of tuple 
print(len(method_tuple))


# 2. to count element in tuple
print(method_tuple.count('hello'))

# 3. to find the index of item
print(method_tuple.index('ram ram'))


''' slicing in tuple further reversing '''

slice_tuple=['k','a','r','t','i','k']
b=slice_tuple[0:4]
rev=slice_tuple[::-1]
print(b,rev)


''' Unpacking the elements of tuple '''

credential=('kartik',19,"6 feet")
name,age,height=credential
print(name)
print(age)
print(height)



''' Unpacking the tuple and than to list '''

credential_1=(0,1,2,3,4,10,9)
i1,*i2,i3=credential_1
print(i1)
print(i3)
print(type(i2),*i2)



