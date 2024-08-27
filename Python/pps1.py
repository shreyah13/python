import math
from math import sqrt 

def count_perfect_squares(list):
    count = 0
    for i in list:
        root_num = math.sqrt(i)
        root_num = math.floor(root_num)
        product = root_num * root_num
        if product == i:
            count += 1
    return count
        
cust_num = int(input("Enter the number of customers: "))
cust_bill = []
for i in range(cust_num):
    amt = int(input("Enter the bill amount: "))
    cust_bill.append(amt)
print(cust_bill)
count_perfect_squares(cust_bill)
print('is/are the number(s) of customers getting discount.')