'''       LETS COMPARE LIST  AND TUPLE '''


import sys
my_list=["kartik","pant",1,2,3]
my_tuple=("kartik","pant",1,2,3)
print(sys.getsizeof(my_list),bytes)
print(sys.getsizeof(my_tuple),bytes)



'''    according to the size took by list and tuple 

      tuple takes-----> 80 bytes
      list takes-----> 104 bytes
      
      
      tuple>>list ( on basis of memory allocation )
      
'''





'''          Time complexity  or time to run '''

import timeit
print(timeit.timeit(stmt="[1,2,3,4,6,7,8,8,9]", number=1000000))
print(timeit.timeit(stmt="(1,2,3,4,6,7,8,8,9)", number=1000000))



'''    according to time took for running list and tuple 

        list took   ---->  0.040223900000455615  seconds
        tuple took  ---->  0.0067376000006333925 seconds

        tuple << list ( on basis of time taken to run the code )
'''






'''       

TUPLE IS MORE FAVOURABLE 

'''