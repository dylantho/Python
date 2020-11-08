"""
Program: Multiple_Inherit.py
Author: Dylan Thomas
Last date modified: 11/7/2020
"""
import datetime

class Person:
    """Person class"""
    def __init__(self, lastname, firstname, address=''):
        self._last_name = lastname
        self._first_name = firstname
        self._address = address

    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address


class Employee:
    # Constructor
    def __init__(self, salary, start_date):
        self.salary = salary
        self._start_date = start_date
        self._start_date = '{}-{}-{}'.format(self._start_date.month, self._start_date.day, self._start_date.year)



class Manager(Person, Employee):
    def __init__(self, start_date, salary, lastname, firstname, address, department):
        super().__init__(lastname, firstname, address)
        super().__init__(start_date, salary)
        self.department = department

    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address


# Driver
my_manager = Manager(str(datetime.datetime(2020, 11, 7)), str(40000), 'Thomas', 'Dylan', '456 Mountain Street Denver, Colorado', 'IT')
print(my_manager.display())
