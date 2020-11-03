"""
Program: employee.py
Author: Dylan Thomas
Last date modified: 11/2/2020
"""

import datetime


class Employee:
    # Constructor
    def __init__(self, lastname, firstname, address, phone, if_salaried, start, salary):
        self._last_name = lastname
        self._first_name = firstname
        self._address = address
        self._phone_number = phone
        self._if_salaried = if_salaried
        self._start_date = start
        self._emp_salary = salary

    def __str__(self):
        return 'Person(first_name={}, last_name={})'.format(self._first_name, self._last_name)

    def __repr__(self):
        return 'Person(first_name={}, last_name={})'.format(self._first_name, self._last_name)

    def display(self):
        # Creates a variable to store the correct text based on the if_salaried boolean
        if self._if_salaried:
            salary_hourly = 'Salaried employee: {}/year'.format(self._emp_salary)
        else:
            salary_hourly = 'Hourly employee: {}/hour'.format(self._emp_salary)

        # Alters the start date to the correct format month-day-year
        start_date = 'Start date: {}-{}-{}'.format(self._start_date.month, self._start_date.day, self._start_date.year)

        # Returns a string based on the given parameters in the correct format
        return '{} {}\n{}\n{}\n{}'.format(self._first_name, self._last_name, self._address, salary_hourly, start_date)


# Driver
emp1_start = datetime.datetime(2020, 6, 28)
emp2_start = datetime.datetime(2021, 1, 15)

# Assignment example
emp = Employee('Patel', 'Sasha', '123 Main Street\nUrban, Iowa', '111-222-3333', True, emp1_start, 40000)
# Original test (Check if hourly condition is reached)
emp2 = Employee('Thomas', 'Dylan', '456 Mountain Street\nDenver, Colorado', '444-555-6666', False, emp2_start, 13.50)

print(emp.display())
del emp
print('------------------')
print(emp2.display())
del emp2
