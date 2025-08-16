from functools import reduce
list_reduce=[1,2]

product_A=reduce(lambda x , y : x*y,list_reduce)
print(product_A)