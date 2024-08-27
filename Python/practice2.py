# my_list = []
# list2 = [2, 5, 8, 9]
# list3 = list(list2)
# list4 = [4, 7, 3, 0]
# list2.extend(list4)
# print(list2)
# list2[:4] = my_list
# print(my_list)
 
import math
from math import sqrt
from math import floor
count = 0
list = [20, 13, 15, 42, 81, 9, 25, 36]
for i in list:
    root_num = math.sqrt(i)
    root_num = math.floor(root_num)
    product = root_num * root_num
    if product == i:
        count += 1
print(count)
 
