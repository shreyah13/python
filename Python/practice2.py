my_list = []
list2 = [2, 5, 8, 9]
list3 = list(list2)
list4 = [4, 7, 3, 0]
list2.extend(list4)
print(list2)
list2[:4] = my_list
print(my_list)