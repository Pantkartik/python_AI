#  Dictionary is key value pair , unordered , mutable 



'''  Creating a dictionary '''


dict_1={  
        
        "name":"kartik",
        "age":19,
        "height":" 6 feet ",
        "education":"B.tech"
        }

mydict2=dict(
        name="kartik",
        age=19,
        height=" 6 feet ",
        education="B.tech")

'''  Accesing a value in a dictionary '''

value= mydict2["name"]

value=dict_1.get("name")
print(value)


''' changing the value of a key '''
mydict2["name"]="krishna"



''' adding new key value pair '''

mydict2["nationality"]="Indian"
print(mydict2)




''' deleting the key value '''

del mydict2["name"]     # deletes the key and value 

mydict2.pop("age")     # also deletes the key and value 

mydict2.popitem()       # deletes the key value at the end 

print(mydict2)       # print the dict after deletion 




'''  to check the key value present in dictionary or not '''

# 1. Using the if in statements

dict3=dict(name="kartik",age=19,nationality="Indian")
if "name" in dict3:
  print("Name : ",dict3["name"])
else:
  print("Not present")
  
# 2. Using try except

try : 
  print(dict3["name"])
except:
  print("Error")



'''  Traverse in the dict '''


# Using for in loop
dict_traverse=dict(Name="Kartik",Age=19,Height="6 feet")
for key in dict_traverse:
  print(key)
  
#  Using method .keys() in for in loop  ( in form of a list )
for key in dict_traverse.keys():
  print(key)
  print(type(key))
  
  
#  Accesing the value using .values()
for values in dict_traverse.values():
  print(values)
  
  
  
#  Accesing both values and key in a single loop
dict_traverse=dict(Name="Kartik",Age=19,Height="6 feet")

for key,value in dict_traverse.items():
  print(key,value)
  
  
  
''' Copying a dictionary'''
dict_original=dict(Name="Kartik",Age=19,Height="6 feet")
print(dict_original)

dict_copy=dict_original

dict_copy.pop("Name")

print(dict_copy)
print(dict_original)    # changes in the orginal if changes in copy dict 

#  to avoid this we use copy method 
dict_original=dict(Name="Kartik",Age=19,Height="6 feet")

dict_copy=dict_original.copy()

dict_copy.popitem()
print(dict_copy)
print(dict_original)




''' Merge/Update two dictionary '''


dict1=dict(Name="Kartik",Age=19,Height="6 Feet")
dict2=dict(Name="Naman",Age=21,Height="6 Feet")

dict1.update(dict2)
print(dict1)
print("hello ")



