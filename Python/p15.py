# Program to find sum of even(/odd) digits of a number

num = int(input('Enter the number whose sum of even and odd digits are to be found: '))
digit = []
sum_even = 0
sum_odd = 0
while num!=0:
    i = num % 10
    digit.append(i)
    num = num // 10
for i in digit:
    if i % 2 == 0:
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i
print('Sum of Even digits of a number is:',sum_even)
print('Sum of Odd digits of a number is:',sum_odd)