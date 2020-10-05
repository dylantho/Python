"""
Program: string_functions.py
Author: Dylan Thomas
Last date modified: 10/04/2020
"""

def multiply_string(message, n):
    """This function takes a string and prints it to number or times specified by the user.
    :param message, any string
    :param n, a positive integer
    :returns a new string of the original string printed n times in a row
    """
    for i in range(n):
        new_message = (message * n)

    return new_message

if __name__ == '__main__':
    pass
