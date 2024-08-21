# Program to find 2nd smallest digit of a number

num = int(input('Enter the number whose biggest and smallest digits are to be found: '))
t = num
digit = []
count = 0
while num != 0:
    i = num % 10
    digit.append(i)
    num = num // 10
digit.sort()
print(digit[1],' is the second Smallest digit in ',t)