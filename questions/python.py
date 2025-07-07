# str="kartik"
# str2=str.endswith("k")
# str2=str.capitalize()
# str2=str.replace('k','t')
# str2=str.
# print(str2)


# list is like array but contains various datatypes
#  list is mutable 

# list1=[4,42,1,34]
# # print(len(list1))ṇ
# list1.append(5)
# list1.sort()
# list1.sort(reverse=True)
# list1.reverse()
# list1.pop(2)
# print(list1)
# print(list1,list2)  #list 1 is updated and value set to none
# print(list1.sort())


# tuple 
# same as tuple but immutable
# tup1=(2,42,21,1)
# print(type(tup1))
# print(tup1[0])

# tup=(1)                 # treated as integer 
# print(type(tup))
# tup2=(1,)                  #treated as tuple
# print(type(tup2))   
tup3=(1,2,5,43,85)
tup3=tup3[1:4]   #this will give   (2,5,43)
print(tup3)
print(tup3.index(43))
print(tup3.count(2))