from collections import deque

d=deque()


#  inserting the element from both side is allowed


d.append(23)
d.append(2)
d.append(9)
d.append(3)

print(sorted(d))