# Program to print a hollow square of n lines

n = int(input('Enter the number of lines to print the star: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n:
            print('* ',end ='')
        if j == n or j == 1:
            print('* ',end =' ')
        else:
            print(' ',end =' ')
    print()