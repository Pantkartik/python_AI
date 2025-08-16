

'''   

NAMED TUPLE   : datatype easy to create and use simple and is like the struct 

'''

from collections import namedtuple
Point = namedtuple('Point','x,y')  # this created a new data type point x and y we can assign values to them 
pt=Point(1,10)
print(pt)


#  accesing only the element of tuple 
print(pt.x,pt.y)





from collections import namedtuple
Point=namedtuple('Point','x,y')
pt=Point(1,20)
print(pt,pt.x,pt.y)