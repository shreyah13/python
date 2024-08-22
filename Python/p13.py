# program to find biggest and smallest digit in a number

num = int(input('Enter the number whose biggest and smallest digits are to be found: '))
t = num
t2 = num
temp = 0
while num != 0:
    i = num % 10
    if i >= temp:
        temp = i
    num = num // 10
if t == 0:
        temp = 0
print(temp,' is the Biggest digit in ',t)

temp1 = 9
while t2 != 0:
    j = t2 % 10
    if j <= temp1:
        temp1 = j
    t2 = t2 // 10
if t == 0:
        temp1 = 0
print(temp1,' is the Smallest digit in ',t)