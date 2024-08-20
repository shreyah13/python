# Program to accpet 3 distinct numbers and find smallest among them. 

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
number3 = int(input('Enter third number: '))

if number1 < number2 and number1 < number3:
    print(number1,' is the smallest.')
elif number2 < number3:
   print(number2,' is the smallest.')
else:
    print(number3,' is the smallest.')