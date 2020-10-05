"""
Program: input_while.py
Author: Dylan Thomas
Last date modified: 09/27/2020
"""

myList = []
stoppingValue = -1

user_Number = int(input('Enter a number between 1 and 100 or -1 to stop: '))

while user_Number != stoppingValue:
    while user_Number not in range(1, 101):
        user_Number = int(input('Invalid input, Please enter a number between 1 and 100 or -1 to stop: '))
    myList.append(user_Number)
    user_Number = int(input('Enter a number between 1 and 100 or -1 to stop: '))

for i in myList:
    print(i)

#   Tested      Expected                Result
#   5, 6, 7     5                       5
#               6                       6
#               7                       7

#   -1          End program             Ended program
#   5, -1       5, program ends 5,      program ends
#   5, 5, -1    5, 5, program ends      5, 5, program ends

#   1, 100, -1  1                       1
#               100 program ends        100 program ends
