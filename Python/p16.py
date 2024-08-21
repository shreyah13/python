# Program to reverse a number

num = int(input('Enter the number which needs to be reversed: '))
t = num
digit = []
while num!=0:
    i = num % 10
    digit.append(i)
    num = num // 10
for i in digit:
    
print(digit[0],' is the Smallest digit in ',t)
print(digit[-1],' is the Biggest digit in ',t)
