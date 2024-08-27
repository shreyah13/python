def insertion_sort(array):
    for i in range(1,len(array)):
        element = array[i]
        j = i - 1
        while j >= 0 and element < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = element
    return array

n = int(input('Enter the size of list: '))
array = []
print('Enter the elements of the list: ')
for i in range(n):
    num = int(input())
    array.append(num)

index = insertion_sort(array)
print(f'{array} is sorted.')

