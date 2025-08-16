'''
Product iter tool is used to product cartesian of two list 

'''


from itertools import product
a=[1,5]
b=[3,0]
prod=product(a,b,repeat=2)
print(list(prod))