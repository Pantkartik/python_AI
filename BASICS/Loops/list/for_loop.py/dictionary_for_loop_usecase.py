#  A dict or dictionary is a datatype in python which stores the data in a key value set


'''
lets declare a dict 

key:value

'''

dict1={
 "Name":"kartik",
 "Age":"20",
 "Gender":"Male",
 "Course":"Btech AI/ML" , 
}




'''
 ACCESING THE DATA FROM THE DICTIONARY
 
 '''
# print(dict1["Name"])



# printing the whole dictionary and its data type
# print(type(dict1)  ,   dict1)








'''

printing the dictionary value using for loop

'''

for dict1 in dict1:
  print(dict1)     #this prints the keys in termial 
  
  
for i in range(len(dict1)):
  print(dict1[i])   # this prints the index of the key 
  
  
  
  for dict in dict1:
    print(dict1,dict1[dict],sep=" ")