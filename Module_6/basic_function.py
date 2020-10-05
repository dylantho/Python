"""
Program: basic_function.py
Author: Dylan Thomas
Last date modified: 10/04/2020
"""

def hourly_employee_input():
    """Asks for name, hours worked, pay rate, and prints a message with the given information with all inputs validated"""
    name = "Name"
    hours_Worked = 0
    hourly_Pay = 0

    while True:
        name = input("Please enter your name: ")
        if name.isalpha():
            print()
            break
        else:
            print("Please enter a valid name")
            print()

    while True:
        try:
            hours_Worked = int(input("Please enter how many hours you worked: "))
            while hours_Worked < 0:
                print("Please enter a number of zero or higher.")
                print()
                hours_Worked = int(input("Please enter how many hours you worked: "))
                print()
            break
        except ValueError:
            print("Please enter a number!")
            print()

    print()

    while True:
        try:
            hourly_Pay = float(input("Please enter your hourly pay rate: "))
            while hourly_Pay < 0:
                print("Please enter a number of zero or higher.")
                print()
                hourly_Pay = float(input("Please enter your hourly pay rate: "))
            break
        except ValueError:
            print("Please enter a number!")
            print()

    print()
    print("----------------------------------------------------------")
    print("Employee name: ", name, " Employee wage: $", hourly_Pay, " Hours worked: ", hours_Worked)

if __name__ == '__main__':
    hourly_employee_input()
