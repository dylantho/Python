"""
Program: camper_age_input.py
Author: Dylan Thomas
Last date modified: 09/14/2020
"""


def convert_to_months(years):
    months = years * 12
    return months

if __name__ == '__main__':
    years = int(input("Enter the age in years: "))
    months = convert_to_months(int(years))
    print(years, "years is equal to", months, " months.")


#Tested 5 years expecting 60 months resulting in 60 months (pass)
#Tested 5 years expecting 61 months resulting in 60 months (fail)
