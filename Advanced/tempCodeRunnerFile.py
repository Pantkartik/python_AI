import timeit
print(timeit.timeit(stmt="[1,2,3,4,6,7,8,8,9]", number=1000000))
print(timeit.timeit(stmt="(1,2,3,4,6,7,8,8,9)", number=1000000))
