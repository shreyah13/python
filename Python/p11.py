# Program to find sum of digits of a number

num = int(input('Enter the number whose sum of digits is to be found: '))
t = num
sum = 0
while num!=0:
    j = num % 10
    sum = sum + j
    num = num // 10
print(sum,' is the sum of digit in',t)

