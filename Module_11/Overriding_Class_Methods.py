"""
Program: Overriding_Class_Methods.py
Author: Dylan Thomas
Last date modified: 11/7/2020
"""

import datetime


class Employee:
    # Constructor
    def __init__(self, lastname, firstname, address, phone):
        self._last_name = lastname
        self._first_name = firstname
        self._address = address
        self._phone_number = phone

    def __str__(self):
        return 'Person(first_name={}, last_name={})'.format(self._first_name, self._last_name)

    def __repr__(self):
        return 'Person(first_name={}, last_name={})'.format(self._first_name, self._last_name)


class SalariedEmployee(Employee):
    def __init__(self, start_date, salary, lastname, firstname, address, phone):
        super().__init__(lastname, firstname, address, phone)
        self._start_date = start_date
        self._start_date = '{}-{}-{}'.format(self._start_date.month, self._start_date.day, self._start_date.year)
        self.salary = salary

    def give_raise(self, new_salary):
        self.salary = new_salary

    def display(self):
        return 'Employee: {}, {}\nStart date: {}\nAddress: {}\nPhone: {}\nSalary: ${}'.format(self._first_name, self._last_name, self._start_date, self._address, self._phone_number, self.salary)


class HourlyEmployee(Employee):
    def __init__(self, start_date, hourly_pay, lastname, firstname, address, phone):
        super().__init__(lastname, firstname, address, phone)
        self._start_date = start_date
        self._start_date = '{}-{}-{}'.format(self._start_date.month, self._start_date.day, self._start_date.year)
        self.hourly_pay = hourly_pay

    def give_raise(self, new_wage):
        self.hourly_pay = new_wage

    def display(self):
        return 'Employee: {}, {}\nStart date: {}\nAddress: {}\nPhone: {}\nHourly Wage: ${:.2f}'.format(self._first_name, self._last_name, self._start_date, self._address, self._phone_number, self.hourly_pay)


# Driver SalariedEmployee
new_salaried_employee = SalariedEmployee(datetime.datetime(2020, 11, 7), 40000, 'Thomas', 'Dylan', '456 Mountain Street Denver, Colorado', '111-222-3333')
print(new_salaried_employee.display())
# Change salary to 45000
new_salaried_employee.give_raise(45000)
print('------------------')
print(new_salaried_employee.display())
# Garbage Collection
del new_salaried_employee

print('\n------------------\n')

# Driver HourlyEmployee
new_hourly_employee = HourlyEmployee(datetime.datetime(2020, 11, 7), 10, 'Thomas', 'Dylan', '123 Main Street Urban, Iowa', '444-555-6666')
print(new_hourly_employee.display())
# Change salary to 45000
new_hourly_employee.give_raise(12)
print('------------------')
print(new_hourly_employee.display())
# Garbage Collection
del new_hourly_employee
