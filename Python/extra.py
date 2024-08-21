# Program to print N shape of N lines

n = int(input('Enter the number of lines to print the star: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j or j == n or j == 1:
            print('* ',end = '')
        else:
            print(' ',end = '')
    print()