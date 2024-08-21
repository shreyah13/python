# Program to print math table of a number

number = int(input('Enter the number whose Math Table is required: '))
print('MATH TABLE FOR ',number)
for i in range (1,11):
    print(number,'x',i,'=',number*i)