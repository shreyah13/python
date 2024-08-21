# Program to check if the number is a perfect square

import math
num = int(input('Enter a number to check for perfect square: '))
root = math.sqrt(num)
if root == int(root):
    print(num,' is a perfect square')