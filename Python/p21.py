# Program to print a hollow square of n lines

n = int(input('Enter the number of lines to print a hollow square: '))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*',end =' ')
        else:
            print(' ',end =' ')
    print()

n = int(input('Enter the number of lines to print a complete square: '))
for i in range(n):
    for j in range(n):
        print('*',end =' ')
    print()