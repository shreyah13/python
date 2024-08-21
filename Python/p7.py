# Program to check if the number is a perfect square

import math
from math import sqrt 
num = int(input('Enter a number to check for perfect square: '))

#root = math.sqrt(num)
#if root == int(root):
#    print(num,' is a perfect square')

root_num = math.sqrt(num)
root_num = math.floor(root_num)
product = root_num * root_num
if product == num:
    print(num,'is a Perfect square.')