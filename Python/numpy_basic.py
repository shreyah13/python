import numpy as np
array1= np.zeros((1,4))
print(array1)
for row in array1:
    print(type(row))
    for element in row:
        print(element, type(element))


array2= np.zeros((3,3))
print(array2)
i = 1
for row in array2:
    print(f'Row:{i}', type(row))
    for element in row:
        print(element, type(element), end = '  ')
    i += 1
    print()


array3 = np.full((3,5), 15)
print(array3)
print(array3[0])
print(array3[0][1])
#print(array3[3][0])


array4 = np.arange(1, 10)
array5 = np.arange(1, 20, 3)
print(array4, array5)


matrix1 = np.array([[2, 3, 4], [3, 4, 7]])
matrix2 = np.array([[5, 1, 8], [9, 2, 6]])
print(matrix1 ,'\n', matrix2 )


matrix3 = np.array([[5, 1], [8, 9], [2, 6]])
matrix4 = np.array([[2, 3, 4], [3, 4, 7]])
product = np.dot(matrix3, matrix4)
print(f'Product matrix is:{product}')


array6 = np.array([[2, 3, 4]])
array7 = np.array([[5, 1, 8]])
product = array6 * array7
print(f'Product array is:{product}')


array8 = np.array([[2, 3, 4]])
array9 = np.array([[5, 1, 8]])
sum = array8 + array9
print(f'Sum array is:{sum}')


array10 = np.array([2, 3, 14, 24, 7, 11])
print(array10)
array11 = array10.reshape(2,3)
print(f'Reshaped array \n {array11}')


array12 = np.array([2, 3, 14, 24, 7, 11])
mean = array12.mean()
#median = array.median()
std_dev = array12.std()
#print(f'Mean = {mean} \n Median = {median} \n Std dev = {std_dev}')


array13 = np.array([2, 12, 3, 15, 25, 45, 30, 33])
root = np.sqrt(array13)
epx = np.exp(array13)
print(f'Root is {root} \n Exponent is {epx}')
print(f'Element at index 3 is {array13[3]}')
print(f'Sliced array is {array13[:3]}')


vector = np.arange(5)
print(f'Vector: {vector}')
print(f'Vector shape: {vector.shape}')
# matrix5 = np.ones()
# need to continue from notes_kleit


array14 = np.arange(12)
a1 = array14.reshape(2, 6)
print(f'Reshaped array1 is \n {a1}')
a2 = a1.reshape(2, 6)
print(f'Reshaped array1 is \n {a2}')
a3 = a2.reshape(2, 6)
print(f'Reshaped array1 is \n {a3}')
a4 = a3.reshape(2, 6)
print(f'Reshaped array1 is \n {a4}')
a5 = a4.reshape(2, 6)
print(f'Reshaped array1 is \n {a5}')


array15 = np.arange(1, 10).reshape(3, -1)
print(array15)


array16 = np.arange(1, 10).reshape(3, -1)
print(array16)
array16 = np.array([2, 5, 7])
matrix5 = np.array([[4, 6, 8], [12, 16, 20]])
result = matrix5 + array16
# Broadcasting of array with matrix
print(f'Result is \n {result}')


array17 = np.arange(1, 10)
array18 = np.arange(2, 25, 2)
print(f'array1 is \n {array17}')
print(f'array2 is \n {array18}')
array19 = array17.reshape(3, -1)
print(f'Reshaped array1 is \n {array19}')
array20 = array18.reshape(4, -1)
print(f'Reshaped array2 is \n {array20}')
array21 = array18.reshape(2, -1)
print(f'Reshaped array3 is \n {array21}')
array22 = array18.reshape(-1, 4)
print(f'Reshaped array4 is \n {array22}')


data1 = np.array([1, 2, 3, 4, 5, 6])
data2 = np.array([2, 9, 3, 4, 0, 8])
data = np.stack((data1, data2), axis = 0)
print(f'Data = \n {data}')
corelation_matrix = np.corrcoef(data)
print(f'Corelation Matrix is \n {corelation_matrix}')


data3 = np.array([[1, 2, 3, 4],[11, 22, 33, 44],[10, 20, 30, 40]])
print(f'Data is {data3}')
data4 = data3[ : 4]
print(f'Modified data1 is \n {data4}')
data5 = data3[3 : ]
print(f'Modified data2 is \n {data5}')
