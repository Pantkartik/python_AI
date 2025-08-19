  
import json
  
user_data=dict(name="kartik",age=30,height="6 feet",nationality="Indian")
  
  # to convert it to json file we use the json.dumps ()
user_dataJson= json.dumps(user_data,indent=4)
  
  
  
'''
Now saving this json file in a folder

'''

with open('Advanced/JSON_PYTHON/user_data.json','w') as file:
  json.dump(user_dataJson,file)