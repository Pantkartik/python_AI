# Errors are the return terminal commands which generate generally when we typo error syntax error import module error and many more 





'''
Exception forcing rasie 

'''

x=-5
if x <0 : 
  raise Exception(" a should be positive ")


y=-10
assert(y>=0)," y should be less than 0 "




try:
  a=5/0   # this will give zero division error
  b=6+'hello'  # this will give type error 
except Exception as e:
  print(e)     # for printing the error 
  
except Exception as n:
  print(n)
else:
  print("NO error dosto! ")