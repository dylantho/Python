"""
Program: input_while_exit.py
Author: Dylan Thomas
Last date modified: 09/27/2020
"""


def main():
    myList = []
    stoppingValue = -1
    exitSentinel = -2


    user_Number = int(input('Enter a number between 1 and 100, enter -1 to stop or -2 to quit the program: '))
    while user_Number != stoppingValue:
        if user_Number == exitSentinel:
            break
        while user_Number not in range(1, 101):
            if user_Number == exitSentinel:
                break
            user_Number = int(input('Invalid input, Please enter a number between 1 and 100, enter -1 to stop or -2 to quit the program: '))
        myList.append(user_Number)
        user_Number = int(input('Enter a number between 1 and 100, enter -1 to stop or -2 to quit the program: '))
    if user_Number == stoppingValue:
        for i in myList:
            print(i)


main()

#   Tested      Expected                Result
#   -2          Program ends            Program ends
#   1, 5, -2    Program ends            Program ends

#   5, 6, 7     5                       5
#               6                       6
#               7                       7

#   -1          Program ends            Program ends
#   5, -1       5, program ends         Program ends
#   5, 5, -1    5, 5, program ends      5, 5, program ends

#   1, 100, -1  1                       1
#               100 program ends        100 program ends
