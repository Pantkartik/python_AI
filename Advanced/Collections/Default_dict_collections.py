'''

Default Dict 

same as dict but have deafult key value if not given 
'''


from collections import defaultdict

dict_default=defaultdict(int)
dict_default["name"]="kartik"
print(dict_default['age'])  
# return default value of integer 0 cuz no such key value present