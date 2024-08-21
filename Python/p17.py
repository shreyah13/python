# Program to find odd(even) placed digits in a number

num = int(input('Enter the number whose even and odd digits are to be found: '))
t = num
digit = []
even_digit = []
odd_digit = []
while num!=0:
    i = num % 10
    digit.append(i)
    num = num // 10
print(digit
print(digit[0],' is the Smallest digit in ',t)
print(digit[-1],' is the Biggest digit in ',t)
