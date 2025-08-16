'''  Counter collections '''

'''
its is a way to count the no. of occurence of character in a string return the character as key and count as value .

'''

from collections import Counter
string="kartik pant is a good boy"
count= Counter(string)
print(count)


from collections import Counter
trial_counter="hello this is a trial counter check "
# return a dict with all character including key value pair and value as number of times its occured 
count=Counter(trial_counter)
print(count)



'''
Methods in counter 

'''

# 1. to find the most common element in a counter dict 
print(count.most_common(1))



# most_common()    -----> return 1 common
#  most common(1)   -----> return tuple list common 
#  most_common(2)   -----> return the 2 common 


# as it is a dictionary thus we can use the dictionary methods

# 1. ---->  .items()
# 2. ---->  .values()
# 3. ---->   .keys()


