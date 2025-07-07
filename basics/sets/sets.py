# sets are the unordered system t store the data and is elements are immutable and unordered doesnt have indexing 
#  lets create a set 
# set1={ 1,3,41,'hello'}
# print(set1 , type(set1))

#  the set ignors the duplicate value and return only in 1 time in unordered manner 
# set2={1,424,22,22,"hello","world","hello"}
# print(len(set2))

# create an empty set 
# collection=set()
# print(collection,type(collection))

# method of sets

# set.add(el)                ---------> adds an element
# set.remove(el)             ---------> removes the element
# set.clear()                ---------> empties the set
# set.pop()                  ---------> removes random values
# set.intersection()         ---------> combines common values and return new
# set.union()                ---------> combines both set values and return new set


# collection=set()

# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add(4)
# collection.remove(2)
# collection.pop()
# collection.clear()
# print(collection)


# union means the common value is treated as the one time and return new set 
set1={1,2,3,4}
set2={4,5,6,3}

print(set1.union(set2))
# when we union set 1 and set 2 it returns set_new={1,2,3,4,5,6}  

print(set1.intersection(set2))
#  when we interect set1 and set2 it returns set_inter={3,4}