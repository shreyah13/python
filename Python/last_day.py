import pandas as pd

def fact_iterative(num):
    fact_num = 1
    if num == 0 or num == 1:
        return fact_num
    for i in range(2, num + 1):
        fact_num = fact_num * i
    return fact_num

def fact_recursive(num):
    if num == 0 or num == 1:
        return 1
    return num * fact_iterative(num - 1)

input_num = int(input('Enter number to find its factorial: '))
choice = int(input('Enter your choice: \n1. Iterative \n2. Recursive \n'))

fact_num = 0
if choice == 1:
    fact_num = fact_iterative(input_num)
elif choice == 2:
    fact_num = fact_recursive(input_num)
print(f'Factorial of {input_num} is {fact_num}.')






# Microsoft Windows [Version 10.0.22631.4037]
# (c) Microsoft Corporation. All rights reserved.

# C:\Shreya_Learning\Python_repo\Python>pip list
# Package         Version
# --------------- -----------
# mysql           0.0.3
# mysqlclient     2.2.4
# numpy           2.1.0
# pandas          2.2.2
# pip             24.2
# PyMySQL         1.1.1
# python-dateutil 2.9.0.post0
# pytz            2024.1
# six             1.16.0
# tzdata          2024.1

# C:\Shreya_Learning\Python_repo\Python>python -m pdb last_day.py
# > c:\shreya_learning\python_repo\python\last_day.py(1)<module>()
# -> import pandas as pd
# (Pdb) list
#   1  -> import pandas as pd
#   2
#   3     def fact_iterative(num):
#   4         fact_num = 1
#   5         if num == 0 or num == 1:
#   6             return fact_num
#   7         for i in range(2, num + 1):
#   8             fact_num = fact_num * i
#   9         return fact_num
#  10
#  11     def fact_recursive(num):
# (Pdb) l
#  12         if num == 0 or num == 1:
#  13             return 1
#  14         return num * fact_iterative(num - 1)
#  15
#  16     input_num = int(input('Enter number to find its factorial: '))
#  17     choice = int(input('Enter your choice: \n1. Iterative \n2. Recursive \n'))
#  18
#  19     fact_num = 0
#  20     if choice == 1:
#  21         fact_num = fact_iterative(input_num)
#  22     elif choice == 2:
# (Pdb) l
#  23         fact_num = fact_recursive(input_num)
#  24     print(f'Factorial of {input_num} is {fact_num}.')
# [EOF]

# (Pdb) b 6
# Breakpoint 1 at c:\shreya_learning\python_repo\python\last_day.py:6

# (Pdb) next
# > c:\shreya_learning\python_repo\python\last_day.py(3)<module>()
# -> def fact_iterative(num):

# (Pdb) step
# > c:\shreya_learning\python_repo\python\last_day.py(11)<module>()
# -> def fact_recursive(num):

# (Pdb) s
# > c:\shreya_learning\python_repo\python\last_day.py(16)<module>()
# -> input_num = int(input('Enter number to find its factorial: '))
# (Pdb) s

# Enter number to find its factorial: 5
# > c:\shreya_learning\python_repo\python\last_day.py(17)<module>()
# -> choice = int(input('Enter your choice: \n1. Iterative \n2. Recursive \n'))
# (Pdb) 1
# 1

# (Pdb) c
# Enter your choice:
# 1. Iterative
# 2. Recursive
# 2
# Factorial of 5 is 120.
# The program finished and will be restarted
# > c:\shreya_learning\python_repo\python\last_day.py(1)<module>()
# -> import pandas as pd

# (Pdb) c
# Enter number to find its factorial: 5
# Enter your choice:
# 1. Iterative
# 2. Recursive
# 1
# Factorial of 5 is 120.
# The program finished and will be restarted
# > c:\shreya_learning\python_repo\python\last_day.py(1)<module>()
# -> import pandas as pd
# (Pdb)