from functools import reduce
l = [5,4,3,6,7,8,9,2,0,1]
print(reduce(lambda x,y : x if x < y else y,l))