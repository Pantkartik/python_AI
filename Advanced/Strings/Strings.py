''' string is ordered , immutable,text representaion '''

str_name=' I am kartik pant '
print(str_name)
string1=str("KARTIK")
print(string1,type(string1))    



''' Accesing the substrings '''

my_str="kartik"
# index=my_str[0]
print(my_str[0:]) 



''' Concating two strings '''

first_name=str(input("Enter the first name : "))
last_name=str(input("Enter the last  name : "))
full_name=first_name+last_name
print("fullname : ",full_name)



''' Iterate over string '''

string1="kartik"
for i in string1: 
  print(i)
  
  
''' To check a sub-string '''
string_sub="Jai shri ram "
if "Jai" in string_sub:
  print("present")
else:
  print("Not present")
  
  
  
''' Method for string '''

#  1. To remove the whitespace 
test_str="               kartik             "
updated_str=test_str.strip()
print(updated_str)
  
#  2. To uppercase whole string 

my_str_to_uppercase=" hello "
my_str_to_uppercase=my_str_to_uppercase.upper()
print(my_str_to_uppercase)


# 3. To lowercase whole string

my_str_to_lowercase=" HELLO "
my_str_to_lowercase=my_str_to_lowercase.lower()
print(my_str_to_lowercase)


# 4. To uppercase the first letters of the string 

my_str_to_title=" hello bhai  "
print(my_str_to_title.title())

# 5. To make the string capatilize

my_str_to_capatilize=" hello bhai  "
print(my_str_to_capatilize.capitalize())


# 6. Ends with 
string4="I am learning python "
for i in string4:
  if string4.endswith("p "):
    print("True")
    break
  else:
    print('false')
    break


# 7. To find the subset string index
string5="here is my method"
print(string5.find("method")) 