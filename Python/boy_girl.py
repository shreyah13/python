student_num = int(input('Enter the number of students: '))
boy_num = girl_num = student_num // 2
boy_height = []
girl_height = []

print('Enter the height of boys: ')
for i in range(boy_num):
    value = int(input())
    boy_height.append(value)

print('Enter the height of girls: ')
for i in range(girl_num):
    value = int(input())
    girl_height.append(value)   

student_height = boy_height.extend(girl_height)
print(student_height)
