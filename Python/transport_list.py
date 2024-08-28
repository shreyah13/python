
n = int(input('Enter the size of Original list: '))
original_list = []
print('Enter elements of the Original list: ')
for i in range(n):
    element = int(input())
    original_list.append(element)

m = int(input('Enter the size of Transported list: '))
transported_list = []
print('Enter elements of the Transported list: ')
for i in range(n):
    element = int(input())
    transported_list.append(element)

sorted(original_list)
sorted(transported_list)

missing_list = []
for i in range(1,n+1):
    for j in range(1,m+1):
        