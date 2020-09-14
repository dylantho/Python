"""
Program: camper_age_input.py
Author: Dylan Thomas
Last date modified: 09/13/2020

The purpose of this program is to get a user input in years and convert it to months, printing the result.
"""

if __name__ == '__main__':

    def convert_to_months():
        years = int(input("Enter the age in years: "))
        months = years * 12
        print(years, "years is equal to", months, " months.")

        return months

    convert_to_months()

print("The value of __name__ is:", repr(__name__))

#TDD First Program
