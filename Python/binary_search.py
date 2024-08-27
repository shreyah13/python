def binary_search(num, search_num):
    start_index = 0
    end_index = len(num) - 1
    
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if num[mid_index] == search_num:
            return mid_index
        elif search_num < num[mid_index]:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1

n = int(input('Enter input size: '))
num = []
print('Enter the numbers: ')
for i in range(n):
    j = int(input())
    num.append(j)

print('The input data is \n', num)
search_num = int(input('Enter the search number: '))

index = binary_search(num, search_num)
if index == -1:
    print(f'{search_num} was not found in the list')
else:
    print(f'{search_num} was found at position {index+1}')