import math

ilist = [49,0,1,-1,-49,-2]
def my_list(item):
    return abs(50 - item)

ilist.sort(key=my_list)
print(ilist)