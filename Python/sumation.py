#import pdb 
#pdb.set_trace()

def sumation(num):
    sum = 0
    while num != 0:
        remainder = num % 10
        num = num // 10
        sum += remainder
    return sum

input_number = int(input('Enter the number to find sum of its digits: '))
sumat = sumation(input_number)
print(f'Sum of digits of {input_number} is {sumat}.')





# PS C:\Shreya_Learning\Python_repo\Python> python extra2.py                             
# Enter the number to find sum of its digits: 67                                         
# Sum of digits of 67 is 13.                                                             
# PS C:\Shreya_Learning\Python_repo\Python> python -m pdb extra2.py
# > c:\shreya_learning\python_repo\python\extra2.py(4)<module>()
# -> def sumation(num):
# (Pdb) b 9      %%%(break 9)
# Breakpoint 1 at c:\shreya_learning\python_repo\python\extra2.py:9
# (Pdb) n        %%%(next)
# > c:\shreya_learning\python_repo\python\extra2.py(12)<module>()
# -> input_number = int(input('Enter the number to find sum of its digits: '))
# (Pdb) n                
# Enter the number to find sum of its digits: 678
# > c:\shreya_learning\python_repo\python\extra2.py(13)<module>()
# -> sumat = sumation(input_number)
# (Pdb) s        %%%(step)
# --Call--
# > c:\shreya_learning\python_repo\python\extra2.py(4)sumation()
# -> def sumation(num):
# (Pdb) s
# > c:\shreya_learning\python_repo\python\extra2.py(5)sumation()
# -> sum = 0
# (Pdb) q        %%%(quit)

# C:\Shreya_Learning\Python_repo\Python>python -m pdb extra2.py
# > c:\shreya_learning\python_repo\python\extra2.py(4)<module>()
# -> def sumation(num):
# (Pdb) n
# > c:\shreya_learning\python_repo\python\extra2.py(12)<module>()
# -> input_number = int(input('Enter the number to find sum of its digits: '))
# (Pdb) n
# Enter the number to find sum of its digits: n
# ValueError: invalid literal for int() with base 10: 'n'
# > c:\shreya_learning\python_repo\python\extra2.py(12)<module>()
# -> input_number = int(input('Enter the number to find sum of its digits: '))
# (Pdb) n
# --Return--
# > c:\shreya_learning\python_repo\python\extra2.py(12)<module>()->None
# -> input_number = int(input('Enter the number to find sum of its digits: '))

# (Pdb) b 5
# Breakpoint 1 at c:\shreya_learning\python_repo\python\extra2.py:5

# (Pdb) d 5
# *** Newest frame

# (Pdb) disable 5
# *** Breakpoint number 5 out of range

# (Pdb) l
#  7             remainder = num % 10
#  8             num = num // 10
#  9             sum += remainder
#  10         return sum
#  11
#  12  -> input_number = int(input('Enter the number to find sum of its digits: '))
#  13     sumat = sumation(input_number)
#  14     print(f'Sum of digits of {input_number} is {sumat}.')
# [EOF]
# (Pdb)
