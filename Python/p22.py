# Program to print X shape of n lines

n = int(input('Enter the number of lines to print the star: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j or j == n - i + 1:
            print('* ',end = '')
        else:
            print(' ',end = '')
    print()