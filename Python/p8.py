# Program to check whether if the user given year is a leap year

year = int(input('Enter the year want to check for leap year: '))
if year % 4 == 0 or year % 100 == 0:
    print(year,' is a leap year')