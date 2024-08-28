input_string = input('Enter a string of parenthesis: ')
open_count = close_count = 0
arrangement = True
for char in input_string:
    if char == '(':
        open_count += 1
    elif char == ')':
        close_count += 1
    if close_count > open_count:
        arrangement = False
        break
if arrangement == True and open_count == close_count:
    print('Number of pairs: ',open_count)
else: 
    print('Improper arrangement.')