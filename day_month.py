

"""
input: index number of a day (from 1 to 365)
output: index number of month and day of the input

e.g.
    input:
        123
    output:
        Month: 4
        Day: 30

    which means 30th day of 4th month
    
"""

from os import system

input_day = int(input("Enter the day: "))

# six first months
temp = input_day - 186   

system('cls')


if input_day not in range(1, 366): # there are only 365 days in a year
    print('\nERROR!')

else:

    # other days (31)
    if input_day in range(1, 187) and input_day % 31 != 0:

        month = input_day // 31 + 1
        day = input_day % 31

        print('\nMonth: ', month)
        print('Day: ', day)

    # last days in each month (31)
    elif input_day in range(1, 187) and input_day % 31 == 0:
        month = input_day // 31
        day = 31

        print('\nMonth: ', month)
        print('Day: ', day)

    # other days (30)
    elif input_day in range(187, 366) and temp % 30 != 0:

        month = (temp // 30) + 6 + 1
        day = temp % 30

        print('\nMonth: ', month)
        print('Day: ', day)

    # last days in each month (30)
    elif input_day in range(187, 366) and temp % 30 == 0:

        month = temp // 30 + 6
        day = 30

        print('\nMonth: ', month)
        print('Day: ', day)
