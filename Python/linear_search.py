#def linear_search(names, search_name):
#    for i in range(len(names)):
#        if names[i] == search_name:
#            return i
#    return -1
#
#n = int(input('Enter input size: '))
#
#names = []
#print(f'Enter the {n} names')
#for i in range(n):
#    names.append(input())
#
#print('The input data is \n', names)
#search_name = input('Enter the search name: ')
#
#index = linear_search(names, search_name)
#if index == -1:
#    print(f'{search_name} was not found in the list')
#else:
#    print(f'{search_name} was found at position {index+1}')



def linear_search(names, search_name):
    for i in range(len(names)):
        if names[i] == search_name:
            return i
    return -1

n = int(input('Enter input size: '))

names = {}
for i in range(n):
    key = int(input('Enter the index: '))
    value = input('Enter the value: ')
    names[key] = value

print('The input data is \n', names)
search_name = input('Enter the search name: ')

index = linear_search(names, search_name)
if index == -1:
    print(f'{search_name} was not found in the list')
else:
    print(f'{search_name} was found at position {index+1}')



# Another method:

#n = int(input('Enter size of the dictionary: '))
#for i in range(n):
#    student
#    name = input()
#    students[student_id] = name
#print('The input datais \n', students)
#search_id = int(input('Enter the student Id: '))
#try:
#    name = students[search_id]
#    printf(f'Student with Id {search_id} name is {students[search_id]}')
#except Keyerror:

