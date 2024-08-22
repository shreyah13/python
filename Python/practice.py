# program to find 2nd smallest digit in a number
for i in range(10):
    print(i)
    i+=1

num = int(input('Enter the number whose biggest and smallest digits are to be found: '))
t = num
temp1 = 9
temp2 = 0
while num != 0:
    j = t2 % 10
    if j <= temp1:
        temp1 = j
    t2 = t2 // 10
print(temp1,' is the Smallest digit in ',t)