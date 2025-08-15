'''  Union of sets '''

odds={1,3,5,7,9}
evens={0,2,4,6,8}
prime={2,3,5,7}


u= odds.union(evens,prime)
print(u)



'''  Intersection '''

i = odds.intersection(prime)
print(i)



'''  Difference '''

setA={1,2,3,6,8,5,6,90}
setB={2,5,21,3,8,10}

diff=setA.difference(setB)
print(diff)


''' Symetric difference '''

setA={1,2,3,6,8,5,6,90}
setB={2,5,21,3,8,10}

# diff=setA.symmetric_difference(setB)
# print(diff)


setA.update(setB)
print(setA)

