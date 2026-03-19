def bin2dec(val):
    return int(val,2)
def oct2hex(val):
    return hex(int(val,8))
try:
    number1 = input('Enter a binary number: ')
    print(bin2dec(number1))
except ValueError:
    print('Invalid literal with base 2: ')
try:
    number2 = input('Enter an octal number: ')
    print(oct2hex(number2))
except ValueError:
    print('Invalid literal with base 2: ')