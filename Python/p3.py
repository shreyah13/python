# Accept a number as input, say x and define a logic to get output y. the input can be only 0 and 1 and the putput must be 1 if the input i 0 and vice versa. Do not use boolean algebra

x = int(input('Enter either of 0 or 1: '))
if x == 0 or x == 1:
    y = 1 - x
    print(y)