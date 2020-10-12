"""
Program: basic_list.py
Author: Dylan Thomas
Last date modified: 10/12/2020
"""

def get_input():
    pass

def make_list():
    myList = []

    for x in range(3):
        userInput = get_input()

        try:
            userInput = int(userInput)
        except ValueError:
            print("non numeric")


        myList.insert(len(myList), userInput)

        #myList.append(userInput) Alternate method


    return myList


