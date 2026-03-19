print('Program to calculate Simple Interest')

principal_amt = int(input('Enter Principal Amount:'))
rate = int(input('Enter Rate of Interest:'))
time_period = int(input('Enter Time Period:'))

simple_int = principal_amt * rate * time_period / 100
print(f'Simple Interest for the provided input is {simple_int}')