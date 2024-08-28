def partition(array, low, high):
    pivot = array[high]
    j = low
    for i in range(low,high):
        if array[i] < pivot:
            array[j], array[i] = array[i], array[j]
            j += 1
    array[j], array[high] = array[high], array[j]
    return j

def quick_sort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index-1)
        quick_sort(array, pivot_index+1, high)
    return array

n = int(input('Enter the size of the list of the Oranges: ')) 
array = []
print('Enter the elements of the list: ')
for i in range(n):
    value = int(input())
    array.append(value)
print('Input Array = ',array)
print('Sorted Array =', quick_sort(array, 0, n-1))