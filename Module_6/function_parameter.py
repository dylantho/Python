"""
Program: function_parameter.py
Author: Dylan Thomas
Last date modified: 10/04/2020
"""

def multiply_string(message, n):
    """Takes in a string and a number (n) and multiplies it by n times. Returns the multiplied string."""
    for i in range(n):
        new_message = (message * n)
    return new_message

if __name__ == '__main__':
    n = 0
    message = str(input("Please enter your favorite class: "))
    while True:
        try:
            n = int(input("Please enter a number between 2 and 7: "))
            while n < 2 or n > 7:
                print()
                n = int(input("Error: Make sure the number is between 2 and 7: "))
                print()
            break
        except ValueError:
            print("Error: please avoid symbols and letters")
            print()

    print()
    print(multiply_string(message, n))
