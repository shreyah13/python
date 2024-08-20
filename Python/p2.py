# Read the number from user and check whether the number is even or not.
# To read data from conole, we can use input(). However the input() always reads only a string as usual with all other languages.

my_number=int(input('Enter the number to check if it is even or not: '))
if my_number % 2 == 0:
    print(my_number,' is an Even number.')
else:
    print(my_number,' is not an Even number.')