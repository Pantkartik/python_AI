
try:
  # a=5/0   # this will give zero division error
  b=6+'hello'  # this will give type error 
except Exception as e:
  print(e)     # for printing the error 
except Exception as n:
  print(n)
    