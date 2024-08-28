num = int(input('Enter the total number of Oranges: '))
print('Enter the size of Oranges: ')
orange_size = []
for i in range(num):
    size = int(input())
    orange_size.append(size)
sorted(orange_size)

check_size = orange_size[-1]

child_orange = []
sell_orange = []
count = 0

for i in orange_size:
    if i < check_size:
        child_orange.append(i)
    elif i > check_size:
        sell_orange.append(i)
    elif i == check_size: 
        count += 1

print(f'{sorted(child_orange)} is the list of oranges that will be provided to the children.')
print(f'{sorted(sell_orange)} is the list of oranges that will be sold.')
print(f'{count} is the number of oranges that are be available for yourself.')