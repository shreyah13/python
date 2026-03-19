def f(n):
    if n <= 2:
        return n-1
    else:
        return f(n-1)+f(n-2)
    
try:
    number = int(input('Enter a number: '))
    if number > 0:
        print(f'f({number}) = {f(number)}')
    else:
        print('Input should be greater than 0.')
except ValueError:
    print('Try with numeric value.')