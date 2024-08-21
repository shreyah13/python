# program to find biggest and smallest digit in a number

num = int(input('Enter the number whose biggest and smallest digits are to be found: '))
t = num
digit = []
while num!=0:
    i = num % 10
    digit.append(i)
    num = num // 10
digit.sort()
print(digit[0],' is the Smallest digit in ',t)
print(digit[-1],' is the Biggest digit in ',t)
