"""
Program: if_elif_assignment.py
Author: Dylan Thomas
Last date modified: 09/20/2020
"""

def tellPrice(userSelection):

    if userSelection == "Platinum" or userSelection == "platinum":
        print("The cost of the platinum plan is $60.")
        return 1
    elif userSelection == "Gold" or userSelection == "gold":
        print("The cost of the gold plan is $50.")
        return 2
    elif userSelection == "Silver" or userSelection == "silver":
        print("The cost of the silver plan is $40.")
        return 3
    elif userSelection == "Bronze" or userSelection == "bronze":
        print("The cost of the bronze plan is $30.")
        return 4
    elif userSelection == "Free Trial" or userSelection == "free trial" or userSelection == "Free trial" or userSelection == "free Trial":
        print("The free plan is free for one month.")
        return 5
    else:
        print("Please enter a valid plan name.")
        print()

        return 6


if __name__ == '__main__':
    print("Hello, here are the sign up options for the Programmer's Toolkit Monthly Subscription box.")
    print()
    print("Platinum - Includes t-shirts, stickers, figurines, and programming books")
    print("Gold - Includes t-shirts, stickers, and figurines")
    print("Silver - Includes t-shirts, and stickers")
    print("Bronze - Includes t-shirts")
    print("Free Trial - Includes t-shirts and stickers for one month")
    print()
    userSelection = input("Type the name of the plan you would like to see the cost of: ")
    planSelected = tellPrice(userSelection)










