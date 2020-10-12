"""
Program: basic_list_exception.py
Author: Dylan Thomas
Last date modified: 10/12/2020
"""

def get_input():
    userInput = input("Please enter number: ")
    return userInput

def make_list():
    myList = []

    for x in range(3):
        userInput = get_input()

        try:
            userInput = int(userInput)
        except ValueError:
            raise ValueError
            print("non numeric")

        myList.insert(len(myList), userInput)

        #myList.append(userInput) Alternate method
    return myList

if __name__ == '__main__':
    make_list()

