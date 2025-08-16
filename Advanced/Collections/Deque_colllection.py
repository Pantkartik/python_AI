'''
Deque is a doubly ended queue and used to enter the data from top and bottom



'''

from collections import deque

d=deque()


#  inserting the element from both side is allowed


d.append(23)
d.append(2)
d.append(9)
d.append(3)


d.appendleft(89)

d.popleft()
d.rotate()
d.extend()
print(d)