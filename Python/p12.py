# Program to find count of digits of a number

num = int(input('Enter the number whose count of digits is to be found: '))
t = num
count = 0
while num!=0:    
    j = num % 10
    count += 1
    num = num // 10
if t == 0:
        count = 1
print(count,' digit are there in',t)