"""
Program: function_return_value.py
Author: Dylan Thomas
Last date modified: 10/04/2020
"""


def weekly_pay(hours_worked, hourly_pay_rate):
    """Calculates the user's weekly pay based on inputs from the hourly_employee_input function"""
    weekly_pay_total = (hours_worked * hourly_pay_rate)
    return weekly_pay_total


def hourly_employee_input():
    """Asks for name, hours worked, pay rate, calls a function to calculate the weekly total and returns a statement to the user"""
    name = "Name"
    hours_worked = 0
    hourly_pay_rate = 0

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
            hours_worked = int(input("Please enter how many hours you worked: "))
            while hours_worked < 0:
                print("Please enter a number of zero or higher.")
                print()
                hours_worked = int(input("Please enter how many hours you worked: "))
                print()
            break
        except ValueError:
            print("Please enter a number!")
            print()

    print()

    while True:
        try:
            hourly_pay_rate = float(input("Please enter your hourly pay rate: "))
            while hourly_pay_rate < 0:
                print("Please enter a number of zero or higher.")
                print()
                hourly_pay_rate = float(input("Please enter your hourly pay rate: "))
            break
        except ValueError:
            print("Please enter a number!")
            print()

    print()

    weekly_total = str(weekly_pay(hours_worked, hourly_pay_rate))

    print("----------------------------------------------------------")
    return "Employee name: " + name + " Weekly pay: $" + weekly_total


if __name__ == '__main__':
    display_string = hourly_employee_input()
    print(display_string)
