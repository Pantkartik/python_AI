# '''
# A json file is  a set of dependecies and install modules and file data situated in a well designed way


# '''






'''
encording the json file

'''

import json
data={
    "id": 567,
    "name": "User26",
    "age": 39,
    "email": "user529@example.com",
    "is_active": False,
    "preferences": {
        "newsletter": False,      
        "notifications": "none"   
    }
}

dataJSON= json.dumps(data,indent=4,sort_keys=True)
print(dataJSON)


with open('data.json','w') as file:
  json.dump(dataJSON,file)
  
  
  
  
  
  
  
  
  
  
  
  '''
  
  to convert a dictionary into a json file 
  
  '''
  
import json
  
user_data=dict(name="kartik",age=30,height="6 feet",nationality="Indian")
  
  # to convert it to json file we use the json.dumps ()
user_dataJson= json.dumps(user_data,indent=4)
  
  
  
'''
Now saving this json file in a folder

'''

with open('Advanced/JSON_PYTHON/user_data.json','w') as file:
  json.dump(user_dataJson,file)

  
  
  
  
  
  
  
  
# import json
# import random

# # Sample function to generate random JSON data
# def generate_random_json():
#     data = {
#         "id": random.randint(1, 1000),
#         "name": f"User{random.randint(1, 100)}",
#         "age": random.randint(18, 70),
#         "email": f"user{random.randint(1, 1000)}@example.com",
#         "is_active": random.choice([True, False]),
#         "preferences": {
#             "newsletter": random.choice([True, False]),
#             "notifications": random.choice(["all", "email", "sms", "none"])
#         }
#     }
#     return json.dumps(data, indent=4)

# # Generate and print random JSON data
# print(generate_random_json())





# '''  

# Json  

# '''

# {
#     "id": 567,
#     "name": "User26",
#     "age": 39,
#     "email": "user529@example.com",
#     "is_active": false,
#     "preferences": {
#         "newsletter": false,      
#         "notifications": "none"   
#     }
# }